#Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]
# def concatenates_two_list(lists1, lists2):
#     return lists1 + lists2

def concatenates_two_list(lists1, lists2):
    for i in lists2:
        lists1.append(i)
    return lists1

lists1 = ["a","b","c"]
lists2 = [1,2,3]
print(concatenates_two_list(lists1, lists2))
