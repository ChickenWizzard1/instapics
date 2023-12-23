import instaloader
from instaloader import *
from only_pics import *
L = instaloader.Instaloader()
USER = str(input("Enter  your username: "))
PASSWORD = str(input("Enter your password: "))
try:
    L.login(USER, PASSWORD)
except:
    try:
        L.load_session_from_file(USER)
    except:
        print("Please login to instagram using firefox, then run 615_import_firefox_session.py")

# add profils you want to download
users = []
users.append(str(input("Enter the profile you want to download: ")))
for i in range(len(users)):
    L.download_profile(users[i], profile_pic_only= False)
    profile = Profile.from_username(L.context, users[i])

# Get Followers
    followers = []
    for follower in profile.get_followees():
        followers.append(follower.username)
    print("Followers: ", followers)


    for highlight in L.get_highlights(profile.userid):
    # highlight is a Highlight object
        for item in highlight.get_items():
        # item is a StoryItem object
            L.download_storyitem(item, users[i])
    keep_files = int(input("1: Keep all files \n 2: Only keep pictures \n 3: Only keep pictures and videos \n Your Choice: "))
    if keep_files == 2:
        keep_pictures(users[i])
    if keep_files == 3:
        keep_videos(users[i])
