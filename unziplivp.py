#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
unziplivp
~~~~~~~~~~~
Unzip all the files in the .livp file in the current directory to the current directory without deleting the .livp file. 

After each .livp file is decompressed, a picture file and a .mov file are obtained. They are named after the .livp file.

usage:
Go to the directory where the .livp file is stored in the Linux terminal or Windows command prompt window, and execute: 
python unziplivp.py
"""

import os
import zipfile
import shutil


def un_zip(file_name):
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names, file_name + "_files/")
    zip_file.close()


def main():
    for file_name in os.listdir("."):
        if file_name.endswith(".livp"):
            un_zip(file_name)
            for tempfile in os.listdir("./" + file_name + "_files/"):
                if tempfile.endswith(".mov"):
                    oldfile = "./" + file_name + "_files/" + tempfile
                    newfile = "./" + file_name.rstrip(".livp") + ".mov"
                    shutil.copyfile(oldfile, newfile)
                else:
                    oldfile = "./" + file_name + "_files/" + tempfile
                    newfile = "./" + file_name.rstrip(".livp") + "." + tempfile.split(".")[-1]
                    shutil.copyfile(oldfile, newfile)

            shutil.rmtree("./" + file_name + "_files/")


if __name__ == '__main__':
    main()
