def total(lists):
    array = []
    sum = 0
    for i in lists:
        sum += i
        array.append(sum)
    return array


listss = [1,2,3,5,5,4]
print(total(listss))


