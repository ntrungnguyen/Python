from datetime import datetime
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiChinhQuy
from ds_sinh_vien import DanhSachSinhVien

sv1 = SinhVienChinhQuy(1957690, "Trần Văn A", datetime.strptime("23/6/1999", "%d/%m/%Y"), 80)
sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", datetime.strptime("5/12/1999", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiChinhQuy(1957692, "Thái Thị Thu", datetime.strptime("15/8/1998", "%d/%m/%Y"), "Cao Đẳng", 2)
sv4 = SinhVienPhiChinhQuy(2000324, "Trần Thanh Tâm", datetime.strptime("27/8/2000", "%d/%m/%Y"), "Cao Đẳng", 2)
sv5 = SinhVienPhiChinhQuy(2004544, "Nguyễn Thanh Trà", datetime.strptime("17/5/2000", "%d/%m/%Y"), "Trung Cấp", 2.5)
sv6 = SinhVienChinhQuy(2004567, "Nguyễn Thành Nam", datetime.strptime("7/12/1999", "%d/%m/%Y"), 60)
sv7 = SinhVienPhiChinhQuy(2004545, "Nguyễn Thanh Thanh", datetime.strptime("29/10/1999", "%d/%m/%Y"), "Trung Cấp", 2.5)
sv8 = SinhVienChinhQuy(2004679, "Võ Hoài Nam", datetime.strptime("4/1/2000", "%d/%m/%Y"), 70)


dssv = DanhSachSinhVien()
dssv.themSv(sv1)
dssv.themSv(sv2)
dssv.themSv(sv3)
dssv.themSv(sv4)
dssv.themSv(sv5)
dssv.themSv(sv6)
dssv.themSv(sv7)
dssv.themSv(sv8)


dssv.xuat()
vt = dssv.timSvTheoMaSo(1957690)
print(f"\nSinh viên ở vị trí thứ {vt + 1} trong danh sách")

kq = dssv.timSvTheoLoai("chinh quy")
print("Danh sách sinh viên theo loại")
for sv in kq:
    print(sv)


diem = 80
kq2 = dssv.diemRL(diem)
print(f"\nDanh sách sinh viên có điểm rèn luyện từ {diem} trở lên")
for sv in kq2:
    print(sv)
    

mssv = 1957690
if dssv.xoaSvTheoMaSo(mssv):
    print(f"\nĐã xóa sinh viên có mã số {mssv} trong danh sách")
else:
    print(f"\nKhông xóa được mssv {mssv} không tồn tại trong danh sách")
    
dssv.xuat()