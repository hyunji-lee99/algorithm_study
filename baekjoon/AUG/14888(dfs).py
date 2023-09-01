import sys

n=int(sys.stdin.readline().strip())
numbers=list(map(int, sys.stdin.readline().strip().split(' ')))
opr=list(map(int, sys.stdin.readline().strip().split(' ')))

maxans=int(-1e9)
minans=int(1e9)
def dfs(cur,idx):
    global maxans, minans, n
    if idx==n:
        maxans=max(maxans, cur)
        minans=min(minans, cur)
        return
    # 더하기
    if opr[0]>0:
        opr[0]-=1
        dfs(cur+numbers[idx], idx+1)
        opr[0]+=1
    # 빼기
    if opr[1]>0:
        opr[1]-=1
        dfs(cur-numbers[idx], idx+1)
        opr[1]+=1
    # 곱하기
    if opr[2]>0:
        opr[2]-=1
        dfs(cur*numbers[idx], idx+1)
        opr[2]+=1
    # 나누기
    if opr[3]>0:
        opr[3]-=1
        if cur<0:
            cur=-cur
            dfs(-(cur//numbers[idx]), idx+1)
        else:
            dfs(cur//numbers[idx], idx+1)
        opr[3]+=1

dfs(numbers[0], 1)

print(maxans)
print(minans)