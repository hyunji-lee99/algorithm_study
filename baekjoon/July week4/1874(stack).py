import sys

n=int(sys.stdin.readline())
# 오름차순으로 push되고 있는지 체크할 변수
cnt=0
stack=[]
ans=[]
for i in range(1,n+1):
    num=int(sys.stdin.readline())
    while cnt<num:
        cnt+=1
        stack.append(cnt)
        ans.append('+')
    if num==stack[-1]:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        sys.exit(0)

for a in ans:
    print(a)
