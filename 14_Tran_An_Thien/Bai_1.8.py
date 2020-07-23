# Generate the output like: A(5), B(3), C(1) with input like ABBAAACB
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
check_string = "ABBAAACB"

for char in chars:
    count = check_string.count(char)
    if count >= 1:
        print(char, count)
