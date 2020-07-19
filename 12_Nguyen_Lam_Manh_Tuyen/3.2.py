#Write a program that read content of a file (path) then show to screen, if the file doesn’t exist, announce user

def read_file():
    filepath=input("Please input file name & path \n")
    try:
        file=open(filepath,"r")
    except (ValueError):
        print("File doesn't exist")
    else:
        content=file.read()
        print("Content: \n",content)

read_file()