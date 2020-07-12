# Order the input string by ASC (a -> z, 0 -> 9) with any string
import re

list_str = []
print('Write your the text:')
value = input()


def arrange_str():
    filter_value = re.findall('\w', value)
    for i in filter_value:
        # print(i)
        list_str.append(i)
        list_str.sort()
        result = "".join(list_str)
    return result


print(arrange_str())
