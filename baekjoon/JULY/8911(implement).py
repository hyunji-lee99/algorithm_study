import sys

n=int(sys.stdin.readline())
# 북 동 남 서
directions=[(0,1),(1,0),(0,-1),(-1,0)]
dir=0

for i in range(n):
    command=list(sys.stdin.readline().strip())
    maxx, maxy = 0,0
    minx, miny = 0,0
    # x,y
    cur=[0,0]
    for c in command:
        if c=='F':
            cur[0]+=directions[dir][0]
            cur[1]+=directions[dir][1]
            minx=min(minx, cur[0])
            maxx=max(maxx, cur[0])
            miny=min(miny, cur[1])
            maxy=max(maxy, cur[1])
        elif c=='B':
            cur[0] -= directions[dir][0]
            cur[1] -= directions[dir][1]
            minx = min(minx, cur[0])
            maxx = max(maxx, cur[0])
            miny = min(miny, cur[1])
            maxy = max(maxy, cur[1])
        elif c=='R':
            dir=(dir+1)%4
        elif c=='L':
            dir-=1
            if dir<0:
                dir+=4
    print(abs(maxx-minx)*abs(maxy-miny))
