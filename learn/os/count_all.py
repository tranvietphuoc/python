#! /usr/local/bin/python3

'''Count all files with the extension of input
of the current directory
'''


import os
import re

#  input the path
p = input('Input the path to the directory you want to count: ')
if not os.path.isdir(p):
    print('Your path is not a directory!')
    exit(0)
    

# print(p)

#  input the extension name, e.g: pdf, txt, docx, xlsx,...
extension = input('Input the extesion you want to count: ')


#  function to count all file
def countFiles(path, extension):
    #  create matching pattern 
    match_pattern = r'[a-zA-Z0-9]+\.' + extension

    count = 0
    #  make a list of all items of path
    items = None
    if os.access(path, os.R_OK):
        items = os.listdir(path)
    
    if items is None:
        return None

    for item in items:
        #  recusive if the item is a directory
        if os.path.isdir(os.path.join(path, item)) and os.access(os.path.join(path, item), os.R_OK):
            count += countFiles(os.path.join(path, item), extension)
        if re.search(match_pattern, item, flags=re.IGNORECASE):
            count += 1
    
    return count


if countFiles(p, extension) is None:
    print('You do not have permission to access this directory!')
print('There are {} files .{} in your directory!'. format(countFiles(p, extension), extension))

    
