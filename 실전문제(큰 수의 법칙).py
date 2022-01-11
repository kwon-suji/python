'''N=int(input())
M=int(input())
K=int(input())
s=[]

for i in range(N):
    n=int(input())
    s.append(n)'''
N,M,K =  map(int, input().split())
s = list(map(int, input().split()))
sum=0

'''for i in range(N):
    for j in range(N-1):
        if(s[j+1]>s[j]):
            tmp=s[j+1]
            s[j+1]=s[j]
            s[j]=tmp'''
s.sort(reverse=True)


cnt=0
while True:
    for j in range(K):
        sum=sum+s[0]
        cnt=cnt+1
        if cnt== M:
           break
    if cnt== M:
        break
    sum=sum+s[1]
    cnt=cnt+1
    if cnt== M:
        break
print(sum)
