import fnmatch
import os
import argparse
import eyed3

parser = argparse.ArgumentParser(description='Read mp3 tags.')
parser.add_argument('-f', '--folder', default=".", help='Starting folder')
parser.add_argument('-a', '--artist', help='artist name')
args = parser.parse_args()

matches = []
for root, dirnames, filenames in os.walk(args.folder):
  for filename in fnmatch.filter(filenames, '*.mp3'):
      matches.append(os.path.join(root, filename))

for song in matches:

    audiofile = eyed3.load(song)
    audiofile.tag.artist = unicode(args.artist)
    audiofile.tag.save()
