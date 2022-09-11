from sinh_vien import SinhVien
from datetime import datetime

class SinhVienPhiChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhDo: str, tgdt: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.trinhDo = trinhDo
        self.tgdt = tgdt
        
    def __str__(self) -> str:
        return super().__str__() + f"{self.trinhDo}\t{self.tgdt}"
 