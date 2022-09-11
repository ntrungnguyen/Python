import math

class PhanSo:
    def __init__(self):
        self.__tu = 0
        self.__mau = 1
        self.rutGon()
        
    @property
    def tu(self):
        return self.__tu
    @tu.setter
    def tu(self, Tu):
        self.__tu = Tu
        
    @property
    def mau(self):
        return self.__mau
    
    @staticmethod
    def mauHopLe(mau: int):
        return mau != 0
    
    @mau.setter
    def mau(self, Mau):
        if self.mauHopLe(Mau):
            self.__mau = Mau
        else:
            print("Mã số không hợp lệ")
            
    def rutGon(self):
        x = math.gcd(self.tu, self.mau)
        self.tu = self.tu // x
        self.mau = self.mau // x
    
    def __add__(self, other):
        result = PhanSo()
        if self.mau == other.mau:
            result.tu = self.tu + other.tu
            result.mau = self.mau
        else:
            result.tu = self.tu * other.mau + self.mau * other.tu
            result.mau = self.mau * other.mau
        return result.rutGon()
            
    def __sub__(self, other):
        result = PhanSo()
        if self.mau == other.mau:
            result.tu = self.tu - other.mau
            result.mau = self.mau
        else:
            result.tu = self.tu * other.mau - self.mau + other.tu
            result.mau = self.mau * other.mau
        return result.rutGon()
    
    def __muf__(self, other):
        result = PhanSo()
        result.tu = self.tu * other.tu
        result.mau = self.mau * other.mau
        result.rutGon()
        return result
    
    def __truediv__(self, other):
        result = PhanSo()
        result.tu = self.tu * other.mau
        result.mau = self.mau * other.tu
        result.rutGon()
        return result
    
    def __multiadd__(self, other):
        if self.mau == other.mau:
            self.tu = self.tu + other.tu
            self.mau = self.mau
            self.rutGon()
        else:
            self.tu = self.tu * other.mau + self.mau * other.tu
            self.mau = self.mau * other.mau
            self.rutGon()
        return self
    
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"

    def xuat(self):
        print(self.tu, "/", self.mau)