"""
Modify the previous program such that only multiples of three or five are considered
in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
"""

tong = 0
n = int(input("nhap vao so n: "))
for x in range(n+1):
    if(x%3==0 or x%5==0):
        tong += x
txt = "tong cac so tu 1 den n la: {}"
print(txt.format(tong))