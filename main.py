import os

GAME_FILES_PATH = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV"
MOD_FILES_PATH = "C:/Users/Lily/Documents/Paradox Interactive/Europa Universalis IV/mod/PostFinem_PreRelease"
LOC = "/localisation"
ENGLISH = "_l_english.yml"

os.chdir(GAME_FILES_PATH+LOC)
files = os.listdir()
files = [f for f in files if f[-14:] == ENGLISH] # Filter for english files only

def process_file(lines):
    """ Take the lines of a file and process them into a dictionary. """
    loc_map = {}
    for line in lines:
        line = line.strip()
        if line == "l_english:" or line[0] == "#":
            continue

        key, *rest = line.split(":") # Cut key by first :
        _, *loc = ":".join(rest).split('"') # Cut loc string by first "
        loc = '"'.join(loc)[:-1] # Remove last "
        loc_map[key] = loc
    return loc_map

with open(files[0], encoding="UTF-8-sig") as f:
    lines = f.readlines()

d = process_file(lines)
print(d["PROV4818"])
print(d["flavor_iro.3.t"])
