n = int(input())
arr = [int(i) for i in input().split()]
sum = 0
for i in range (1,n):
    if arr[i]>arr[i-1]:
        sum+=1
print(sum)