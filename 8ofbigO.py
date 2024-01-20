def factorial(n):
    if n<0:
        return -1 #bigO>>O(1)
    elif n == 0:#bigO>>O(1)
        return 1#bigO>>O(1)
    else:
        return n * factorial(n-1)