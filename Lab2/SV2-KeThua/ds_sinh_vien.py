from datetime import datetime
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from sinh_vien import SinhVien

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
        
    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)
        
    def xuat(self):
        for sv in self.dssv:
            print(sv)
            
    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == ms:
                return i
        else:
            return -1
        
    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy)]
    
    def diemRL(self, diem: int):
        return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv.diemRL >= diem]
    
    def trinhDoCaoDangSinhTruocNgay(self, ngay, trinhDo: str):
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy) and sv.ngaySinh < datetime.strptime(ngay, "%d/%m/%Y") and sv.trinhDo.upper() == trinhDo.upper()]
    
    #Làm thêm
    #Tìm vt sv, nếu có trả về vt sinh viên trong danh sách
    def timVtSvTheoMs(self, mssv: int) -> int:
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    #Xóa sv theo mã số, cho biết xóa được hay không
    def xoaSvTheoMs(self, maSo: int) -> bool:
        vt = self.timVtSvTheoMs(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    