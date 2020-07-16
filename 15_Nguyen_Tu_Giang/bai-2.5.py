# Write a function that computes the running total of a list.
def total(list_ele, count=0):
    for i in list_ele:
        # print(type(i))
        if str(i).isdigit():
            count += i
    return count


print(total([1, 's', 0, 'e', 3, 6]))
