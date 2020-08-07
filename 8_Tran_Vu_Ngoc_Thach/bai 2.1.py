"""Write a function that returns the largest element in a list."""


def largest_element(a):
    return max(a)


mylist = [1, 4, 5, 100,  2, 1, -1, -7]
max = largest_element(mylist)
print("The largest value is ", max)
