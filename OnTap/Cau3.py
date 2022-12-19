#Viết chương trình cho nhập vào 2 số nguyên a, b bất kỳ. Yêu cầu người
#dùng nhập 1 số nằm trong đoạn [a, b] (hoặc [b,a] nếu b < a), xuất ra màn hình kết quả của
#số đó chia cho 3, lấy 2 số thập phân. Nếu nhập sai yêu cầu thì người dùng phải nhập lại.

a = int(input("Nhập vào số thứ nhất: "))
b = int(input("Nhập vào số thứ hai: "))

if (b < a):
    num = int(input(f"Nhập vào một số trong đoạn [{b},{a}]:"))
    while num < b or num > a:
        num = int(input(f"Nhập vào một số trong đoạn [{b},{a}]:"))
    print(f"Kết quả của số {num} chia cho 3 là", round(num/3,2))
else:
    num = int(input(f"Nhập vào một số trong đoạn [{a},{b}]:"))
    while num > b or num < a:
        num = int(input(f"Nhập vào một số trong đoạn [{a},{b}]:"))
    print(f"Kết quả của số {num} chia cho 3 là", round(num/3,2))