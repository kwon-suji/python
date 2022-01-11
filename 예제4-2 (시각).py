N=int(input())

cnt=0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if(i== 3 or j== 3 or k== 3 or
               i==13 or j==13 or k==13 or
               i==23 or j==23 or k==23 or
                        j==30 or k==30 or
                        j==31 or k==31 or
                        j==32 or k==32 or
                        j==33 or k==33 or
                        j==34 or k==34 or
                        j==35 or k==35 or
                        j==36 or k==36 or
                        j==37 or k==37 or
                        j==38 or k==38 or
                        j==39 or k==39 or
                        j==43 or k==43 or
                        j==53 or k==53):
                cnt=cnt+1


print(cnt)


'''N = int(input())
c = 0
h = 0
m = 0
s = 0
while(1):
    s = s + 1
    if(s == 60):
        s = 0
        m = m +1
    if (m == 60):
        m = 0
        h = h + 1
    if(s%10 == 3 or int(s / 10) == 3):
        c = c + 1
    elif(m % 10 == 3 or int(m / 10) == 3):
        c= c +1
    elif(h % 10 == 3 or int(h/10) == 3):
        c = c + 1
    if(N == h and m == 59 and s == 59):
        break

print(c)'''
