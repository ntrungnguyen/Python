from Hinh_Hoc import HinhHoc
from Hinh_CN import HinhChuNhat

class HinhVuong(HinhHoc):
    def __init__(self, canh: float) -> None:
        super().__init__(canh)   
        self.__canh = canh
        
    def __str__(self) -> str:
        return super().__str__() + f" Hình vuông cạnh {self.__canh} Diện tích {self.dienTich}"
    
    @property
    def dienTich(self):
        return int(self.__canh) * int(self.__canh)