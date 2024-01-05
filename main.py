import os

GAME_FILES_PATH = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV"
MOD_FILES_PATH = "C:/Users/Lily/Documents/Paradox Interactive/Europa Universalis IV/mod/PostFinem_PreRelease"
LOC = "/localisation"
ENGLISH = "_l_english.yml"

os.chdir(GAME_FILES_PATH+LOC)
files = os.listdir()
files = [f for f in files if f[-14:] == ENGLISH] # Filter for english files only

with open(files[0], encoding="UTF-8-sig") as f:
    lines = f.readlines()

print(lines[:10])
