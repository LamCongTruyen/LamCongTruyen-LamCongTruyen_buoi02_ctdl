def foo(array):
    sum = 0 #bigO laf O(1)
    product = 1 #bigO la O(1)

    for i in array: # lap qua cac phan tu,bigO la O(n)
        sum  +=i #truy cap 1 phan tu, bigO la O(1)

    for i in array: #lap qua cac phan tu, big O la O(n)
        product *= i #bigO la O(1)
    print("sum = "+str(sum)+", Product = "+str(product)) #bigO la O(1)