Quick script to scan through localisation files of a game to find entries containing a keyword that have not been overriden in mod files.
The purpose is to find mentions of a name that is intended to be renamed in a mod, so that all mentions of it can be caught.

Localisation entries are in the following format:
 {key}:0 "{loc}"
The 0 is optional and ignored, there can also be comment lines starting with # and every file starts with the line "l_english:"

The text files are scanned and entries are converted into a dictionary mapping keys to their loc strings. This is wrapped in the collect_loc_map() function that I then use to collect dictionaries of both the game and mod files and compare.
Any entries in the game files that are not overwritten in the mod files and contain a specific keyword are printed out. Since there are a lot of false positive results/entries that are unnecessary to change these results then require manual parsing.
