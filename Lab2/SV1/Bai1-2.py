
#Bài 1: Cài đặt lớp Sinh viên và danh sách sinh viên như sau và hoàn thành các hàm còn trống (chưa có nội dung)
from datetime import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo #private
        self.__hoTen = hoTen #private
        self.__ngaySinh = ngaySinh #private

    #cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSo
    @property
    def maSo(self):
        return self.__maSo

    @property
    def hoTen(self):
        return self.__hoTen
    
    @property
    def ngaySinh(self):
        return self.__ngaySinh

    #cho phép thay đổi thuộc tính 
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    # @hoTen.setter
    # def hoTen(self, hoTen):
    #     self.__hoTen = hoTen
    
    #phương thức tĩnh: các pt không truy xuất được đến thuộc tính, hành vi của lớp
    # những pt này không cần truyền tham số mặc định self
    # đây không phải là 1 hành vi (pt) của 1 đối tượng thuộc lớp
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    #pt của lớp, chỉ truy xuất đến các biến thành viên của lớp
    # không truy xuất được các thuộc tính riêng của đối tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    #hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}.rjust(15)\t{self.__ngaySinh}.rjust(15)")

    #tương tự phương thức ghi đè toString
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"

    
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        print("\nDanh sách sinh viên:")
        print("MSSV", "Họ và tên".rjust(15), "Ngày sinh".rjust(20), "\n===================================================")
        for sv in self.dssv:
            print(sv.maSo, sv.hoTen.rjust(15), "".ljust(7),sv.ngaySinh)

    #Tìm sv theo mssv, nếu có trả về sv
    def timSvTheoMssv(self, mssv: int) -> list:
        #return [ sv for sv in self.dssv if sv.maSo == mssv ]
        kq = []
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                kq.append(self.dssv[i])
        return kq

    #Tìm vt sinh viên theo mssv
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1

    #xóa sv có mssv, thông báo xóa được hoặc không
    def xoaSvTheoMssv(self, mssv: int) -> bool:
        vt = self.timVTSvTheoMssv(mssv)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    #Tìm sv tên 
    def timSvTheoTen(self, tentim: str) -> list:
        #return [ sv for sv in self.dssv if sv.__hoTen.split(' ')[-1].lower() == tentim.lower()]
        
        kq = []
        for i in range(len(self.dssv)):
            if self.dssv[i].hoTen.split(' ')[-1].lower() == tentim.lower():
                kq.append(self.dssv[i])
        return kq
        

    #Tìm sv sinh trước ngày 15/06/2000
    def timSvSinhTruocNgay(self, ngay):
        return [sv for sv in self.dssv if sv.ngaySinh < datetime.strptime(ngay, "%d/%m/%Y") ]
    
    #Đọc file txt
    def DocFile(self):
        try:
            f = open("file.txt", "r", encoding="utf-8")
            #print(f.read())
            for x in f:
                maSo = x.split(',')[0]
                hoTen = x.split(',')[1].rjust(15)
                ngaySinh = datetime.strptime(x.split(',')[2].strip(), "%d/%m/%Y")
                svFile = SinhVien(maSo, hoTen,ngaySinh)
                dssv.themSinhVien(svFile)
            print("Đọc file thành công. Đã thêm vào danh sách sinh viên")
        except:
            print("Lỗi đọc file. Có thể không có file")
            
    def sapTangTheoTen(self):
        self.dssv.sort(key=lambda x: x.hoTen, reverse=False)
    def sapGiamTheoTen(self):
        self.dssv.sort(key=lambda x: x.hoTen, reverse=True)

sv1 = SinhVien(1911111, "Nguyễn Văn O", datetime.strptime("1/1/2001", "%d/%m/%Y"))
sv2 = SinhVien(1922222, "Nguyễn Văn M", datetime.strptime("1/1/2001", "%d/%m/%Y"))
sv3 = SinhVien(1933333, "Nguyễn Văn N", datetime.strptime("1/1/2002", "%d/%m/%Y"))

dssv = DanhSachSv()
dssv.themSinhVien(sv1)
dssv.themSinhVien(sv2)
dssv.themSinhVien(sv3)

dssv.DocFile()

dssv.xuat()

mssv = 1911111
print(f"\nSinh viên có mã số {mssv}")
kqmssv = dssv.timSvTheoMssv(mssv)
for tmp in kqmssv:
    print(tmp)

vt = dssv.timVTSvTheoMssv(mssv)
if vt != -1:
    print(f"\nSinh viên có mã số {mssv} nằm ở vị trí thứ {vt + 1} trong danh sách")
else:
    print(f"\nSinh viên có mã số {mssv} không nằm trong danh sách")

if dssv.xoaSvTheoMssv(mssv):
    print(f"\nĐã xóa sinh viên có mã số {mssv} trong danh sách")
else:
    print(f"\nKhông xóa được vì mâ số sinh viên {mssv} không có trong danh sách")


tentim = "A"
print(f"\nDanh sách viên có tên {tentim}:")
kqten = dssv.timSvTheoTen(tentim)
for tmp in kqten:
    print(tmp)

ngaytim = "15/06/2000"
print(f"\nDanh sách sinh viên sinh trước ngày {ngaytim}")
kq = dssv.timSvSinhTruocNgay(ngaytim)
for tmp in kq:
    print(tmp)


dssv.xuat()

dssv.sapTangTheoTen()
print("\nDanh sách sinh viên sau khi sắp xếp tăng theo họ tên")
dssv.xuat()

dssv.sapGiamTheoTen()
print("\nDanh sách sinh viên sau khi sắp xếp giảm theo họ tên")
dssv.xuat()

