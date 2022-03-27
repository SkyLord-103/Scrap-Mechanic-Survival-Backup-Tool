import os
from os import path
import sys
import shutil
import time
# from datetime import datetime as dt

def Closing():
    print("(Closing in 1.5/s)")
    time.sleep(1.5)
    sys.exit(1)

appdata = os.getenv('appdata')
Saves = path.join(appdata, "Axolot Games\\Scrap Mechanic\\User")
usr = os.listdir(Saves)[0]

if (not "User_" in usr) or not usr:
    print("Could not find the proper folder")
    Closing()

Saves = path.join(Saves, usr, "Save\\Survival")
DefaultName = "My World Name.db"
Name = input("Please specify a file to backup (%s)" % DefaultName)
if Name.lower() == "n" or Name.lower() == "": Name = DefaultName

if not path.exists(path.join(Saves, Name)):
    print("The name you gave was not found!")
    Closing()


# date = str(dt.date(dt.now()))[5:]
# backupname = Name.split(".")[0] + ".backup-{}.db".format(date[5:]) # If you want to date the backup by the day and month

backupname = Name.split(".")[0] + ".backup.db"

shutil.copy2(path.join(Saves, Name), path.join(Saves, backupname))

print("Done.")
Closing()