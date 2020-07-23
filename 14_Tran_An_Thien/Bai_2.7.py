# Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.
# (Subject to availability of these constructs in your language of choice.)
# sử dụng for
total = 0

list1 = [11, 5, 17, 18, 23]

for ele in range(0, len(list1)):
    total = total + list1[ele]

print("Sum of all elements in given list: ", total)

# sử dụng while
total = 0
ele = 0

list1 = [11, 5, 17, 18, 23]

while (ele < len(list1)):
    total = total + list1[ele]
    ele += 1

print("Sum of all elements in given list: ", total)

# sử dụng đệ quy
list1 = [11, 5, 17, 18, 23]


def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


total = sumOfList(list1, len(list1))

print("Sum of all elements in given list: ", total)
