import fnmatch
import os




def keep_pictures(folder):
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, '*.jpg'):
            pass
        else:
            print("Removed", file)
            os.remove(folder + "/" + file)

def keep_videos(folder):
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, '*.mp4') or fnmatch.fnmatch(file, '*.jpg'):
            pass
        else:
            print("Removed", file)
            os.remove(folder + "/" + file)
