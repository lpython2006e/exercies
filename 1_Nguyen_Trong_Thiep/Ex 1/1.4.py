# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

print("Nhập vào số n tôi sẽ trả lại tổng các số từ 1 đến n")
n = input()
i = 1
result = 0
while not n.isdigit():  # or n <= 0:
    print("Hay nhap vao so nguyen duong")
    n = input()
for i in range(int(n) + 1):
    result = result + i
print("Tong la:", result)
