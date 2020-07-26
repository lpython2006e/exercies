"""Modify the previous program such that only the users Alice and Bob are greeted with their names.."""

print("please input your name")
your_name = input("what is your name?")
if your_name in ("Alice","Bob"):
    print("welcome to my world " + your_name)
else:
    print ("you are not Alice or Bob")