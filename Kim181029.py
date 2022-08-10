N=int(input())
t=int(input())
a=[0]
b=[]
c=[]
suma=0
sumb=0

for i in range(N):
    a.append(int(input()))
    b.append(int(input()))

for i in range(N):
    sumb=0
    suma=0
    for k in range(i,N):
        sumb+=b[k]
    for h in range(0,i+1):
        suma+=a[h]
    c.append(sumb+suma+t)


print(min(c))