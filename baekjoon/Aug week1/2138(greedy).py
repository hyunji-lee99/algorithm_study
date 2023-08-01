import sys

n=int(sys.stdin.readline())
start=list(map(int, sys.stdin.readline().strip()))
goal=list(map(int, sys.stdin.readline().strip()))

ans=[]
# 0번 스위치를 누른 경우
pushzero=1
pushzero_start=start.copy()
pushzero_start[0]=1-pushzero_start[0]
pushzero_start[1]=1-pushzero_start[1]
for i in range(1,n):
    if pushzero_start[i-1]!=goal[i-1]:
        pushzero+=1
        # i번 스위치 눌러야 함
        for t in (i-1, i, i+1):
            if 0<=t<n:
                pushzero_start[t]=1-pushzero_start[t]
if pushzero_start==goal:
    ans.append(pushzero)

# 0번 스위치 안누른 경우
notpushzero=0
for i in range(1,n):
    if start[i-1]!=goal[i-1]:
        notpushzero+=1
        for t in (i-1,i,i+1):
            if 0<=t<n:
                start[t]=1-start[t]
if start==goal:
    ans.append(notpushzero)

if ans:
    print(min(ans))
else:
    print(-1)
