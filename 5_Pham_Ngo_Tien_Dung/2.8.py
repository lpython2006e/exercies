# Write a function on_all that applies a function to every element of a list.
# Use it to print the first twenty perfect squares.
# The perfect squares can be found by multiplying each natural number with itself.
# The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16.
# Twelve for example is not a perfect square because there is no natural number m so that m*m=12.
# (This question is tricky if your programming language makes it difficult to pass functions as arguments.)

def checksohoanhao(a):
    for i in range(int(a)+1):
        if(i*i == a):
            return a

def nhap(n,a):
    for i in range(n):
        x = int(input("nhap phan tu thu " + str(i+1) + ": "))
        a.append(x)

def timsohoanhao(a):
    print("so hoan hao trong list:", end= " ")
    for i in a:
        if(checksohoanhao(i) == i):
            print(i,end="  ")

my_list=[]
n = int(input("nhap so phan tu: "))
nhap(n,my_list)
print("my_list = ",my_list)
timsohoanhao(my_list)