import os
from shutil import copyfile
import random

def getCharacterImages(image_directory):
    character_image_files = os.listdir(image_directory)

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

def makeMessageImageMapping(message, alphabet_images, character_image_files):
    message_character_images = []
    message_image_names = []

    for index, character in enumerate(message):
        message_character_images.append(alphabet_images[character])
        message_image_names.append(character_image_files[index])

    return message_character_images, message_image_names

def makeMessageImages(image_directory, target_directory, message_image_mapping):
    message_character_images, message_image_names = message_image_mapping

    os.mkdir(target_directory)

    for source_name, target_name in zip(message_character_images, message_image_names):
        source_name_path = "{0}/{1}".format(image_directory, source_name)
        target_name_path = "{0}/{1}".format(target_directory, target_name)
        copyfile(source_name_path, target_name_path)

    return

def makeEncodingPrefixes(message_images):
    message_prefixes = []
    for index, image in enumerate(message_images):
        if index < 10:
            index = ("0" + str(index))
        else:
            str(index)
        message_prefixes.append(index)

    return message_prefixes

def getEncodingPrefix(message_prefixes):
    prefix_index = random.randint(0, len(message_prefixes)-1)
    prefix = message_prefixes[prefix_index]
    del message_prefixes[prefix_index]

    return prefix

def encodeMessage(message, target_directory):
    original_wd = os.getcwd()
    program_wd = "/Users/messrobd 1/github/Lesson4-SecretMsg"

    os.chdir(program_wd)
    character_image_files = getCharacterImages("alphabet")
    alphabet_images = makeAlphabetImageDict(character_image_files)
    message_image_mapping = makeMessageImageMapping(message, alphabet_images, character_image_files)

    makeMessageImages("alphabet", target_directory, message_image_mapping)
    message_images = os.listdir(target_directory)
    message_prefixes = makeEncodingPrefixes(message_images)

    os.chdir(target_directory)
    for image in message_images:
        prefix = getEncodingPrefix(message_prefixes)
        encoded_name = prefix + image
        os.rename(image, encoded_name)

    os.chdir(original_wd)

    return

#execution
message = "you smell"
target_directory = "message_encoded"

encodeMessage(message, target_directory)
