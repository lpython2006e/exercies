"""
    "Create a “MathUtils” class that have ability to solve
    Sum of range input
    solve quadratic equations
    Calculate the area of 4 type of shape (circle, rectangle, triangle, Pentagon)"
"""

from My_Math import *
import math

print(math.pi)
a = int(input("nhập giá trị a: "))
b = int(input("nhập giá trị b: "))
c = int(input("nhập giá trị c: "))
d = int(input("nhập giá trị d: "))

print(add(a, b))

print(giaiPTBac2(a, b, c))

print("diện tích hình chữ nhật là: ", dien_tich_HCN(a, b))
