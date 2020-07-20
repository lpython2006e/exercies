# "Create a “MathUtils” class that have ability to solve
# Sum of range input
# solve quadratic equations
# Calculate the area of 4 type of shape (circle, rectangle, triangle, Pentagon)

''''
"Tạo một lớp MathUtils có khả năng giải quyết:
Tính tổng đầu vào
Giải phương trình bậc hai
Tính diện tích của 4 loại hình dạng (hình tròn, hình chữ nhật, hình tam giác, hình ngũ giác)
'''
from math import sqrt


class MathUtils:

    def __init__(self, n, a, b, c, d, e, r):
        self.n = n
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.r = r

    def sum_of_range_input(self, n):
        for i in range(n):
            x = int(input("nhap so: "))
            number_list.append(x)
        print("Tong: ", sum(number_list))

    def solve_quadratic_equations(self, a, b, c):
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
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                print("Phương trình vô nghiệm!")
            elif delta == 0:
                print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
            else:
                print("Phương trình có 2 nghiệm phân biệt!")
                print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
                print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))

    def calculate_the_area_of_circle(self, r):
        return r ** 2 * 3.14

    def calculate_the_area_of_rectangle(self, a, b):
        return a * b

    def calculate_the_area_of_triangle(self, a, b, c):
        if (a + b > c and a + c > b and b + c > a):
            p = 1 / 2 * (a + b + c)
            return sqrt(p * (p - a) * (p - b) * (p - c))
        else:
            print("not triangle, try again")

    def calculate_the_area_of_pentagon(self, a, b, c, d, e):
        pass


number_list = []
_math = MathUtils('', '', '', '', '', '', '')

print("""
1. Tinh tong
2. giai pt bac 2
3. tính dien tich cac hinh
""")
x = int(input("nhap lua chon cua ban: "))

if (x == 1):
    n = int(input("nhap so cac so can tinh: "))
    _math.sum_of_range_input(n)
elif (x == 2):
    print("pt co dang: ax^2+bx+c=0")
    a = float(input("nhap a: "))
    b = float(input("nhap b: "))
    c = float(input("nhap c: "))
    _math.solve_quadratic_equations(a, b, c)
else:
    canh = int(input("nhap so canh: "))
    if (canh == 0):
        ban_kinh = float(input("nhap ban kinh: "))
        print("dien tich hinh tron: ", _math.calculate_the_area_of_circle(ban_kinh))
    elif (canh == 2):
        canh_thu_nhat = float(input("nhap canh thu nhat: "))
        canh_thu_hai = float(input("nhap canh thu hai: "))
        print("dien tich hinh chu nhat: ", _math.calculate_the_area_of_rectangle(canh_thu_nhat, canh_thu_hai))
    elif (canh == 3):
        canh_thu_nhat = float(input("nhap canh thu nhat: "))
        canh_thu_hai = float(input("nhap canh thu hai: "))
        canh_thu_ba = float(input("nhap canh thu ba: "))
        print("dien tich tam giac: ", _math.calculate_the_area_of_triangle(canh_thu_nhat, canh_thu_hai, canh_thu_ba))
    else:
        canh_thu_nhat = float(input("nhap canh thu nhat: "))
        canh_thu_hai = float(input("nhap canh thu hai: "))
        canh_thu_ba = float(input("nhap canh thu ba: "))
        canh_thu_tu = float(input("nhap canh thu tu: "))
        canh_thu_nam = float(input("nhap canh thu nam: "))
        print("dien tich ngu giac: ",
              _math.calculate_the_area_of_pentagon(canh_thu_nhat, canh_thu_hai, canh_thu_ba, canh_thu_tu, canh_thu_nam))
