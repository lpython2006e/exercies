# exercise 1
def max_array(array):
    return max(array)

# exercise 2
def reverse_array(array):
    result=[]
    for i in range(len(array)-1,-1,-1):
        result.append(array[i])
    return result

# exercise 3
def check(array,char):
    if char in array:
        return 'yes'
    else:
        return 'dont find'

# exercise 4
def phan_tu_le(array):
    result=[]
    for i in range(1,len(array),2):
        result.append(array[i])
    return result
# exercise 5:
def sum(array):
    tong=0
    for i in range(len(array)):
        tong+=array[i]
    return tong

#excercise 6
def check_symmetry(str):
    for i in range(int(len(str)/2)+1):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True

# exercise 7
# use for loop
def sum1(array):
    tong=0
    for i in range(len(array)):
        tong+=array[i]
    return tong

# use while loop
def sum2(array):
    tong=0
    i=0
    while i<len(array):
        tong+=array[i]
        i+=1
    return tong

# use recursion
def cal_sum(array):
    if len(array)==1:
        return array[0]
    else:
        return array[0]+cal_sum(array[1:])

# exercise 8
import math
def square(array):
    result=[]
    for i in array:
        if pow(int(math.sqrt(i)),2)==i:
            result.append(i)
    return result


# excercise 9
def conCat(array1,array2):
    return array1+array2




