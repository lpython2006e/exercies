# Write a function that returns the largest element in a list.
def largest_ele(ele):
    ele.sort()
    result = ele[len(ele) - 1]
    return result


print(largest_ele([1, 10, 5]))
