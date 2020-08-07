#Write a function that computes the running total of a list. sum
def sum_list(list_1):
    tong = 0
    for num in range(len(list_1)):
        tong = tong + list_1[num]
    print(tong)
list_2 = [1,2,3,4,5,2,23,2,4,32,42,324,324]
sum_list(list_2)