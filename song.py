import re
import fileinput

songs = []
with open('songlist.txt', 'r') as file:
    # reading each line
    for line in file:
        # reading each word
        for word in fileinput.input("songlist.txt.txt", inplace=True):
            print(re.sub("\d+", "", line))
