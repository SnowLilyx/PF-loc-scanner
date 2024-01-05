import os

GAME_FILES_PATH = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV"
MOD_FILES_PATH = "C:/Users/Lily/Documents/Paradox Interactive/Europa Universalis IV/mod/PostFinem_PreRelease"
LOC = "/localisation"

os.chdir(GAME_FILES_PATH+LOC)
files = os.listdir()

with open(files[0], encoding="UTF-8") as f:
    lines = f.readlines()

print(lines[:10])
