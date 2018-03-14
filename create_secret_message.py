import os

original_wd = os.getcwd()
program_wd = "/Users/messrobd 1/github/Lesson4-SecretMsg"

os.chdir(program_wd)

def getCharacterImages(image_directory):
    character_image_files = os.listdir("alphabet")

    image_extension, image_extension_length = ".jpg", 4

    for index, image in enumerate(character_image_files):
        if image[-image_extension_length:] != image_extension:
            del character_image_files[index]

    return character_image_files

def makeAlphabetImageDict(character_image_files):
    alphabet = "abcdefghijklmnopqrstuvwxyz. "
    alphabet_images = {}

    for index, character in enumerate(alphabet):
        alphabet_images[character] = character_image_files[index]

    return alphabet_images

def makeMessageImageMapping(message, alphabet_images):
    message_character_images = []
    message_image_names = []

    for index, character in enumerate(message):
        message_character_images.append(alphabet_images[character])
        message_image_names.append(character_image_files[index])

    return message_character_images, message_image_names

def makeMessageImages(image_directory, message_image_mapping):
    message_character_images, message_image_names = message_image_mapping
    target_directory = os.getcwd()

    for source_name, target_name in zip(message_character_images, message_image_names):
        source_name_path = "{0}/{1}".format(image_directory, source_name)
        target_name_path = "{0}/{1}".format(target_directory, target_name)
        os.rename(source_name_path, target_name_path)

    return

#execution
message = "you smell"
