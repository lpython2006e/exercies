str=[]
digit=[]
print("Please input your string")
input=input()
for ele in input:
    if ele.isnumeric():
        digit.append(ele)
    else:
        str.append(ele)
str=sorted(str)
digit=sorted(digit)
result=str+digit
print("Your string after sorting is {}".format("".join(result)))
