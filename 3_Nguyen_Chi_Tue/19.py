a=[]
i=2020
while 1:
    if i%4==0 and i%100!=0:
        a.append(i)
    if len(a)==20:
        break
    i+=1
print(a)