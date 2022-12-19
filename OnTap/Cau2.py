#Câu 2 (1 điểm) Viết chương trình xuất ra số đảo ngược của một số nguyên cho trước
#(không chuyển thành chuỗi rồi đảo ngược)

n = 7981

def reverse(num):
    rev = 0
    while num > 0:
        rev = (10 * rev) + num % 10
        num //= 10
    return rev

print(f"Số đã cho {n}")
print("Số đảo ngược", reverse(n))
