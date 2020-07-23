# Write a function that returns the elements on odd positions in a list.
def return_odd_position_element(list_a):
    c = []
    for i in range(1, len(list_a), 2):
        c.append(a[i])
    return c


a = [41, 19, 74, 107, 12309, -82, 64, 39, 501, 124, 70, 1111]
odd_element_list = return_odd_position_element(a)
print(odd_element_list)
