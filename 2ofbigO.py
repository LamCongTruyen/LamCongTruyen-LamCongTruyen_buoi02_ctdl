def printParis(array):
    for i in array : #bigO la O(n^2)
        for j in array: # bigO la O(n)
            print(str(i)+","+str(j)) #bigO la O(1)
