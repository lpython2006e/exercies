#Write a function that returns the elements on odd positions in a list
def odd_positions(lists):
    arr = []
    for i in range(1, len(lists), 2):
        arr.append(lists[i])
    return arr


lists = ['hihi', 1, 3, 'trung', 'hieu', 'lan']
print(odd_positions(lists))

