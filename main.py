import os
from os.path import isfile, join
import shutil


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
    '7z' : 'archive',
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


# loop through files and get extensions
for file in list_files:
    extension = file.split('.')[-1].lower()
    if extension in extensions.keys():
        new_dir = extensions[extension]
        new_path = os.path.join(path, new_dir)
        current_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            shutil.move(current_path, new_path)
        else:
            os.makedirs(new_path, exist_ok=True)
            shutil.move(current_path, new_path)
    else:
        new_dir = 'other'
        new_path = os.path.join(path, new_dir)
        current_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            shutil.move(current_path, new_path)
        else:
            os.makedirs(new_path, exist_ok=True)
            shutil.move(current_path, new_path)