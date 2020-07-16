# Write a function that checks whether an element occurs in a list.
def check_in(ele, list_ele):
    if list_ele.count(ele):
        return True
    else:
        return False


print(check_in(2, ['apple', 'cherry', 'banana']))
