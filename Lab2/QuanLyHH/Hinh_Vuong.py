from Hinh_CN import HinhChuNhat

class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float) -> None:
        super().__init__(canh, canh)
        
    def __str__(self) -> str:
        return f"\nHình vuông cạnh {self.canh} Diện tích {self.dienTich()}"
        
