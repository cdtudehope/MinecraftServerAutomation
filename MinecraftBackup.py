#Title: Minecraft Server Shutdown and Backup Automation
#Created by: Chris Tudehope
#Description: This program automates the operation of backing up a Minecraft server
# by copying the world folder. 
import time
from Backup import backupServer

#Start of program
backupSrc = "/Users/minecraftserver/Desktop/Minecraft/world"	
backupDest = "/Users/minecraftserver/Desktop/MinecraftBackups/"
print("Minecraft Backup is in Progress. It takes awhile :(")
if backupServer(backupSrc,backupDest,10) == True:	#Check if backup occurred
	print("A backup was created in the folder: " + backupDest)
	#Give the user time to see final console output
	time.sleep(5)
else:
	print("Backup aborted because of server backup error.")
	#Give the user time to see final console output
	time.sleep(10)
	