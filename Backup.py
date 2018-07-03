import shutil
import datetime
import os
import re
 
 
#This function is the entry point for backing up a Minecraft server.
#Paramaters
#	minecraftWorldLocation: Path of the folder to where the Minecraft server's world folder is contained.
#	backupFolder: Location where the backup will be placed within. The backup will be placed within this folder.
#Return
#	boolean: Returnes if the backup was successful
def backupServer(minecraftWorldLocation, backupFolder, maxBackupNumber):
	manageBackupFolder(backupFolder, maxBackupNumber)
	return copyDirectory(minecraftWorldLocation, backupFolder + createBackupName())

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

#This function will create the name for the backup with the format:
#	worldBackupyymmdd_hhmi		
#Return
#	string: Returns the created backup name
def createBackupName():
	now = datetime.datetime.now()
	str ="worldBackup" + now.strftime("%y%m%d_%H%M")
	return str
	
#This function counts the number of backups in the backupFolder and figure outs if any
#need to be deleted. Intended to be called before backup.
#Parameters
#	backupFolder: Location where the backup will be placed within.
#	maxBackupNumber: Max number of backups that are allowed in the backup folder
def manageBackupFolder(backupFolder, maxBackupNumber):
	releventFileList = []
	#This is a regex that matching the name of the backup folders
	backupRegex = "worldBackup([0-9][0-9])(0[0-9]|1[0-2])([0-2][0-9]|3[0-1])_([0-1][0-9]|2[0-4])([0-5][0-9])"
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
	
	if len(releventFileList) >= maxBackupNumber:
		#By sorting it in reverse the oldest backups will be at the back of the list
		releventFileList = sorted(releventFileList,reverse=True)
		#need to end up with maxBackupNumber - 1 so that when the backup is done the 
		#backup count will equal maxBackupNumber
		try:
			while len(releventFileList) >= maxBackupNumber:
				deletedBackup = releventFileList.pop(-1)
				shutil.rmtree(backupFolder + deletedBackup)
				print("The backup " + deletedBackup + " was deleted to make room for new backup!")
		except:
			print("Error: Deleting an old backup failed!")
	
		
		
backupServer("/Users/christudehope/Desktop/testFolder", "/Users/christudehope/Desktop/testBackupFolder/", 5)
	