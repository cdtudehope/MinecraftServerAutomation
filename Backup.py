import shutil
import datetime
 
 
#This function is the entry point for backing up a Minecraft server.
#Paramaters
#	minecraftWorldLocation: Path of the folder to where the Minecraft server's world folder is contained.
#	backupFolder: Location where the backup will be placed within. The backup will be placed within this folder.
#Return
#	boolean: Returnes if the backup was successful
def backupServer(minecraftWorldLocation, backupFolder):
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
		return True
	except shutil.Error as e:    # Directories are the same
		print('Directory not copied. Error: %s' % e)
		return False
	except OSError as e:    # Any error saying that the directory doesn't exist
		print('Directory not copied. Error: %s' % e)
		return False

#This function will create the name for the backup with the format:
#	worldBackupyymmdd_hhmi		
#Return
#	string: Returns the created backup name
def createBackupName():
	now = datetime.datetime.now()
	str ="worldBackup" + now.strftime("%y%m%d_%H%M")
	return str
	