"""Write a function that computes the running total of a list."""


def count_total(a):
    b = 0
    for i in range(0, len(a)):
        b+=a[i]
    return b


mylist = [1,2,3,5,-1]
count = count_total(mylist)
print(count)
