# Write a program that read content of a file (path) then show to screen, if the file doesn’t exist, announce user
import os

print('Type your the file:')
url = input()
# try:
#     f = open(url, 'r')
#     print(f.read())
# except FileNotFoundError:
#     print('File not accessible.')

# Using os.path
if os.path.isfile(url):
    f = open(url, 'r')
    print(f.read())
    f.close()
else:
    print('File not exist')

