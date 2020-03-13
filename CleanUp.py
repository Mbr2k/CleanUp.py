import os
import shutil
import time

'''
    For the given path, get the List of all files in the directory tree 
    https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

'''
    For the given list of file paths, get a list of all filepaths for those modified >2weeks ago
'''
def getListOfOldFiles(dirFiles):
    # Create a list of files that are older than 2 weeks
    # for the filenames given
    oldFiles = list()
    curr_time = time.time()
    # Iterate over all the entries
    for entry in dirFiles:
        # 1209600 is the number of seconds in 2 weeks:
        if  (curr_time - os.path.getmtime(entry)) > 1209600:
            oldFiles.append(entry)
                
    return oldFiles

'''
    For the given list of file paths, move them to the specified destination path
'''
def moveFiles(destination, dirFiles):
    # Iterate over all the entries
    # cuts and pastes, but does not work
    # if an entry of same name is already 
    # in destination
    for entry in dirFiles:
        shutil.move(entry, destination)

'''
    Main driver code:
'''
allFiles = getListOfFiles("G:/DL")

for entry in allFiles:
    print("All Files incl.:" + entry)

oldFiles = getListOfOldFiles(allFiles)
for entry in oldFiles:
    print("Moving Old File :" + entry)

moveFiles("I:\DL", oldFiles)
