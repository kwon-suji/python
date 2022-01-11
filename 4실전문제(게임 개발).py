# -*- coding: cp949 -*-
N,M=map(int, input().split())
a,b,d=map(int, input().split())
cnt=1

#이중배열 입력받기
s=[0 for i in range(M)]
for j in range(M):
    s[j]=list(map(int, input().split()))

#step=(a,b)=(ud,lr)
#방향에 따른 이동값
if d==0:
    steps=[(0,-1),(1,0),(0,1),(-1,0)]
elif d==1:
    steps=[(-1,0),(0,-1),(1,0),(0,1)]
elif d==2:
    steps=[(0,1),(-1,0),(0,-1),(1,0)]
elif d==3:
    steps=[(1,0),(0,1),(-1,0),(0,-1)]


k=0

s[a][b]==1
print("처음 a,b=",a,b)
for i in range(4):
for step in steps:
    UD=a+step[0]
    LR=b+step[1]
    if s[UD][LR]==0:
        cnt+=1
        s[UD][LR]==1
        a=UD
        b=LR
        print("바뀐거 a,b=",a,b)
    
        d=3-k+d
        print("d=",d)
        if d==0:
            steps=[(0,-1),(1,0),(0,1),(-1,0)]
        elif d==1:
            steps=[(-1,0),(0,-1),(1,0),(0,1)]
        elif d==2:
            steps=[(0,1),(-1,0),(0,-1),(1,0)]
        elif d==3:
            steps=[(1,0),(0,1),(-1,0),(0,-1)]
        k=0
    else:
        k+=1
print(cnt)
