#Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.
import random
lov=[]
secretnum=random.randrange(1,100)
print(secretnum)
guess=()
print("Please input your guess")
while guess!=secretnum:
    guess = input()
    while guess.isdigit() == False:
        print("Your input is not a valid number, please try again")
        guess = input()
    if int(guess)<secretnum:
        print("Your input number is lower than the secret number, try higher")
        print("Please input your guess again")
        lov.append(guess)
    if int(guess)>secretnum:
        print("Your input number is higher than the secret number, try lower")
        print("Please input your guess again")
        lov.append(guess)
    if int(guess)==secretnum:
        #count times user have tried to input
        lov=list(set(lov))
        count=len(lov)+1
        print("Bingo, You've guessed it correcly in {} times".format(count))

