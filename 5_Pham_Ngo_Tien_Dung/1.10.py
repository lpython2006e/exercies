# "Tạo một chương trình bằng Python, giải phương trình bậc hai
# A.x2 + B.x1 + C = 0
# Trong đó A, B, C là số thực (có thể âm), hãy tìm X. "


from math import sqrt

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhcp c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        if c == 0:
            print("Phuong trinh co 1 nghiem x = 0")
        else:
            print("Phuong trinh co 1 nghiem x = ", -c / b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))