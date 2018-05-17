#!/usr/bin/env python3

"""
Initial version taken from https://codereview.stackexchange.com/a/113684/169862

Development Notes:
1. Hardcoded check for file ending currently - improve later.
2. Tested only with default python packages shipping in Ubuntu 18.04

"""

import os
import glob
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(fn):
    # Function to extract Image metadata
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

# Manually adding file endings that we want to convert
files = glob.glob("*.jpg") + glob.glob("*.JPG") + glob.glob("*.jpeg")

for file in files:
    
    ptime = get_exif(file)["DateTimeOriginal"]
    ptime = ptime.replace(":", "")
    ptime = ptime.replace(" ", "_")
    # If filename already exists append _x to save image with a different name.
    number = 0
    new_name = ptime+".jpg"
    if new_name == file:
        print(new_name, "is already ok")
        continue
    while os.path.exists(new_name):
        number += 1
        new_name = ptime+"_"+str(number)+".jpg"
    os.rename(file, new_name)
    print(file + " renamed to " + new_name)

