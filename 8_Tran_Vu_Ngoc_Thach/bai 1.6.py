"""Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively."""
import    random
a= random.randrange(1,9)
print("hint = " + str(a))
print("please input the number")
number = input("input your number")
k=0

while int(number) != a:
    if int(number) < a:
        number = input("your number is lower, please input new one")
        k+=1
    else:
        number = input("your number is higher, please input new one")
        k+=1

string = "Congratulation, you input right number. The total input are {}"
print(string.format(k))