from Phan_So import PhanSo

class DSPhanSo:
    def __init__(self) -> None:
        self.dsPhanSo = []
        
    def xuat(self):
        print("\nDanh sách phân số")
        count = -1
        print("STT".ljust(5),"Phân số")
        for ps in self.dsPhanSo:
            count += 1
            print(f"{[count]}".ljust(5), f"{ps}")
        
    def themPS(self, ps:PhanSo):
        ps.rutGon()
        self.dsPhanSo.append(ps)
        
    def phanSoDuong(self):
        return [ps for ps in self.dsPhanSo if ps.tu * ps.mau > 0]
    
    def phanSoAm(self):
        return [ps for ps in self.dsPhanSo if ps.tu * ps.mau < 0]
    
    def demPSAm(self):
        dem = 0
        for ps in self.dsPhanSo:
            if ps.tu < 0 or ps.mau < 0:
                dem += 1
        return dem
    
    def soSanhPS(self, a: PhanSo, b:PhanSo):
        if a.mau == b.mau:
            return a.tu < b.tu
        else:
            return a.tu * b.mau < b.tu * a.mau
        
    def psDuongMin(self):
        for ps in self.dsPhanSo:
            if ps.tu > 0 and ps.mau > 0:
                min = ps
                break
        
        for ps in self.dsPhanSo:
            if ps.tu > 0 and ps.mau > 0:
                if (dsps.soSanhPS(ps, min)):
                    min = ps
        return min
    
    def SoSanh(self, a: PhanSo, b: PhanSo):
        if (a.tu == b.tu and a.mau == b.mau):
            return True
        return False
    
    def timAllVT(self, a: PhanSo):
        return [p for p in range(0, len(self.dsPhanSo)) if self.SoSanh(self.dsPhanSo[p], a)]
    
    def sumPsAm(self):
        sum = PhanSo()
        for ps in self.phanSoAm():
            sum.__multiadd__(ps)
        return sum
    
    def timVTPS(self, a: PhanSo) -> int:
        for i in range(len(self.dsPhanSo)):
            if self.dsPhanSo[i] == a:
                return i
        return -1
        
    def xoaPS(self, a: PhanSo) -> bool:
        vt = self.timVTPS(a)
        if vt != -1:
            del self.dsPhanSo[vt]
            return True
        else:
            return False
          
    def xoaPSCoTuLaX(self, tu: int):
        for ps in self.dsPhanSo:
            if ps.tu == tu:
                self.xoaPS(ps)
                
    def sapTangMau(self):
        self.dsPhanSo.sort(key=lambda x: x.mau, reverse=False)
        dsps.xuat()
        
    def sapGiamMau(self):
        self.dsPhanSo.sort(key=lambda x: x.mau, reverse=True)
        dsps.xuat()
        
    def sapTangTu(self):
        self.dsPhanSo.sort(key=lambda x: x.tu, reverse=False)
        dsps.xuat()
        
    def sapGiamTu(self):
        self.dsPhanSo.sort(key=lambda x: x.tu, reverse=True)
        dsps.xuat()

dsps = DSPhanSo()

a = PhanSo()
a.tu = 8
a.mau = 6

b = PhanSo()
b.tu = 5
b.mau = 4

c = PhanSo()
c.tu = -5
c.mau = 2
d = PhanSo()
d.tu = -2
d.mau = 3

e = PhanSo()
e.tu = -8
e.mau = 3

f = PhanSo()
f.tu = 4
f.mau = 3

dsps.themPS(a)
dsps.themPS(b)
dsps.themPS(c)
dsps.themPS(d)
dsps.themPS(e)
dsps.themPS(f)

dsps.xuat()

print("\nDanh sách số dương")
tmp = dsps.phanSoDuong()
for x in tmp:
    print(x)
    
print("\nDanh sách số âm")
tmp = dsps.phanSoAm()
for x in tmp:
    print(x)


print("\nSố phân số âm trong mảng là:", dsps.demPSAm())

print(f"\nTổng tất cả các phân số âm trong mảng là: {dsps.sumPsAm()}")

psmin = dsps.psDuongMin()
print(f"\nPhân số dương nhỏ nhất là: {psmin}")

pstim = PhanSo()
pstim.tu = 4
pstim.mau = 3
print(f"\nTất cả vị trí của phân số {pstim} là: {dsps.timAllVT(pstim)}")


if dsps.xoaPS(pstim):
    print(f"\nĐã xóa phân số {pstim} trong danh sách")
else:
    print(f"\nKhông xóa được vì phân số {pstim} không tồn tại trong danh sách")
dsps.xuat()

tuXoa = -8    
dsps.xoaPSCoTuLaX(tuXoa)
print(f"\nDanh sách phân số sau khi xóa phân số có tử là {tuXoa}")
dsps.xuat()

print("\nSắp xếp mẫu tăng")
dsps.sapTangMau()

print("\nSắp xếp tử tăng")
dsps.sapTangTu()

print("\nSắp xếp mẫu giảm")
dsps.sapGiamMau()

print("\nSắp xếp tử giảm")
dsps.sapGiamTu()
