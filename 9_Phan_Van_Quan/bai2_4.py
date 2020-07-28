#Write a function that returns the elements on odd positions in a list.
def old_position(list_1):
    for num in range(len(list_1)):
        if num % 2 == 1:
            print(list_1[num])
list_2 = [1,2,3,4,4,2,3,'s','f','w',1,3,23]
old_position(list_2)