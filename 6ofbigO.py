def reserse(array):
    for i in range(0, int(len(array)/2)): #bigO la O(N)-lap qua cac phan tu cua mang
        other = len(array) -i-1  #bigO laa O(1)-truy cap vao 1 phan tu cu the
        temp = array[i]#bigO laa O(1)
        array[i] = array[other]#bigO laa O(1)
        array[other] = temp#bigO laa O(1)
    print(array)#bigO laa O(1)