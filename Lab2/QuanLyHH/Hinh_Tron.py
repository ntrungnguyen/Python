from Hinh_Hoc import HinhHoc
from math import pi

class HinhTron(HinhHoc):
    def __init__(self, canh: float) -> None:
        super().__init__(canh)
        self._banKinh = canh
        
    def __str__(self) -> str:
        return super().__str__() + f" Hình tròn có bán kính {self._banKinh} Diện tích {self.dienTich()}"
    
    def dienTich(self):
        return float(round(pi * pow(int(self._banKinh), 2), 2))