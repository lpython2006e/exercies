# Write a program that prints the next 20 leap years (enter year or if not, get current year as default)


while 1:
    a = int(input("nhap vao nam: "))
    if(a%4==0 ):
        print("la nam nhuan. ")
        print("20 nam nhuan lien tiep: ")
        for x in range (a,a+80,4):
            print(x)
        break
    else:
        print("kp nam nhuan, vui long nhap lai: ")