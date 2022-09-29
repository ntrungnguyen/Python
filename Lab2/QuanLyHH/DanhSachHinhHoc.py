import sys
from unittest import result
from Hinh_Hoc import HinhHoc
from Hinh_CN import HinhChuNhat
from Hinh_Vuong import HinhVuong
from Hinh_Tron import HinhTron
from loaiHinh import LoaiHinh

class DanhSachHH:
    def __init__(self) -> None:
        self.dshh = []
        
    def themHinh(self, hh: HinhHoc):
        self.dshh.append(hh)
        
    def xuat(self):
        for hh in self.dshh:
            print(hh)
            
    def docFile(self):
        try:
            f = open("hinhhoc.txt", 'r', encoding="utf-8")
            lines = f.readlines()
            for line in lines:
                sp = line.split(",")
                if(sp[0] == "HinhVuong"):
                    hv = HinhVuong(sp[1])
                    self.themHinh(hv)
                elif(sp[0] == "HinhChuNhat"):
                    hcn = HinhChuNhat(sp[1], sp[2])
                    self.themHinh(hcn)
                elif(sp[0] == "HinhTron"):
                    ht = HinhTron(float(sp[1]))
                    self.themHinh(ht)
            print("Đọc file thành công. Đã thêm vào danh sách hình học")
        except:
            print("Lỗi đọc file. Có thể không có file")
            
    def timHinhCoDienTichLonNhat(self):
        max = 0
        result = HinhHoc(0)
        for hh in self.dshh:
            if hh.dienTich() > max:
                max = hh.dienTich()
                result = hh
        return print(result)
    
    def timHinhCoDienTichNhoNhat(self):
        min = sys.maxsize
        result = HinhHoc(0)
        for hh in self.dshh:
            if hh.dienTich() < min:
                min = hh.dienTich()
                result = hh
        return print(result)
    
    def timHinhCoDienTichLonNhatTheoLoai(self, loaiHinh: str):
        max = 0
        result = HinhHoc(0)
        if(loaiHinh == "HinhTron"):
            for hh in self.dshh:
                if hh.dienTich() > max and isinstance(hh, HinhTron):
                    max = hh.dienTich()
                    result = hh
        elif(loaiHinh == "HinhChuNhat"):
            for hh in self.dshh:
                if hh.dienTich() > max and isinstance(hh, HinhChuNhat):
                    max = hh.dienTich()
                    result = hh
        elif(loaiHinh == "HinhVuong"):
            for hh in self.dshh:
                if hh.dienTich() > max and isinstance(hh, HinhVuong):
                    max = hh.dienTich()
                    result = hh
        return print(result)
    
    def sapGiamTheoS(self):
        return self.dshh.sort(key = lambda x: x.dienTich(), reverse=True)
    
    def demSoLuongHinhTheoLoai(self, loai: str):
        result = []
        if loai == "HinhTron":
            result = [hh for hh in self.dshh if isinstance(hh, HinhTron)]
        elif loai == "HinhChuNhat":
            result = [hh for hh in self.dshh if isinstance(hh, HinhChuNhat)]
        elif loai == "HinhVuong":
            result = [hh for hh in self.dshh if isinstance(hh, HinhVuong)]
        return f"\nCó {len(result)} {loai}"
    
    def tinhTongS(self):
        sum = 0
        for hh in self.dshh:
            sum += hh.dienTich()
        return f"\nTổng diện tích của các hình là {round(sum,2)}"
    
    def timVtCuaHinh(self, h: HinhHoc):
        pass
            
    def timHinhTheoS(self, s:float):
        return [hh for hh in self.dshh if hh.dienTich() == s]
    
    def xoa(self, hh: HinhHoc):
        self.dshh.remove(hh)
    
# dshh = DanhSachHH()
# dshh.docFile()
# dshh.xuat()

# print("\nHình có diện tích lớn nhất là")
# dshh.timHinhCoDienTichLonNhat()

# print("\nTìm S max theo loại")
# dshh.timHinhCoDienTichLonNhatTheoLoai("HinhTron")

# print("\nHình có diện tích nhỏ nhất là")
# dshh.timHinhCoDienTichNhoNhat()

# print("\nDanh sách sắp giảm diện tích")
# dshh.sapGiamTheoS()
# dshh.xuat()

# print(dshh.demSoLuongHinhTheoLoai("HinhVuong"))

# print(dshh.tinhTongS())

# timTheoS = dshh.timHinhTheoS(12)
# print("\nDanh sách hình học có diện tích bằng 12")
# for tmp in timTheoS:
#     print(tmp)