import array#khai thư viện array


myarray1 = array.array('i', [1,2,3,4])#khai báo kiểu dư liệu signed int và gắn giá trị ban đầu cho mảng array
print("mảng myarray: ",myarray1)#in ra màn hình
myarray1.insert(0,6)#chèn giá trị 6 vào vị trí thứ 0 của mảng
print("mảng myarray: ",myarray1)#in mảng sau khi chèn ra màn hình