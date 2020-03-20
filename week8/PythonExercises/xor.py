def xor(x,y):
   if(x==1) and (y==0):
        return True
    elif (x==0) and (y==1):
        return True
    else:
        return False
a,b=input().split()
if xor(int(a),int(b)) == True:
    print("1")
else:
    print("0")
    
