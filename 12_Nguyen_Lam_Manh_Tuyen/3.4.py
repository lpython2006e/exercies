#Update previous one, allow to enter multiple classmate, at end, allow to save to file as CSV format
import pandas
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

def multiple_input():
    name, birthday, email=[],[],[]
    num=int(input(" How many students do you want to add?\n"))
    for i in range(0,num):
        temp=list(getinput())
        name.append(temp[0])
        birthday.append(temp[1])
        email.append(temp[2])
    return name, birthday, email

class_list=list(multiple_input())

print("Your enter the Student info:",class_list)
filename = input("Please input file name \n")

df = pandas.DataFrame(data={"Name": class_list[0], "Birthday": class_list[1],"Email":class_list[2]})
df.to_csv(filename, sep=',',index=False)