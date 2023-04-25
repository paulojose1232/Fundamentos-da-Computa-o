i = input("Insira a ou b ou c: ")
j=1001
h=10000
import math
for x in range(j,h):
    if i=="a":
        n=str(x)
        if x==(int(n[0]+n[1])+int(n[2]+n[3]))**2:
            print("",x)
    elif i=="c":
        d=2
        for y in range(2,math.ceil(math.sqrt(x))):
            if x%y==0:
                d+=1
        if d==2:
            print("",x)
    elif i=="b":
        s=0
        for y in range(1,x-1):
            if x%y==0:
                s=y+s
        if x==s:
            print("",x)