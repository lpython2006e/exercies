# Write a function that checks whether an element occurs in a list.
test_list = [1, 6, 3, 5, 3, 4]

print("Kiểm tra items x có trong list không ( sử dụng loop ) : ")

for i in test_list:
    if (i == 4):
        print("True")

print("Kiểm tra items x có trong list không ( sử dụng In ) : ")

if (4 in test_list):
    print("True")
