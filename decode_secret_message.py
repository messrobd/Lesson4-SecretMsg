import os

def renameFiles(directory):
    original_wd = os.getcwd()
    #1. get files
    os.chdir(directory)
    file_list = os.listdir(directory)
    #2. for each file, rename
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")#to do: look this function     up
        print ("old name - " + file_name)
        print ("new name - " + new_name)
        os.rename(file_name, new_name)
    #3. go back to original working directory
    os.chdir(original_wd)

directory = "/Users/messrobd 1/github/Lesson4-SecretMsg/message_encoded"
renameFiles(directory)
