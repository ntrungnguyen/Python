from os import system
from DanhSachHinhHoc import DanhSachHH
from Hinh_Vuong import HinhVuong


dshh = DanhSachHH()

def xuatMenu():
    print('\nChọn chức năng muốn thực hiện: ')
    print('0: Thoát chương trình')
    print('1: Thêm hình vào danh sách')
    print('2: Xuất danh sách hình học')
    print('3: Tìm hình có diện tích lớn nhất')
    print('4: Tìm hình có diện tích nhỏ nhất')
    print('5: Tìm hình tròn có diện tích lớn nhất')
    print('6: Sắp các hình giảm dần theo diện tích')
    print('7: Đếm số lượng hình theo loại')
    print('8: Tính tổng diện tích các hình')
    print('9: Tìm hình có diện tích lớn nhất theo loại hình học cho trước')
    print('10: Tìm vị trí của hình H trong danh sách')
    print('11: Tìm hình theo diện tích')
    print('12: Xoá một hình học khỏi danh sách')
    print('13: Xoá tất cả các hình theo loại cho trước')
    print('14: Xuất danh sách hình theo loại cho trước và sắp tăng hoặc giảm')
    print('15: Tính tổng diện tích các hinh theo loại')

while True:
    xuatMenu()
    try:
        nhap = int(input())
        if nhap == 0:
            break
        elif type(nhap) != int:
            print("Vui lòng nhập số thứ tự để thực hiện: ")
            nhap = int(input())
            xuatMenu()
    except:
        print("Không hợp lệ")
        break
    
    match nhap:
        case 1:
            system("CLS")
            print('1: Thêm hình vào danh sách')
            dshh.docFile()
        case 2:
            system("CLS")
            print("Danh sách hình học")
            dshh.xuat()
        case 3:
            system("CLS")
            print('3: Tìm hình có diện tích lớn nhất')
            dshh.timHinhCoDienTichLonNhat()
        case 4:
            system("CLS")
            print('4: Tìm hình có diện tích nhỏ nhất')
            dshh.timHinhCoDienTichNhoNhat()
        case 5:
            system("CLS")
            print('5: Tìm hình tròn có diện tích lớn nhất')
            dshh.timHinhCoDienTichLonNhatTheoLoai("HinhTron")
        case 6:
            system("CLS")
            print('6: Sắp các hình giảm dần theo diện tích')
            dshh.sapGiamTheoS()
            dshh.xuat()
        case 7:
            system("CLS")
            print('7: Đếm số lượng hình theo loại')
            dshh.demSoLuongHinhTheoLoai("HinhVuong")
        case 8:
            system("CLS")
            print('8: Tính tổng diện tích các hình')
            dshh.tinhTongS()
        case 9:
            system("CLS")
            print('9: Tìm hình có diện tích lớn nhất theo loại hình học cho trước')
            dshh.timHinhCoDienTichLonNhatTheoLoai("HinhVuong")
        case 10:
            system("CLS")
            print('10: Tìm vị trí của hình H trong danh sách')
        case 11:
            system("CLS")
            print('11: Tìm hình theo diện tích')
            kq = dshh.timHinhTheoS(12)
            for tmp in kq:
                print(tmp)
        case 12:
            system("CLS")
            print('12: Xoá một hình học khỏi danh sách')
            hv = HinhVuong(10)
            dshh.xoa(hv)
            dshh.xuat()
        case 13:
            system("CLS")
            print('13: Xoá tất cả các hình theo loại cho trước')
        case 14:
            system("CLS")
            print('14: Xuất danh sách hình theo loại cho trước và sắp tăng hoặc giảm')
        case 15:
            system("CLS")
            print('15: Tính tổng diện tích các hình theo loại')