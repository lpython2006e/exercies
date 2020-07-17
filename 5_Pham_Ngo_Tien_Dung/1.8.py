# Generate the output like: A(4), B(3), C(1) with input like ABBAAACB

a = input("nhap vao chuoi: ")
n = set(a)
for x in n:
    txt = str(x) + "(" + str(a.count(x)) + ")"
    print(txt)
