n = int(input())
arr = [int(i) for i in input().split()]
arr.reverse()
for i in range (n):
    print(arr[i],end=" ")
print()