import math
a = int(input())
b = int(input())
i = math.ceil(math.sqrt(a))
while i*i<=b:
    print(i*i)
    i+=1