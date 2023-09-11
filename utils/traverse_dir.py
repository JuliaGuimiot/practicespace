import os
import fnmatch

for dirpath, dirnames, files in os.walk('.', topdown=False):
    print(f'Found directory: {dirpath}')
    for file in files:
        if fnmatch.fnmatch(file, 'tasks.py'):
            print(file)
