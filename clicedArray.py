import array

# Khai báo một mảng arr1 với kiểu dữ liệu 'i' và giá trị khởi tạo là [1, 2, 3, 4, 5]
arr1 = array.array('i', [1, 2,3, 4, 5])

# Cắt mảng từ vị trí 1 đến 5 (không bao gồm chỉ số 3)
sliced_array = arr1[1:5]

# In ra mảng sau khi cắt
print(sliced_array)#array('i', [2, 3, 4, 5])
