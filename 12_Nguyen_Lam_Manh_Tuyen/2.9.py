# Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]
def concat(list1, list2):
    lists = []
    for i in range(0, len(list1)):
        lists.append(list1[i])
    for i in range(0, len(list2)):
        lists.append(list2[i])
    return lists
