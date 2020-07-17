# Write a function that checks whether an element occurs in a list.

def checklist(a, b):
    if a in b:
        return "True"
    else:
        return "False"


number = int(input("nhap: "))
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(checklist(number, mylist))
