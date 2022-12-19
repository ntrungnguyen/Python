from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiChinhQuy

class DanhSachSinhVien:
    def __init__(self) -> None:
        self.dssv = []
        
    def themSv(self, sv: SinhVien):
        self.dssv.append(sv)
        
    def xuat(self):
        stt = 0
        for sv in self.dssv:
            stt += 1
            print(f"[{stt}]", sv)
            
    def timSvTheoMaSo(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms: 
                return i
        else:
            return -1
        
    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy".lower() or loai == "chinh quy".lower():
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy)]
    
    def diemRL(self, diem: int):
        return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv._diemRL >= diem]
    
    def xoaSvTheoMaSo(self, ms: str) -> bool:
        vt = self.timSvTheoMaSo(ms)
        if vt != -1:
            del self.dssv[vt]
            return True
        return False