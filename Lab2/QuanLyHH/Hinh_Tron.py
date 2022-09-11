from Hinh_Hoc import HinhHoc
from math import pi

class HinhTron(HinhHoc):
    def __init__(self, canh: float) -> None:
        super().__init__(canh)
        self.__banKinh = canh
        
    def __str__(self) -> str:
        return super().__str__() + f" Hình tròn có bán kính {self.__banKinh} Diện tích {self.dienTich}"
    
    @property
    def dienTich(self):
        return round(pi * pow(int(self.__banKinh), 2), 2)