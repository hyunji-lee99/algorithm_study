import sys
from collections import deque

init=sys.stdin.readline().strip()
n=int(sys.stdin.readline())

# 초기 커서의 위치는 맨 뒤
# 커서 기준으로 왼쪽 스택
cl_stack=deque(list(init))
# 커서 기준으로 오른쪽 스택
cr_stack=deque()
for _ in range(n):
    command=sys.stdin.readline().strip().split(' ')
    # 커서 왼쪽으로 이동
    if command[0]=='L':
        if cl_stack:
            cr_stack.appendleft(cl_stack.pop())
    # 커서 오른쪽으로 이동
    elif command[0]=='D':
        if cr_stack:
            cl_stack.append(cr_stack.popleft())
    # 커서 왼쪽 요소 삭제
    elif command[0]=='B':
        if cl_stack:
            cl_stack.pop()
    # 커서 왼쪽에 ch 추가
    elif command[0]=='P':
        cl_stack.append(command[1])

print(*cl_stack,sep='',end='')
print(*cr_stack,sep='')
