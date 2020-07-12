# "Make a program in Python, that solve quadratic equations
# A.x2 + B.x1 + C = 0
# Where A, B, C is real numbers (could be negative), find X. "
import math

list_param = []
i = 1
while i <= 3:
    print('Type your number', i, ':')
    value = input()
    if i == 1 and float(value) == 0:
        print('Please retype your number', i, ', it must be greater than 0:')
    else:
        number = float(value)
        list_param.append(number)
        i += 1
print(list_param)
delta = (list_param[1] ** 2) - (4 * list_param[0] * list_param[2])
if delta < 0:
    result = 'The equation has no solution...'
elif delta == 0:
    result = 'x =' + str(-list_param[1] / (2 * list_param[0]))
else:
    result = 'x1 =' + str((-list_param[1] + math.sqrt(delta)) / (2 * list_param[0])) + '\nx2 =' + str((-list_param[1] - math.sqrt(delta)) / (2 * list_param[0]))

print(delta)
print(result)
