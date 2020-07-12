# Write a program that prints the next 20 leap years (enter year or if not, get current year as default)


while 1:
    namnhap = int(input("nhap vao nam: "))
    # Note: bai nay van xu ly thieu truong hop ko nhap -> lay nam hien tai
    ketqua = set()
    if (namnhap % 4 == 0 and namnhap % 100 != 0):
        ketqua.add(namnhap)
        while (len(ketqua) <= 20):
            namnhap += 4
            if (namnhap % 100 != 0):
                ketqua.add(namnhap)
    else:
        for i in range(6):
            namnhap += 1
            if (namnhap % 4 == 0 and namnhap % 100 != 0):
                ketqua.add(namnhap)
                break
        while (len(ketqua) <= 20):
            namnhap += 4
            if (namnhap % 100 != 0):
                ketqua.add(namnhap)
    print("Ket qua 20 nam nhuan: " + str(sorted(ketqua)))
