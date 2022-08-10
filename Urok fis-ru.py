n=int(input())
mal=[]
dev=[]
k=0

for k in range(n):
    pol=int(input())
    if (pol==0):
        heghtM=int(input())
        mal.append(heghtM)
    elif (pol==1):
        heghtD=int(input())
        dev.append(heghtD)

mal.sort()
dev.sort()

esy=dev[-1]-mal[0]

print(esy)
        
