def centered_average(arr):
    arr.sort()
    return sum(arr[1:-1])/(len(arr)-2)