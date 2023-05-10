# pypy에선 통과, python에선 시간초과
import sys

n=int(sys.stdin.readline())
crane=list(map(int, sys.stdin.readline().split(' ')))
m=int(sys.stdin.readline())
box=list(map(int, sys.stdin.readline().split(' ')))

if max(crane)<max(box):
    print(-1)
    sys.exit(0)

crane.sort(reverse=True)
box.sort(reverse=True)

time=0
while box:
    for cr in crane:
        for i in range(len(box)):
            if box[i]<=cr:
                del box[i]
                break
    time+=1

print(time)

