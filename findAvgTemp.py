def calculate_average_temperature(temperatures):# gọi hàm tính giá trị nhiệt độ trung bình
    average_temperature = sum(temperatures) / len(temperatures)#giá trị nhiệt độ trung bình bằng tổng của mảng chia cho chiều dài mảng
    return average_temperature # trả về giá trị nhiệt độ trung bình

def count_days_above_average(temperatures):#gọi hàm tính số ngày nhiêt độ cao hơn nhiệt độ trung bình
    average_temperature = calculate_average_temperature(temperatures)#gọi lại giá trị nhiệt độ trung bình
    days_above_average = 0#tạo biến đếm(số ngày)  bằng 0
    for temperature in temperatures:#chạy biến temperature trong cái mảng temperatures
        if temperature > average_temperature:#nếu biến temperatures lớ hơn giá trị nhiệt độ trung bình
            days_above_average += 1#tăng biến đếm số ngày lên một(days_above_average= days_above_average + 1)
    return days_above_average#trả về giá trị của số ngày nhiệt độ lớn hơn nhiệt độ trung bình

temperature = [27, 28, 29, 30, 31, 32, 33]#khai báo mảng gồm 7 giá trị tương đương nhiệt độ của 7 ngày trong tuần

days_above_average_count = count_days_above_average(temperature)#gán giá trị của hàm count_days_above_average(temperature) cho biến days_above_average_count
average_temperature = calculate_average_temperature(temperature)#gián giá trị của hàm calculate_average_temperature(temperature) cho biến average_temperature
print(f"Số ngày có nhiệt độ cao hơn giá trị trung bình là: {days_above_average_count}")#in ra màn hình
print(f"nhiet do trung binh la: {average_temperature}")#in ra màn hình



