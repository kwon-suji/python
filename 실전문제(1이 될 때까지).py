N,K=map(int, input().split())
cnt=0
while N/K !=1 :
    if N%K==0 :
        N=N/K
    else:
        N=N-1
    cnt=cnt+1
    
print(cnt+1)
print("수정8")
