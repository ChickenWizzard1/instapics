import instaloader
from instaloader import *
from only_pics import *

target_user = str(input("Enter the profile you want to download: "))
# Get instance
L = instaloader.Instaloader()
L.download_profile(target_user, profile_pic_only= False)

delete_files(target_user)
