import array

# Khai báo một mảng arr1 với kiểu dữ liệu 'i' và giá trị khởi tạo là [1, 2, 3, 4, 5, 6]
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])

# Sử dụng phương thức pop để xóa phần tử cuối cùng của mảng
arr1.pop()#pop-đưa vào ngăn xếp

# In ra mảng sau khi xóa phần tử cuối cùng
print(arr1)