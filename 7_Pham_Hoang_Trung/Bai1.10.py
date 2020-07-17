import math
#Nhap cac so A, B, C
a = float(input("Nhap so a ="))
b = float(input("Nhap so b = "))
c = float(input("Nhap so c = "))

if(a==0):
    if(b==0):
        if (c==0):
            print("Moi x la nghiem")
        else:
            print("Vo nghiem")
    else:
        print("Phuong trinh co nghiem don: {} ".format(-c/b))

else:
    delta =  b**2 - 4*a*c
    if(delta<0):
        print("Phuong trinh vo nghiem")
    else:
        if(delta==0):
            print("Phuong trinh nghiem kep: {}".format(-b/(2*a)))
        else:
            print("Phuong trinh co 2 nghiem phan biet\n");
            print("x1 ={}".format((-b - math.sqrt(delta)) / (2 * a)))
            print("x2 ={}".format((-b + math.sqrt(delta)) / (2 * a)))

