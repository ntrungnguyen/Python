from datetime import datetime
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from ds_sinh_vien import DanhSachSv

sv1 = SinhVienChinhQuy(1957690, "Trần Văn A", datetime.strptime("23/6/1999", "%d/%m/%Y"), 80)
sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", datetime.strptime("5/12/1999", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiChinhQuy(1957692, "Thái Thị Thu", datetime.strptime("15/8/1998", "%d/%m/%Y"), "Cao Đẳng", 2)
sv4 = SinhVienPhiChinhQuy(2000324, "Trần Thanh Tâm", datetime.strptime("27/8/2000", "%d/%m/%Y"), "Cao Đẳng", 2)
sv5 = SinhVienPhiChinhQuy(2004544, "Nguyễn Thanh Trà", datetime.strptime("17/5/2000", "%d/%m/%Y"), "Trung Cấp", 2.5)
sv6 = SinhVienChinhQuy(2004567, "Nguyễn Thành Nam", datetime.strptime("7/12/1999", "%d/%m/%Y"), 60)
sv7 = SinhVienPhiChinhQuy(2004545, "Nguyễn Thanh Thanh", datetime.strptime("29/10/1999", "%d/%m/%Y"), "Trung Cấp", 2.5)
sv8 = SinhVienChinhQuy(2004679, "Võ Hoài Nam", datetime.strptime("4/1/2000", "%d/%m/%Y"), 70)

dssv = DanhSachSv()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

dssv.xuat()

vt = dssv.timSVTheoMs(2000324)
print(f"\nSinh viên ở vị trí thứ {vt + 1} trong danh sách")

kq = dssv.timSvTheoLoai("chinhquy")
print("\nDanh sách sinh viên theo loại")
for sv in kq:
    print(sv)
    
diem = 80
kqdiem = dssv.diemRL(diem)
print(f"\nDanh sách sinh viên có điểm rèn luyện từ {diem} trở lên")
for tmp in kqdiem:
    print(tmp)
    
kqcd = dssv.trinhDoCaoDangSinhTruocNgay("15/8/1999", "Cao đẳng")
print("\nSinh viên có trình độ cao đẳng sinh trước ngày 15/8/1999")
for tmp in kqcd:
    print(tmp)
    
#------------------------------------------------------------#
mssvTim = 1957691
print(f"\nVị trí của sinh viên có mã số {mssvTim} là: {dssv.timVtSvTheoMs(mssvTim) + 1}")

vt = dssv.xoaSvTheoMs(mssvTim)
if vt != -1:
    print(f"Sinh viên có mã số {mssvTim} nằm ở vị trí thứ {vt + 1} trong danh sách")
else:
    print(f"Sinh viên có mã số {mssvTim} không tồn tại trong danh sách")
    

if dssv.xoaSvTheoMs(mssvTim):
    print(f"Đã xóa sinh viên có mã số {mssvTim} trong danh sách")
else:
    print(f"Không xóa được mssv {mssvTim} không tồn tại trong danh sách")
