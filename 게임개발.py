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
    steps=[[0,-1],[1,0],[0,1],[-1,0]]
elif d==1:
    steps=[[-1,0],[0,-1],[1,0],[0,1]]
elif d==2:
    steps=[[0,1],[-1,0],[0,-1],[1,0]]
elif d==3:
    steps=[[1,0],[0,1],[-1,0],[0,-1]]


k=0

s[a][b]==1
print("처음 a,b=",a,b)

for step in steps:
        print("step=",step)
        print("steps=",steps)
        UD=a+step[0]
        LR=b+step[1]
        if s[UD][LR]==0:
            cnt+=1
            s[UD][LR]==1
            a=UD
            b=LR
            print("바뀐 a,b=",a,b)
    
            d=3-k+d
            print("d=",d)
            if d==0:
                steps=[[0,-1],[1,0],[0,1],[-1,0]]
            elif d==1:
                steps=[[-1,0],[0,-1],[1,0],[0,1]]
            elif d==2:
                steps=[[0,1],[-1,0],[0,-1],[1,0]]
            elif d==3:
                steps=[[1,0],[0,1],[-1,0],[0,-1]]
            k=0
        else:
            k+=1
print(cnt)
















#이중배열 입력받기
s=[0 for i in range(M)]
for j in range(M):
    s[j]=list(map(int, input().split()))


a,b = map(int,input().split())
cnt = 0
back = 0

c,d,e = map(int,input().split())

r = [[0 for j in range(b)]for i in range(a)]
for i in range(0,a):
    q = input()
    r[i] = [j for j in q.split(" ")]


    
r[c][d] = 999
while(1):
    print(r,e)
    if(e != 0):
        e = e - 1
    else:
        e = 3
    if(back == 4):
        if(e == 3):
            e = 0
        else:
            e=e+1
        back = 0
        if(e == 0):
            if(r[c+1][d] == '1' or c+1>=a):
                break
            else:
                r[c+1][d] = 999
                c = c + 1
                cnt = cnt+1
        if(e == 1):
            if(r[c][d-1] == '1' or d-1>=-1):
                break
            else:
                r[c][d-1] = 999
                d = d - 1
                cnt = cnt+1
        if(e == 2):
            if(r[c-1][d] == '1' or c-1>=-1):
                break
            else:
                r[c-1][d] = 999
                c = c -1
                cnt = cnt+1
        if(e == 3):
            if( d+1>=b):
                break
            elif(r[c][d+1] == '1' ):
                break
            else:
                r[c][d+1] = 999
                #print("4")
                d = d + 1
                cnt = cnt+1
                #print(cnt,e)
    if(e == 0):
        if(r[c-1][d] == 999 or (c-1<=-1) or r[c-1][d] == '1'):
            back = back+1
            continue
        else:
            r[c-1][d] = 999
            c = c - 1
            #print("5")
            cnt = cnt+1
            back = 0
            #print(cnt,e)
    if(e == 1):
        if( (d+1>=b)or r[c][d+1] == 999 or r[c][d+1] == '1'):
            back = back+1
            continue
        else:
           
            r[c][d+1] = 999
            d = d + 1
            cnt = cnt+1
            back = 0
            
    if(e == 2):
        if((r[c+1][d] == '1') or (r[c+1][d] == 999) or (c+1>=a)):
            back = back+1
            continue
        else:
            r[c+1][d] = 999
            c = c + 1
            cnt = cnt+1
            back = 0
            
    if(e == 3):
        if(r[c][d-1] == 999 or (d-1>=-1) or r[c][d-1] == '1' ):
            back = back+1
            continue
        else:
            r[c][d-1] = 999
            d = d - 1
            cnt = cnt+1
            #print("8")
            back = 0
           # print(cnt,e)

        
print(cnt+1)
