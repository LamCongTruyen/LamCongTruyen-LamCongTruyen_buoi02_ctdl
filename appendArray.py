import array

# Khai báo một mảng arr1 với kiểu dữ liệu 'i' và giá trị khởi tạo là [1, 2, 3, 4, 5]
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Thêm giá trị 6 vào cuối mảng bằng phương thức append
arr1.append(6)

# In ra mảng sau khi thêm giá trị mới
print(arr1)#[1, 2, 3, 4, 5, 6]