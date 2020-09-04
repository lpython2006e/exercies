"""Create a “MathUtils” class that have ability to solve
Sum of range input
solve quadratic equations
Calculate the area of 4 type of shape (circle, rectangle, triangle, Pentagon)"""


class Math:
    def __init__(self, ban_kinh = None, canh_thu_nhat = None, canh_thu_hai = None):
        self.ban_kinh = ban_kinh
        self.canh_thu_nhat = canh_thu_nhat
        self.canh_thu_hai = canh_thu_hai

    def lay_canh_thu_nhat(self,canh_thu_nhat):
        self.canh_thu_nhat = int(canh_thu_nhat)

    def lay_canh_thu_hai(self,canh_thu_hai):
        self.canh_thu_hai = int(canh_thu_hai)

    def lay_ban_kinh(self,ban_kinh):
        self.ban_kinh = int(ban_kinh)

    def tinh_dien_tich(self,dai,rong):
        dientich = int(dai) * int(rong)
        return dientich

    def tinh_dien_tinh_hinh_tron(self,ban_kinh):
        dien_tich_tron = int(ban_kinh)*int(ban_kinh)*3.14
        return dien_tich_tron

    def in_dien_tich(self,dientich):
        print ("Dien tich la: ",dientich)

tinh_dien_tich_tam_giac = Math()
dai= input("Nhap canh thu nhat: ")
tinh_dien_tich_tam_giac.lay_canh_thu_nhat(dai)
rong = input("Nhap canh thu hai: ")
tinh_dien_tich_tam_giac.lay_canh_thu_hai(rong)
dien_tich = tinh_dien_tich_tam_giac.tinh_dien_tich(tinh_dien_tich_tam_giac.canh_thu_nhat,tinh_dien_tich_tam_giac.canh_thu_hai)
tinh_dien_tich_tam_giac.in_dien_tich(dien_tich)


tinh_dien_tich_tron = Math()
ban_kinh = input("Nhap ban kinh: ")
tinh_dien_tich_tron.lay_ban_kinh(ban_kinh)
dien_tich_tron = tinh_dien_tich_tron.tinh_dien_tinh_hinh_tron(tinh_dien_tich_tron.ban_kinh)
tinh_dien_tich_tron.in_dien_tich(dien_tich_tron)