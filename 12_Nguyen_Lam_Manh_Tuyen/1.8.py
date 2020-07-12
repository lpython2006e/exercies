print("Please input your string")
input=input()
for ele in list(set(input)):
    print(ele+"["+str(input.count(ele))+"]")