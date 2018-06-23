import shutil
import datetime
 
#This function simply copies a folder from one place to another.
#Parameters
#	src: Path of the folder to be copied
#	dest: Location the folder will be copied to. Folder will be renamed as what dest points to.
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

#This function will create the name for the backup with the format:
#	worldBackupyymmdd_hhmi		
def createBackupName():
	now = datetime.datetime.now()
	str ="worldBackup" + now.strftime("%y%m%d_%H%M")
	return str

print("Minecraft Backup is in Progress:) It only takes a million years:(")	
print("\nHere is a flying pig for your wait:)")
print("\n         _____ ____")
print("        `----,\\    )")
print("         `--==\\\\  /")
print("          `--==\\\\/")
print("        .-~~~~-.Y|\\\\_")
print("     @_/        /  66\\_")
print("       |    \\   \\   _(\")")
print("        \\   /-| ||'--'")
print("         \\_\\  \\_\\\\")

backupSrc = "E:\\ServerForThePlex\\world"	
backupDest = "C:\\MinecraftBackups\\" + createBackupName()
copyDirectory(backupSrc,backupDest)
print("A backup was created in the folder: " + backupDest)