'''Count all file with the extension of the input
of a directory
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
match_pattern = r'[a-zA-Z0-9]+\.' + extension
# print(match_pattern)
#  change the current directory to the input directory
current = os.chdir(p)
# print(current)
#  list all items of current directory
items = os.listdir(current)

#  count how many file with the extension inputted
count = 0
for i in items:
    if re.search(match_pattern, i, flags=re.IGNORECASE):
        count += 1

print('There are: {} file with {} extension in your directory'.format(count, extension))

