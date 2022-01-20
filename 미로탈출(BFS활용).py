n,m=map(int, input().split())
ar=[]

for i in range(n):
    ar.append(list(map(int, input())))

cnt=0

global min
min=999

def bfs(x,y,cnt):
    
    global min
    
    if x==n-1 and y==m-1:
        if cnt+1 < min:
            min=cnt+1
        
        return min

    if x<0 or x>=n or y<0 or y>=m:
        return min
    
    if ar[x][y]==1:
        ar[x][y]=cnt+1

        if min > bfs(x,y-1,ar[x][y]) :
            min=bfs(x,y-1,ar[x][y])
                    
        if min > bfs(x+1,y,ar[x][y]):
            min=bfs(x+1,y,ar[x][y])
                    
        if min > bfs(x,y+1,ar[x][y]) :
            min=bfs(x,y+1,ar[x][y])
                    
        if min > bfs(x-1,y,ar[x][y]) :
            min=bfs(x-1,y,ar[x][y])
    
    return min

print(bfs(0,0,0))

'''n,m = map(int, input().split())

ar = [0 for i in range(n)]

for i in range(n):
    ar[i] = list(map(int,input()))
nn = n
mm = m
cnt = [0,0,0,0]
cnt1 = 1
n = 0
m = 0
while(1):
    if(nn-1 == n and mm-1 == m):
        break
    if(m+1 < mm and ar[n][m+1] == 1):
       cnt1 = cnt1 + 1
       m = m + 1
       continue
    elif(n+1 <nn and ar[n+1][m] == 1):
        n = n + 1
        cnt1 = cnt1 + 1
        continue
    elif(n-1>=0 and ar[n-1][m] == 1):
        n = n - 1
        cnt1 = cnt1 + 1
        continue
    elif(m-1>=0 and ar[n][m-1] == 1):
        m = m - 1
        cnt1 = cnt1 + 1
        continue

cnt[0] = cnt1
cnt1 = 1
n = 0
m = 0
while(1): #case2
    if(nn-1 == n and mm-1 == m):
        break
    if(m+1 < mm and ar[n][m+1] == 1):
       cnt1 = cnt1 + 1
       m = m + 1
       continue
    elif(n+1 <nn and ar[n+1][m] == 1):
        n = n + 1
        cnt1 = cnt1 + 1
        continue
    elif(m-1>=0 and ar[n][m-1] == 1):
        m = m - 1
        cnt1 = cnt1 + 1
        continue
    elif(n-1>=0 and ar[n-1][m] == 1):
        n = n - 1
        cnt1 = cnt1 + 1
        continue
cnt[1] = cnt1
cnt1 = 1
n = 0
m = 0
while(1):
    if(nn-1 ==n and mm-1 ==m):
        break
    if(n+1 <nn and ar[n+1][m] == 1 ):
        n = n + 1
        cnt1 = cnt1 + 1
    elif(m+1 < mm and ar[n][m+1] == 1):
        m = m + 1
        cnt1 = cnt1 + 1
        continue
    elif(n-1>=0 and ar[n-1][m] == 1):
        n = n - 1
        cnt1 = cnt1 + 1
        continue
    elif(m-1>=0 and ar[n][m-1] == 1):
        m = m - 1
        cnt1 = cnt1 + 1
        continue

cnt[2] = cnt1
cnt1 = 1
n = 0
m = 0
while(1):
    if(nn-1 ==n and mm-1 ==m):
        break
    if(n+1 <nn and ar[n+1][m] == 1 ):
        n = n + 1
        cnt1 = cnt1 + 1
    elif(m+1 < mm and ar[n][m+1] == 1):
        m = m + 1
        cnt1 = cnt1 + 1
        continue
    elif(m-1>=0 and ar[n][m-1] == 1):
        m = m - 1
        cnt1 = cnt1 + 1
        continue
    elif(n-1>=0 and ar[n-1][m] == 1):
        n = n - 1
        cnt1 = cnt1 + 1
        continue

cnt[3] = cnt1

print(min(cnt))

10 9
100000000
100000000
100011000
100001111
100001001
111111001
000001001
001111001
001000001
001111111
'''
