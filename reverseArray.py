import array

# Khai báo một mảng arr1 với kiểu dữ liệu 'i' và giá trị khởi tạo là [1, 2, 3, 4, 5]
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Sử dụng phương thức reverse để đảo ngược mảng
arr1.reverse()

# In ra mảng sau khi đảo ngược
print(arr1)
