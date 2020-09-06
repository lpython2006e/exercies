"""Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17"""

print("please input the number")
number = input("input your number")
k=0
for i in range(1,int(number)+1):
    if (i%3==0 or i%5==0):
        k+=i

string = "sum is {}"
print(string.format(k))