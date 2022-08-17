import argparse
import sys
import os

"""python implementation of unix find function"""

parser = argparse.ArgumentParser(description="pyton implemented find")
parser.add_argument('path', nargs='?', action='store', type=str, default='./')
parser.add_argument('find', action='store', type=str)
args = vars(parser.parse_args())

for root, dirs, files in os.walk(args['path'], topdown=True):
    for file in files:
        file_splt = file.split('.')
        args_splt = args['find'].split('.')
        if file_splt == args_splt:
            print(root)

