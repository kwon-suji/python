n,m=map(int, input().split())
ar=[]
for i in range(n):
    ar.append(list(map(int, input())))

def check(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False

    if ar[x][y]==0:
        ar[x][y]=1

        check(x,y-1)
        check(x+1,y)
        check(x,y+1)
        check(x-1,y)
        return True
    
    return False

cnt=0

for i in range(n):
    for j in range(m):
        if check(i,j)==True:
            cnt+=1
print(cnt)
