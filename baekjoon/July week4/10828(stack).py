import sys

n=int(sys.stdin.readline())
stack=[]
for i in range(n):
    command=list(sys.stdin.readline().strip().split(' '))
    # push 연산인지 확인
    if command[0]=='push':
        num=int(command[1])
        stack.append(num)
    elif command[0]=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0]=='size':
        print(len(stack))
    elif command[0]=='empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0]=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

