N,M=map(int, input().split())

k=[]
for i in range(N):
    s=list(map(int, input().split()))
    k.append(min(s))


print(max(k))
