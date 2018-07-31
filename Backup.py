#Title: Folder Backup Automation
#Created by: Chris Tudehope
#Description: This is a module intended to be used to backup the world folder of a minecraft
#server. The entry point of this module is backupServer()
import shutil
import datetime
import os
import re
 
#This function is the entry point for backing up a Minecraft server.
#Paramaters
#	minecraftWorldLocation: Location of the world folder of the Minecraft server
#	backupFolder: The backup will be placed within this folder.
#Return
#	boolean: Returnes if the backup was successful
def backupServer(minecraftWorldLocation, backupFolder, maxBackupNumber):
	backupSuccess = copyDirectory(minecraftWorldLocation, backupFolder + createBackupName())
	if backupSuccess:
		manageBackupFolder(backupFolder, maxBackupNumber)
	return backupSuccess
		

#This function simply copies a folder from one place to another.
#Parameters
#	src: Path of the folder to be copied
#	dest: Location the folder will be copied to. Folder will be renamed as what dest points to.
#Return
#	boolean: Returns true if successful and false if error occurred.
def copyDirectory(src, dest):
	try:
		shutil.copytree(src, dest)
		ret = True
	except shutil.Error as e:    # Directories are the same
		print("Directory not copied. Error: %s" % e)
		ret = False
	except OSError as e:    # Any error saying that the directory doesn't exist
		print("Directory not copied. Error: %s" % e)
		ret = False
	return ret

#This function will create the name for the backup with the format:
#	world_backup_yymmdd_hhmi		
#Return
#	string: Returns the created backup name
def createBackupName():
	now = datetime.datetime.now()
	str ="world_backup_" + now.strftime("%y%m%d_%H%M")
	return str
	
#This function counts the number of backups in the backupFolder and figure outs if any
#need to be deleted.
#Parameters
#	backupFolder: Location where the backup will be placed within.
#	maxBackupNumber: Max number of backups that are allowed in the backup folder
def manageBackupFolder(backupFolder, maxBackupNumber):
	releventFileList = []
	#This is a regex that matching the name of the backup folders
	backupRegex = "world_backup_([0-9][0-9])(0[0-9]|1[0-2])([0-2][0-9]|3[0-1])_([0-1][0-9]|2[0-4])([0-5][0-9])"
	#The walk function will start at the dir passed in and trace through all of the subdirectories
	#Only want root's subdiretories so break after it is found
	for dirpath, dirnames, filenames in os.walk(backupFolder, True):
		#It should be the first iteration but going to check to be sure
		if(dirpath == backupFolder):	
			#Look through the dirs and filter out any that do not match the backup file name format
			for dir in dirnames:
				if re.fullmatch(backupRegex,dir):
					releventFileList.append(dir)
			break
	
	if len(releventFileList) > maxBackupNumber:
		#By sorting it in reverse the oldest backups will be at the back of the list
		releventFileList = sorted(releventFileList,reverse=True)
		try:
			while len(releventFileList) > maxBackupNumber:
				deletedBackup = releventFileList.pop(-1)
				shutil.rmtree(backupFolder + deletedBackup)
				print("The backup " + deletedBackup + " was deleted to make room for new backup!")
		except:
			print("Error: Deleting an old backup failed!")
	