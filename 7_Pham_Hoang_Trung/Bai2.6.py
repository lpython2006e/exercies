def check_palindrome(strings):
    for i in range(int(len(strings)/2)):
        if strings[i] != strings[len(strings)-i-1]:
            return False
        return True

strings = input("Nhap vào chuoi: ")
if(check_palindrome(strings)):
    print("Chuoi doi xung")
else:
    print("khong la chuoi doi xung")


