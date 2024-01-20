import array

# Khai báo một mảng arr1 với kiểu dữ liệu 'i' và giá trị khởi tạo là [1, 2, 3, 4, 2, 5, 2]
arr1 = array.array('i', [1, 2, 3,3, 4, 3, 2, 5, 2])

# Kiểm tra số lần xuất hiện của giá trị 2 bằng phương thức count
count_of_3 = arr1.count(3)

# In ra số lần xuất hiện
print(f"Số lần xuất hiện của giá trị 3 trong mảng là: {count_of_3}")#3 lần
