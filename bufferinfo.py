import array

# Khai báo một mảng arr1 với kiểu dữ liệu 'i' và giá trị khởi tạo là [1, 2, 3, 4, 5]
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Lấy thông tin bộ đệm thông qua phương thức buffer_info
buffer_info = arr1.buffer_info()

# In ra thông tin bộ đệm
print("Địa chỉ bắt đầu của bộ đệm:", buffer_info[0])
print("Số lượng phần tử trong mảng:", buffer_info[1])#từ vị trí thứ 2 thì chính là giá trị đầu tiên của mảng
