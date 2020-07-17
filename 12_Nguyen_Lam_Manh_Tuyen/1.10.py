#Make a program in Python, that solve quadratic equations
#A.x2 + B.x1 + C = 0
#Where A, B, C is real numbers (could be negative), find X.

import math
print("Quadratic equation: Ax\u00b2+Bx+C=0")
while True:
    try:
        a = float(input("please input value for A: "))
        if a==0:
            print("A can not be zero, please try again!")
            continue
    except ValueError:
        print("Your input is not a valid number")
    else:
        break
while True:
    try:
        b = float(input("please input value for B: "))
    except ValueError:
        print("Your input is not a valid number")
    else:
        break
while True:
    try:
        c = float(input("please input value for C: "))
    except ValueError:
        print("Your input is not a valid number")
    else:
        break
print("Quadratic equation {}x\u00b2+{}x+{}=0".format(a,b,c))
delta=(b**2)-(4*a*c)
if delta<0:
    print("The equation have no solution")
elif delta==0:
    root=-b/2*a
    print("The equation have double root: {:.2f}".format(root))
elif delta>0:
    root1=(-b+math.sqrt(delta))/(2*a)
    root2=(-b-math.sqrt(delta))/(2*a)
    print("The equation have the root 1 = {:.2f}".format(root1))
    print("The equation have the root 2 = {:.2f}".format(root2))
