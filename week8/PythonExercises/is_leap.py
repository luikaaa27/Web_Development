def is_leap(year):
    leap = False
    if year%4==0 and year%100!=0 or year%400==0:
        leap = True
    
    return leap

year = int(raw_input())
print is_leap(year)from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end="")

