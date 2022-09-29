from Hinh_Hoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, canh: float, chieuRong: float) -> None:
        super().__init__(canh)
        self._chieuRong = chieuRong
        
    def __str__(self) -> str:
        return super().__str__() + f"Hình chữ nhật có chiều dài {self.canh}, chiều rộng {self._chieuRong} Diện tích {self.dienTich()}"
    
    def dienTich(self):
        return float(self.canh) * float(self._chieuRong)