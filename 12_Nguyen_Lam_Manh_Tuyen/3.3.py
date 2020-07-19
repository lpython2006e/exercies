#Write a program that allow user to enter classmate (name, Birthday, Email), validate if enter values are valid format (limit length apply), else ask user to enter again per field

def getinput():

    while True:
        name = input("Please input student name\n")
        if len(name)<=12:
            break
        else:
            print("Name can only contain a maximum of 12 characters")
            continue
    while True:
        birth = input("Please input student birthday mm/dd/yy \n")
        if len(birth)<=8:
            break
        else:
            print("Birthday can only contain a maximum of 8 characters")
            continue
    while True:
        email = input("Please input student email\n")
        if len(email)<=50:
            break
        else:
            print("Name can only contain a maximum of 50 characters")
            continue

    return name,birth,email
    return name
Student=getinput()
print("Your enter the Student info:",Student)