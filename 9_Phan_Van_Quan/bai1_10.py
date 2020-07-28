# Make a program in Python, that solve quadratic equations
# A.x2 + B.x1 + C = 0
# Where A, B, C is real numbers (could be negative), find X.
# using function
import math
def giaiPT(A, B, C):
    # kiem tra he so
    if A == 0:
        if B == 0:
            print("Phuong trinh vo nghiem")
        else:
            print("Phuong trinh co nghiem la x = ", + (-C/B))
    # tinh delta
    delta = B*B - 4*A*C
    # tinh nghiem
    if (delta > 0):
        x1 = float(-B + math.sqrt(delta) / 2*A )
        x2 = float(-B - math.sqrt(delta) / 2*A )
        print("phuong trinh co 2 nghiem la x1 = ", x1, "x2 =", x2)
    elif(delta == 0):
        x = (-B / 2*A)
        print("phuong trinh co nghiem kep x1 = x2 =", x)
    else:
        print("phuong trinh vo nghiem")
A = float(input("Nhap vao he so A "))
B = float(input("Nhap vao he so B "))
C = float(input("Nhap vao he so tu do C "))
giaiPT(A,B,C)
