import sys

n=int(sys.stdin.readline())
calculate=list(sys.stdin.readline().strip())
numbers=[int(sys.stdin.readline()) for _ in range(n)]

stack=[]
idx=0
for cal in calculate:
    if cal=='+':
        a=stack.pop()
        b=stack.pop()
        stack.append(b+a)
    elif cal=='-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif cal=='/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    elif cal=='*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b*a)
    else:
        stack.append(numbers[ord(cal)-65])


print('{:.2f}'.format(stack[-1]))