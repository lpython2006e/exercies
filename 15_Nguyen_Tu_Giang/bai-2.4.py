# Write a function that returns the elements on odd positions in a list.
def odd_position(list_ele, list_ele_odd=[]):
    for i in range(1, len(list_ele), 2):
        list_ele_odd.append(list_ele[i])
    return list_ele_odd


print(odd_position([3, 'list', 4, 0, 'element', 'i', 'odd']))
