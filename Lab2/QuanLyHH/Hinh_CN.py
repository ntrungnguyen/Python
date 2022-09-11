from Hinh_Hoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, canh: float, chieuRong: float) -> None:
        super().__init__(canh)
        self.__chieuDai = canh
        self.__chieuRong = chieuRong
        
    def __str__(self) -> str:
        return super().__str__() + f" Hình chữ nhật có chiều dài {self.__chieuDai}, chiều rộng {self.__chieuRong} Diện tích {self.dienTich}"
    
    @property
    def dienTich(self):
        return int(self.__chieuDai) * int(self.__chieuRong)