import sys

n,t=map(int, sys.stdin.readline().strip().split(' '))

L=[]
R=[]
for _ in range(n):
    l,r=map(int, sys.stdin.readline().strip().split(' '))
    L.append(l)
    R.append(r)

# 최소 주량을 모두 더했는데 t보다 크다면 불가능한 경우
if sum(L)>t:
    print(-1)
    sys.exit(0)
# 최대 주량을 모두 더했는데 t보다 작다면 불가능한 경우
if sum(R)<t:
    print(-1)
    sys.exit(0)

def possible(mid):
    more=0
    min_adding=0
    for l,r in list(zip(L,R)):
        min_adding+=l
        if l<=mid<=r:
            more+=(mid-l)
        elif mid>r:
            more+=(r-l)
    if more>=(t-min_adding):
        return True
    else:
        return False

startS=max(L)
endS=max(R)
mid=(startS+endS)//2

while startS<=endS:
    mid = (startS + endS) // 2
    # S가 mid일 때 가능한가?
    if possible(mid):
        # 가능할 경우 -> mid 값을 더 줄일 수 없는지?
        endS=mid-1
    else:
        # 불가능할 경우 -> mid 값을 더 늘려도 안되는가?
        startS=mid+1

print(mid)

