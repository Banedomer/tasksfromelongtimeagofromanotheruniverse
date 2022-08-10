# col- колличество окон
# okna[]- сами окна
# lub- № любимого окна
# sek- колличество секунд
# k- колличество альт табов

okna=[1]
col=int(input())
lub=int(input())
s=2
k=int(input())
b=1

while s<=col: 
    okna.append(s)
    print(okna[s-1])
    s=s+1
    
r=1

while r<=k:
    sek=int(input())
    sek=sek+1
    if (sek // col > 0):
        y=sek//col
        sek=sek-y*col
    d=okna[0]
    h=okna[sek]
    okna[0]=h
    okna[sek]=d
    r=r+1

r=0
while r<=col:
    if (okna[r]==lub):
        print(r)
    r=r+1
