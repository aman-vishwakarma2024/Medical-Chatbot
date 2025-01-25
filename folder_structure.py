import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # basic logging configuration it will print the time and message which i want to print

# creating list of files which i want to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
   " test.py"
]

# 
for filepath in list_of_files:
    filepath = Path(filepath) # converting the string to path object so that this code can run in windows and linux as well
    filedir, filename = os.path.split(filepath) #splitting the path into directory and filename


    if filedir !="": # if the directory is not empty then create the directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # checking if the file is not exists or the file is empty , then create new file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

       
    else: #if file already exists then print the message that file already exists
        logging.info(f"{filename} is already exists")