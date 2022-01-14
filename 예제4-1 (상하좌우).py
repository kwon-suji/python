N=int(input())
r=1
c=1
s=input().split()

for i in s:
    if i=='R' and c<N:
        c=c+1
    elif i=='L' and c>1:
        c=c-1
    elif i=='U' and r>1:
        r=r-1
    elif i=='D' and r<N:
        r=r+1
        
print(r,c)
