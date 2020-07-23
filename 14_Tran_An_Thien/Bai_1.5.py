# Modify the previous program such that only multiples of three or five are considered in the sum,
# e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

tong = 0
number = int(input('nhap vao so n: '))
# while not number>0 or number>17:
#     number = int(input('moi ban nhap vao so nguyen duong: '))
for i in range(1, 18):
    if ((i % 3 == 0) | (i % 5 == 0)) & (number <= 17):
        tong += i
print('Tổng cac so tu 1 den n là: ', tong)
