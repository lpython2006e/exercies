#Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]
def concatenates(list_1,list_2):
    return list_2 + list_1
list_3 = ['a','b','c']
list_4 = [1,2,3]
print(concatenates(list_3,list_4))