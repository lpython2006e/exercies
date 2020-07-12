# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n


tong = 0
n = int(input("nhap vao so n: "))
for x in range(n+1):
    tong += x
txt = "tong cac so tu 1 den n la: {}"
print(txt.format(tong))