# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
tong = 0
number = int(input('nhp vao so n: '))
while not number > 0:
    number = int(input('moi ban nhap vao so nguyen duong: '))
for i in range(1, number + 1):
    tong += i
print('Tổng cac so tu 1 den n là: ', tong)
