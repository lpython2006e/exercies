"""Write a program that asks the user for a number n and prints the sum of the numbers 1 to n."""

print("please input the number")
number = input("input your number")
k=0
for i in(1,int(number)):
    k+=i

string = "sum is {}"
print(string.format(k))