#Write a program that allow user enter a file name (path) then content, allow user to save it

#get list from user input until none input
def getinput():
    filename=input("Please input file name \n")
    print("Please input your content \n")
    while True:
        element=input()
        if element!='':
            content.append(element)
        else:
            break
    print(filename)
    return filename,content

def write_to_file(filename,content):
    file = open(filename,"w")
    for ele in content:
        file.write(ele+"\n")
    file.flush()
    file.close()

content=[]
user_input=getinput()
write_to_file(user_input[0],user_input[1])