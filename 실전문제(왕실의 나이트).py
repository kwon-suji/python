'''N=input()
r=N[0]
c=N[1]

r=ord(r)
c=ord(c)

cnt=0


if(r+2<=104 and c+1<=56):
    cnt=cnt+1
if(r+2<=104 and c-1>=49):
    cnt=cnt+1
    
if(r-2>=97 and c+1<=56):
    cnt=cnt+1
if(r-2>=97 and c-1>=49):
    cnt=cnt+1
    
if(r+1<104 and c+2<56):
    cnt=cnt+1
if(r+1<104 and c-2>=49):
    cnt=cnt+1
    
if(r-1>=97 and c+2<=56):
    cnt=cnt+1
if(r-1>=97 and c-2>=49):
    cnt=cnt+1

print(cnt)
'''


N=input()

r=ord(N[0])-ord('a')+1
c=int(N[1])

steps=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

cnt=0

for step in steps:
    rr=r+step[0]
    cc=c+step[1]
    if 0<rr and rr<9 and 0<cc and cc<9:
        cnt=cnt+1

print(cnt)




































