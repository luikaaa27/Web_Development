n = int(input())
arr = [int(i) for i in input().split()]
sum = 0
for i in range (1,n):
    if arr[i]>0 and arr[i-1]>0 or arr[i]<0 and arr[i-1]<0:
        sum = 1
        print("YES")
        break
if sum==0 :
    print("NO")