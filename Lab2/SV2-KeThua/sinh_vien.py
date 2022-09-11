from datetime import datetime


class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        #Khai báo kiểu truy xuất là protected
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh
        
    @property
    def hoTen(self):
        return self.__hoTen
    @hoTen.setter
    def hoTen(self, hoTen: str):
        self.__hoTen = hoTen
        
    @property
    def mssv(self):
        return self.__maSo
    @mssv.setter
    def mssv(self, ms: int):
        if self.ktMsHopLe(ms):
            self.__maSo = ms
            
    @property
    def ngaySinh(self):
        return self.__ngaySinh
    @ngaySinh.setter
    def hoTen(self, ngaySinh: str):
        self.__ngaySinh = ngaySinh
        
    @staticmethod
    def ktMsHopLe(mssv: int):
        return len(str(mssv)) == 7
    
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"