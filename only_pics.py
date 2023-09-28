import fnmatch
import os

def delete_files(folder):
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, '*.jpg'):
            pass
        else:
            print("Removed", file)
            os.remove(folder + "/" + file)