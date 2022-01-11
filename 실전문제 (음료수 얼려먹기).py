'''N,M=map(int, input().split())
s= [list(map(int, input())) for _ in range(N)]
cnt=0

for i in range(N):
    for j in range(M):
        if s[i][j]==0:
            s[i][j]=2
            if i-1>-1 and N>=i+1 and j-1>-1 and M>=j+1:
                if s[i][j+1]!=2 and s[i][j-1]!=2 and s[i+1][j]!=2 and s[i-1][j]!=2:
                    cnt+=1
            
            if s[i][j+1]==0 and M>=j+1:
                s[i][j+1]=2
                
            if s[i][j-1]==0 and j-1>-1:
                s[i][j-1]=2
                
            if s[i+1][j]==0 and i+1>=N:
                s[i+1][j]=2
                
            if s[i-1][j]==0 and i-1>-1:
                s[i-1][j]=2

print(cnt)








N = int(input())
M = int(input())
ar=[0 for i in range(N)]
for i in range(N):
    ar[i] = list(map(int, input()))

ar1 = [[0 for i in range(M)]for j in range(N)] #북쪽스타트
ar2 = [[0 for i in range(M)]for j in range(N)] #동
ar3 = [[0 for i in range(M)]for j in range(N)] #남
ar4 = [[0 for i in range(M)]for j in range(N)] #서

for r in range(N):
    for t in range(M):
        ar1[r][t] = ar[r][t]
for r in range(N):
    for t in range(M):
        ar2[r][t] = ar[r][t]
for r in range(N):
    for t in range(M):
        ar3[r][t] = ar[r][t]
for r in range(N):
    for t in range(M):
        ar4[r][t] = ar[r][t]

cnt = 0
cnt1 = 0
cnt2 = 0
ccnt = 0
for h in range(N):
    for k in range(M):
        if(ar[h][k] == 0):
            ar[h][k] = 2
            i = h
            j = k
            while(1):#북쪽시작
                if(ccnt == 0):
                    if(ar1[i-1][j] == 0 and i-1>=0): #북
                        ar1[i-1][j] = 2
                        i = i-1
                        ccnt = 0
                        continue
                    else:
                        ccnt+=1
                if(ccnt == 1):
                    if(j+1<M):
                        if(ar1[i][j+1] == 0): #동
                            ar1[i][j+1] = 2
                            j = j + 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 2):
                    if(i+1<N):
                        if(ar1[i+1][j] == 0 and i+1<N): #남
                            ar1[i+1][j] = 2
                            i = i + 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 3):
                    if(ar1[i][j-1] == 0 and j-1>=0): #서
                        ar1[i][j-1] = 2
                        j = j - 1
                        ccnt = 0
                        continue
                    else:
                        ccnt+=1
                if(ccnt == 4):
                    ccnt = 0
                    print("-----Ar1-----")
                    print(ar1)
                    break
            i = h
            j = k
            while(1):#동쪽시작
                if(ccnt == 0):
                    if(j+1<M):
                        if(ar2[i][j+1] == 0): #동
                            ar2[i][j+1] = 2
                            j = j + 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 1):
                    if(i+1<N):
                        if(ar2[i+1][j] == 0): #남
                            ar2[i+1][j] = 2
                            i = i + 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 2):
                    if(j-1>=0):
                        if(ar2[i][j-1] == 0): #서
                            ar2[i][j-1] = 2
                            j = j - 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 3):
                    if(ar2[i-1][j] == 0 and i-1>=0): #북
                        ar2[i-1][j] = 2
                        i = i - 1
                        ccnt = 0
                        continue
                    else:
                        ccnt+=1
                if(ccnt == 4):
                    ccnt = 0
                    print("-----Ar2-----")
                    print(ar2)
                    break
            i = h
            j = k
            while(1):#남쪽시작
                if(ccnt == 0):
                    if(i+1<N):
                        if(ar3[i+1][j] == 0):
                            ar3[i+1][j] = 2
                            i = i + 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 1):
                    if(j-1>=0):
                        if(ar3[i][j-1] == 0):
                            ar3[i][j-1] = 2
                            j = j - 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 2):
                    if(i-1>=0):
                        if(ar3[i-1][j] == 0):
                            ar3[i-1][j] = 2
                            i = i - 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 3):
                    if(j+1<M):
                        if(ar3[i][j+1] == 0):
                            ar3[i][j+1] = 2
                            j = j + 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 4):
                    ccnt = 0
                    print("-----Ar3-----")
                    print(ar3)
                    break
            i = h
            j = k
            while(1):#서쪽시작
                if(ccnt == 0):
                    if(j-1>=0):
                        if(ar4[i][j-1] == 0):
                            ar4[i][j-1] = 2
                            j = j - 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 1):
                    if(i-1>=0):
                        if(ar4[i-1][j] == 0):
                            ar4[i-1][j] = 2
                            i = i - 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 2):
                    if(j+1<M):
                        if(ar4[i][j+1] == 0):
                            ar4[i][j+1] = 2
                            j = j + 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 3):
                    if(i+1<N):
                        if(ar4[i+1][j] == 0):
                            ar4[i+1][j] = 2
                            i = i + 1
                            ccnt = 0
                            continue
                        else:
                            ccnt+=1
                    else:
                        ccnt+=1
                if(ccnt == 4):
                    ccnt = 0
                    print("-----Ar4-----")
                    print(ar4)
                    break
            for w in range(N):
                for e in range(M):
                    if(ar1[w][e] == 2):
                        ar[w][e] = 2
            for w in range(N):
                for e in range(M):
                    if(ar2[w][e] == 2):
                        ar[w][e] = 2
            for w in range(N):
                for e in range(M):
                    if(ar3[w][e] == 2):
                        ar[w][e] = 2
            for w in range(N):
                for e in range(M):
                    if(ar4[w][e] == 2):
                        ar[w][e] = 2
            print(ar)
            cnt = cnt + 1

print(cnt)'''

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 2
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        print(x,y,"북 들어감")
        dfs(x - 1, y)
        #print("북")
        #print(graph)
        print(x,y,"서 들어감")
        dfs(x, y - 1)
       # print("서")
        #print(graph)
        print(x,y,"남 들어감")
        dfs(x + 1, y)
        #print("남")
        #print(graph)
        print(x,y,"동 들어감")
        dfs(x, y + 1)
        #print("동")
       # print(graph)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력

   
