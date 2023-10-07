import sys

n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split(' ')))

ans=[-1]*n
stack=[]
stack.append(numbers[n-1])
for i in range(n-2, -1, -1):
    # 자신보다 큰 값이 stack의 top에 위치할 때까지 pop
    while stack and stack[-1]<=numbers[i]:
        stack.pop()
    # stack에 남은 값이 있으면
    if stack:
        ans[i]=stack[-1]
    stack.append(numbers[i])

print(*ans, sep=' ')