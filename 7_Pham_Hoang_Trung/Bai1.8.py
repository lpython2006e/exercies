test_str = 'ABBAAACB'
A, B, C = 0, 0, 0
for i in test_str:
    if i == 'A':
        A +=1
    if i == "B":
        B += 1
    if i == "C":
        C += 1
print("A({}), B({}), C({})".format(A, B, C))



