minx1=10000
minx2=10000
minx3=10000
minx4=10000
miny1=10000
miny2=10000
miny3=10000
miny4=10000
chet1=0
chet2=0
chet3=0
chet4=0
N=int(input())
for i in range(N):
    x=int(input())
    y=int(input())
    if (x>=0) and (y>=0):  #1 четверть
        chet1+=1
        if (minx1>x) or (miny1>y):
            minx1=x
            miny1=y
    elif (x<=0) and (y>=0):  #2 четверть
        chet2+=1
        if (minx2>x) or (miny2>y): 
            minx2=x
            miny2=y
    elif (x<=0) and (y<=0):  #3 четверть
        chet3+=1
        if (minx3>x) or (miny3>y):  
            minx3=x
            miny3=y
    elif (x>=0) and (y<=0):  #4 четверть
        chet4+=1
        if (minx4>x) or (miny4>y):
            minx4=x
            miny4=y
if(chet1>chet2) and (chet1>chet3) and (chet1>chet4):
    print('K = 1')
    print('M = ',chet1)
    print('A = (',minx1,',',miny1,')')
    if (minx1<miny1):
        print('R =',minx1)
    else:
        print('R =',miny1)
elif(chet2>chet1) and (chet2>chet3) and (chet2>chet4):
    print('K = 2')
    print('M = ',chet2)
    print('A = (',minx2,',',miny2,')')
    if (minx2<miny2):
        print('R =',minx2)
    else:
        print('R =',miny2)
elif(chet3>chet2) and (chet3>chet1) and (chet3>chet4):
    print('K = 1')
    print('M = ',chet3)
    print('A = (',minx3,',',miny3,')')
    if (minx3<miny3):
        print('R =',minx3)
    else:
        print('R =',miny3)
elif(chet4>chet2) and (chet4>chet3) and (chet4>chet1):
    print('K = 1')
    print('M = ',chet4)
    print('A = (',minx4,',',miny4,')')
    if (minx4<miny4):
        print('R =',minx4)
    else:
        print('R =',miny4)