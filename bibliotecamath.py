import math
e = 0
x = float(input("Insira x:"))
y = float(input("Insira y:"))
for i in range(1,51,1):
    e = e+(x+math.sqrt(y+2))/3+i**2-y**5
print (e)