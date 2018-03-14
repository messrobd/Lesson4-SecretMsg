import os

original_wd = os.getcwd()
program_wd = "/Users/messrobd 1/github/Lesson4-SecretMsg"

os.chdir(program_wd)

character_image_files = os.listdir("alphabet")

i = 0
for image in character_image_files:
    if image[-4:] != ".jpg":
        del character_image_files[i]
    i += 1

print character_image_files

alphabet = "abcdefghijklmnopqrstuvwxyz. "
alphabet_images = {}

for index, character in enumerate(alphabet):
    alphabet_images[character] = character_image_files[index]
