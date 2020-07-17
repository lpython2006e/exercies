#Modify the previous program such that only the users Alice and Bob are greeted with their names.
names=["Alice","Bob"]
name=()
while name not in names:
    print("Please input your name")
    name = input()
    if name=="Alice":
        print("Hello",name)
    elif name=="Bob":
        print("Hello",name)
