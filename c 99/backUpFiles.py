import os
import shutil


source = input("enter sorce folder name:")
destination = input("enter destination folder name:")

source = source+'/'
destination = destination+'/'


list_of_file=os.listdir(source)
for file in list_of_file:
    shutil.move((source+file),destination)
