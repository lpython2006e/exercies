
def checkleadyear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 ==0

now = 2020
arraylead = []
dem = 0
for year in range(now,3000):
    if(checkleadyear(year)):
        arraylead[dem] = year
        dem = dem + 1
    if (dem == 40):
        print(arraylead)
        break

