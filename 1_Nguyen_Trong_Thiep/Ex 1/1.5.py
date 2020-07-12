# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9,
# 10, 12, 15 for n=17

print("Nhập vào số n")
n = input()
i = 1
result = 0
while not n.isdigit():  # or n <= 0:
    print("Hay nhap vao so nguyen duong")
    n = input()
for i in range(int(n) + 1):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i
print("Tong la:", result)
