bar_rod=int(input())
bar_um=int(input())
c=int(input())
k=0

if(bar_rod % c == 0):
    k=1

k=k+(bar_um-bar_rod)//c

print(k)
