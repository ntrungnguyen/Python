from datetime import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo
        self._hoTen = hoTen
        self._ngaySinh = ngaySinh
        
    
    @staticmethod
    def ktMsHopLe(mssv: int):
        return len(str(mssv)) == 7
    @property
    def maSo(self):
        return self._maSo
    @maSo.setter
    def maSo(self, maSo: int):
        if self.ktMsHopLe(maSo):
            self._maSo = maSo
    
        
    @property
    def hoTen(self):
        return self._hoTen
    @hoTen.setter
    def hoTen(self, hoTen: str):
        self._hoTen = hoTen
        
    
    @property
    def ngaySinh(self):
        return self._ngaySinh
    @ngaySinh.setter
    def ngaySinh(self, ngaySinh: str):
        self._ngaySinh = ngaySinh
        
        
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"