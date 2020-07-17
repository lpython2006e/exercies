index = eval(input("Gia tri n nhap vao "))
print("Vay ban can tinh tong tu 1 den ", index)
sum = 0
for num in range(1, index):
    sum = num + sum
print(sum)