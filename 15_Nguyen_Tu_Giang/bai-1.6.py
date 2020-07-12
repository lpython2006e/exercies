# Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

secret_number = 15
value = ''
# count = 0
set_number = {''}
while value != secret_number:
    print('What is your secret number?')
    value = int(input())
    set_number.add(value)
    if value == secret_number:
        print('Awesome! You right! You tried', len(set_number) - 1, 'times.')
    elif value < secret_number:
        print('Your number is smaller the secret number.')
    else:
        print('Your number is greater the secret number.')
    # count += 1
