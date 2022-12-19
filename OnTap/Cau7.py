import numpy as np

A = [[11,22,35,20],[45,28,39,70],[3,9,13,17]]
print(A)

arr = np.array(A)

print(f'Phần tử cuối cùng mỗi hàng: {arr[0:,-1]}')
arr[0:].sort()