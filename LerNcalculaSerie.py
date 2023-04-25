n = int(input("Insira um número:"))
e = 0
for i in range(n,0,-1):
    e = e + 1/i
print ('E=',e)
