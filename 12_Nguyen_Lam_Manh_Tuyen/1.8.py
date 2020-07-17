#Generate the output like: A(5), B(3), C(1) with input like ABBAAACB
print("Please input your string")
input=input()
for ele in list(set(input)):
    print(ele+"["+str(input.count(ele))+"]")