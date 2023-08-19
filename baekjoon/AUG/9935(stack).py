import sys

init_str=sys.stdin.readline().strip()
pung_str=sys.stdin.readline().strip()

# replace의 시간 복잡도
# while pung_str in init_str:
#     init_str=init_str.replace(pung_str, '')
#
# if init_str=='':
#     print('FRULA')
# else:
#     print(init_str)

length=len(pung_str)
stack=[]
for s in init_str:
    stack.append(s)
    if len(stack)>=length and ''.join(stack[-length:])==pung_str:
        for _ in range(length):
            stack.pop()

ans=''.join(stack)

if ans=='':
    print('FRULA')
else:
    print(ans)