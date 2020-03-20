def count_evens(n):
    cnt = 0
    for i in n:
        cnt-=i%2-1
    return cnt