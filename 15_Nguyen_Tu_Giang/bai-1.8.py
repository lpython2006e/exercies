# Generate the output like: A(5), B(3), C(1) with input like ABBAAACB

print('Write your string:')
value = input()
dic_str = {}
list_count = []
count = 0
for i in value:
    dic_str.update({i: ''})
# print(dic_str)
for x in dic_str:
    result = "{}({})"
    print(result.format(x, value.count(x)))
# print(dic_str)




