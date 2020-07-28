#Write a program that prints the next 20 leap years (enter year or if not, get current year as default)
current_year = 2020
year = eval(input("Nhap vao nam ban chon "))
# in ra nam nhuan dau tien
for num in range(8):
    if year % 4 == 0 and year % 100 != 0:
        nam_nhuan_dau_tien = year
    year = year +1

print("Nam nhuan dau tien ", nam_nhuan_dau_tien)

nam_nhuan = [nam_nhuan_dau_tien]

for num2 in range(20):
    nam_nhuan_dau_tien = nam_nhuan_dau_tien + 4
    if nam_nhuan_dau_tien % 4 == 0 and nam_nhuan_dau_tien % 100 != 0:
        nam_nhuan.append(nam_nhuan_dau_tien)
print(nam_nhuan)