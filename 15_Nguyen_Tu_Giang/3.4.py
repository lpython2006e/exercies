# Update previous one, allow to enter multiple classmate, at end, allow to save to file as CSV format
import csv

print('Type path your file:')
path_file = input()
print('How many people in list:')
num = int(input())
i = 0

with open(path_file, mode='a') as csv_file:
    fieldnames = ['Name', 'Birthday', 'Email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    while i < num:
        print('Type your classmate\'s name:')
        name = input()
        print('Type your classmate\'s birthday:')
        birthday = input()
        print('Type your classmate\'s email:')
        email = input()


        def valid_length(name_field, field, length):
            if len(field) <= length:
                print('Retype your classmate\'s', name_field, 'it has must least', length, 'character:')
                field = input()


        valid_length('name', name, 2)
        valid_length('birthday', birthday, 7)
        valid_length('email', email, 8)
        writer.writerow({'Name': name, 'Birthday': birthday, 'Email': email})
        i += 1
        # writer.writerow({'Name': 'Huong', 'Birthday': '14/11/1990', 'Email': 'huong@gmail.com'})
