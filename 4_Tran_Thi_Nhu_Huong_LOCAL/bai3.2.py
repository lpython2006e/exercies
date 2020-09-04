"""Write a program that read content of a file (path) then show to screen, if the file doesn’t exist, announce user"""


def _check_existence(a):
    try:
        f = open(filename, "r")
    except:
        return False
    return True


filename = input("Please input filename")
check = _check_existence(filename)
if check:
    f = open(filename, "r")
    content = f.read()
    #todo: nen xuong dong
    print("this is content ", content)
else:
    print("file does not exist")


