"""Generate the output like: A(5), B(3), C(1) with input like ABBAAACB"""

print("please input the number")
string = input("input your string")
bracket_1 = "("
bracket_2 = ")"
underscore = ", "
the_len = len(string)
if the_len == 1:
    print(string[0] + bracket_1 + str(0) + bracket_2)
else:
    for i in range(len(string)):
        if i ==(len(string)-1):
            print(string[i] + bracket_1 + str(i) +bracket_2)
        else:
            print(string[i] + bracket_1 + str(i)+ bracket_2 + underscore, end=' ')


