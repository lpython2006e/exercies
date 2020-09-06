"""Write a function that returns the elements on odd positions in a list."""


def odd_elements_list(a):
    odd_list = []
    for i in range(0, len(a)):
        if i % 2 != 0:
            odd_list.append(a[i])
    else:
        i += 1
    return odd_list


mylist = [1, 4, 5, 100, 2, 1, -1, -7]
odd = odd_elements_list(mylist)
print(odd)
