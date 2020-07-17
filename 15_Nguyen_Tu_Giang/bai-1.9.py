# Write a program that prints the next 20 leap years (enter year or if not, get current year as default)

print('Type your year that you want to check:')
value = int(input())
count = 1
i = 0


def leap_years(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


while count <= 20:
    if not leap_years(value):
        if leap_years(value + i):
            print(value + i)
            count += 1
        i += 1
    else:
        if leap_years(value + i):
            print(value + i)
            count += 1
        i += 4


# print(leap_years(value))
