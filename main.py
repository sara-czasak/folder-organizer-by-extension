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
    "images": ["jpg", "jpeg", "png"],
    "video": ["mp4", "webm"],
    'audio': ['mp3', 'wav'],
    'archive': ['zip', '7z'],
    'document': ['doc', 'docx'],
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
