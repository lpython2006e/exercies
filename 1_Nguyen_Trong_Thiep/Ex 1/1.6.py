# Write a guessing game where the user has to guess a secret number. After every guess the program tells the user
# whether their number was too large or too small. At the end the number of tries needed should be printed. It counts
# only as one try if they input the same number multiple times consecutively


import random

rand = random.randint(1, 10)
history = []

while True:
    n = input("Nhap vao so n trong khoang 1 den 10: ")
    while not n.isdigit():
        print("Your input is not a number, please try again")
        n = input()
    n = int(n)
    if n < rand:
        print("So ban nhap qua nho")
        if n not in history:
            history.append(n)
    if n > rand:
        print("So ban nhap qua lon")
        if n not in history:
            history.append(n)
    if n == rand:
        print("Ban da doan dung")
        history.append(n)
        break
print("Cac so ban da doan", history)
