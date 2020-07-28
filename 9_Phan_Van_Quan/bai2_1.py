#Write a function that returns the largest element in a list.
def large_element(list_1):
    large = list_1[0]
    for num in range(len(list_1)-1):
        if large > (list_1[num]):
            large = large
        else:
            large = (list_1[num])
    print("gia tri cuc dai cua list", large)

    # def largest_element(a):
    #     return max(a)
list_2 = [1,10,3,4,5,6,4,2,2,5,4,-3,2]
large_element(list_2)
