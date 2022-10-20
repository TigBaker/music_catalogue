import os

# creates file with music artist and albums from a given directory
target_dir = input("Enter full path to target directory: ")
root = os.path.basename(target_dir)


# Takes input from user and creates file to add music info
music_list = input("Enter name for file: ")
f = open(music_list, 'a+')


for path, sub_dir, filenames in os.walk(target_dir):
    for album in sub_dir:
        artist = os.path.basename(path)
        if artist != root:
            entry = os.path.join(artist, album)
            f.write(entry + "\n")

f.close()
