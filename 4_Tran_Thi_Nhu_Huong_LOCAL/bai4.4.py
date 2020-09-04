"""Create a “LunarCalendarUtils” class that have ability to convert from Gregorian calendar to Lunar Calendar"""


class LunaConvert:
    def __init__(self):
        pass

    def chuyendoi(self,nam):
        danh_sach_can = ["Quy","Giap","At","Binh","Dinh","Mau","Ky","Canh","Tan","Nham"]
        danh_sach_chi =["Hoi","Ty","Suu","Dan","Mao","Thin","Ty","Ngo","Mui","Than","Dau","Tuat"]
        temp = int(nam) - 3
        vi_tri_can = temp % 10
        vi_tri_chi = temp % 12
        can = danh_sach_can[vi_tri_can]
        chi = danh_sach_chi[vi_tri_chi]
        nam_am_lich = can + " " + chi
        return nam_am_lich

    def in_name_am_lich(self,a):
        print("Nam Am Lich la : {}".format(a))

chuyendoinam = LunaConvert()
namduonglich = input("Nhap nam duong lich: ")
al= chuyendoinam.chuyendoi(namduonglich)
chuyendoinam.in_name_am_lich(al)




