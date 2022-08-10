A=str(input())
B=str(input())
C=str(input())

A=A.replace(':','')
B=B.replace(':','')
C=C.replace(':','')

A=int(A) #vremya otpravki klientom
B=int(B) #vremya otpravki serverom
C=int(C) #vremya poluchenya klientom

A1=A%100 #desyatki(sek)
A2=int((A%10000-A%100)/100) #sotni(min)
A3=A//10000 #tusyachi(chas)
print(A3)

B1=B%100
B2=int((B%10000-B%100)/100)
B3=B//10000
print(B3)

C1=C%100
C2=int((C%10000-C%100)/100)
C3=C//10000
print(C3)

L1=C1-A1
if (L1>=60):
    L2=L2+1
    L1=L1-60
L2=C2-A2
if (L2>=60):
    L3=L3+1
    L2=L2-60
L3=C3-A3
print(L1)

S1=L1//2
if (L3%2>=0,5):
    S1=S1+1
S2=L2//2
if (L2%2>=0,5):
    S2=S2+1
S3=L3

K2=0
K3=0
K1=S1+B1
if (K1>=60):
    K2=K2+1
    K1=K1-60
K2=S2+B2
if (K2>=60):
    K3=K3+1
    K2=K2-60
K3=B3+L3

print(str(K3)+':'+str(K2)+':'+str(K1))




