n = int(input())
arr = [int(i) for i in input().split()]

for x in arr:
    if x%2==0:
        print(x,end=" ")
print()
