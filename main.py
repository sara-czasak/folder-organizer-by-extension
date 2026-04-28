# TODO 1: Get filepath for dir to be organized
# TODO 2: List all the files in dir
# TODO 3: Loop through files and find extensions
# TODO 4: Make dirs for each file type
# TODO 5: Move files to corresponding dir
# TODO 6: If file has unknown extension put into dir 'other'
import os
from os.path import isfile, join


# Extensions dict
extensions = {
    'jpg': 'images',
    'jpeg': 'images',
    'png' : 'images',
    'mp4' : 'video',
    'webm' : 'video',
    'mp3' : 'audio',
    'wav' : 'audio',
    'zip' : 'archive',
    'z7' : 'archive',
    'doc' : 'document',
    'pdf' : 'document',
    'docx' : 'document',
}


# Get file path and validate path
path = ''
valid_path = False
while not valid_path:
    path = input("Enter folder path for folder to be organized: ")
    if os.path.exists(path):
        valid_path = True
    else:
        print("Folder does not exist. Please try again.")

# Get list of all files in dir excluding subdirs
list_files = [f for f in os.listdir(path) if isfile(join(path, f))]
