import os

def renameFiles():
    original_wd = os.getcwd()
    #1. get files
    directory = "/Users/messrobd 1/Documents/STUDY/IntroToProgramming/mod4/prank copy"
    os.chdir(directory)
    file_list = os.listdir(directory)
    #2. for each file, rename
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")#to do: look this function up 
        print ("old name - " + file_name)
        print ("new name - " + new_name)
        os.rename(file_name, new_name)
    #3. go back to original working directory
    os.chdir(original_wd)

renameFiles()
