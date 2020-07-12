start=1
print("Please input your number")
end=input()
sum=0
while end.isdigit()==False:
    print("Your input is not a valid number, please try again")
    end=input()
for i in range(start,int(end)+1):
    sum=sum+i
print("Sum from 1 to {} is {}".format(end,sum))