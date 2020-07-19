# Write a program that allow user enter a file name (path) then content, allow user to save it
print('Type your path of file:')
title = input()
print('Type your content:')
content = input()

f = open(title, 'a')  # w
f.write(content)
f.close()
print('The content of', title, ':')
f = open(title, 'r')
print(f.read())
f.close()
