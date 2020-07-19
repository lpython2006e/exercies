# Write a program that allow user to enter classmate (name, Birthday, Email), validate if enter values are valid format (limit length apply), else ask user to enter again per field
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

