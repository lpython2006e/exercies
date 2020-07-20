"""Write a program that allow user enter a file name (path) then content, allow user to save it"""

filename = input("Please input filename")
f= open(filename,"w+")
content = input("Please input content")
f.write(content)