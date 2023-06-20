import sys

n=int(sys.stdin.readline())
S=set()
for _ in range(n):
    command=sys.stdin.readline().strip()
    if command!='all' and command!='empty':
        command, num=command.split(' ')
        num=int(num)
    if command=='add':
        S.add(num)
    elif command=='remove' and num in S:
        S.remove(num)
    elif command=='check':
        if num in S:
            print(1)
        else:
            print(0)
    elif command=='toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif command=='all':
        S={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif command=='empty':
        S.clear()


