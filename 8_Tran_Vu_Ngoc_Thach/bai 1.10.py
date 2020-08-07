"""Make a program in Python, that solve quadratic equations
A.x2 + B.x1 + C = 0
Where A, B, C is real numbers (could be negative), find X. """
import   math
a = float (input("Input a: "))
b = float (input("Input b: "))
c = float (input("Input c: "))

if (a==0):
    if (b==0):
        print("Phuong trinh vo nghiem ")
    else:
        x = -c/b
        print ("phuong trinh co 1 nghiem: x= " +str(x))
else:
    if (b==0):
        x = sqrt(-c/b)
    else:
        delta = b*b - 4*a*c
        if delta >0:
            x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
            x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
            print("Phuong trinh co 2 nghiem: x1 = ", x1, " và x2 = ", x2)
        elif delta==0:
            x1 = (-b / (2 * a))
            print("phuong trinh co nghiem kep: x1 = x2 = ", x1)
        else:
            print("vo nghiem")




