import argparse
import sys
import os

parser = argparse.ArgumentParser(description="pyton implemented find")
parser.add_argument('path', nargs='?', action='store', type=str, default='./')
parser.add_argument('find', action='store', type=str)
args = vars(parser.parse_args())

for root, dirs, files in os.walk(args['path'], topdown=True):
    for file in files:
        file_splt = file.split('.')
        if file_splt[0] == args['find'].split('.')[0]:
            print(root)

