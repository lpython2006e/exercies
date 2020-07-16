# Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]


def concatenates(list_1, list_2, i=0):
    while i < len(list_2):
        list_1.append(list_2[i])
        i += 1
    return list_1


list_a = ['a', 'b', 'c']
list_b = ['1', '2', '3']
print(concatenates(list_a, list_b))
