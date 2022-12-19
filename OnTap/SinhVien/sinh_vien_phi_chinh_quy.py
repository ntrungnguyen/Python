from sinh_vien import SinhVien
from datetime import datetime

class SinhVienPhiChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhDo: str, tgdt: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self._trinhDo = trinhDo
        self._tgdt = tgdt
        
    def __str__(self) -> str:
        return super().__str__() + f"\t{self._trinhDo}\t{self._tgdt}"