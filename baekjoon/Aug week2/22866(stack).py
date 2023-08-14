import sys

n=int(sys.stdin.readline())
building=list(map(int, sys.stdin.readline().strip().split(' ')))
building.insert(0,0)

# 스택을 이용해서 좌측으로 볼 수 있는 건물들, 우측으로 볼 수 있는 건물들 확인

count=[0]*(n+1)
# 좌측으로 볼 수 있는 건물 확인
stackL=[]
ansL=[0]*(n+1)
for i in range(1,n+1):
    while stackL and stackL[-1][0]<=building[i]:
        stackL.pop()
    if stackL:
        ansL[i]=stackL[-1][1]
        count[i]+=len(stackL)
    stackL.append((building[i], i))

# 우측으로 볼 수 있는 건물 확인
stackR=[]
ansR=[0]*(n+1)
for i in range(n,0,-1):
    while stackR and stackR[-1][0]<=building[i]:
        stackR.pop()
    if stackR:
        ansR[i]=stackR[-1][1]
        count[i]+=len(stackR)
    stackR.append((building[i], i))

ans=[0]*(n+1)
for i in range(1, n+1):
    if count[i]==0:
        continue
    if ansR[i]!=0 and ansL[i]!=0:
        if (ansR[i] - i) == (i - ansL[i]):
            ans[i] = ansL[i]
        elif (ansR[i] - i) > (i - ansL[i]):
            ans[i] = ansL[i]
        elif (ansR[i] - i) < (i - ansL[i]):
            ans[i] = ansR[i]
    elif ansR[i]==0 and ansL[i]!=0:
        ans[i]=ansL[i]
    elif ansR[i]!=0 and ansL[i]==0:
        ans[i]=ansR[i]


for i in range(1, n+1):
    if count[i]==0:
        print(0)
    else:
        print(count[i], ans[i])