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

