import sys

h,w,x,y=map(int, sys.stdin.readline().split(' '))
B=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(h+x)]

for i in range(x,h+x):
    for j in range(y,w+y):
        # A 배열과 겹치는 부분
        if i<h and j<w:
            B[i][j]-=B[i-x][j-y]

for i in range(h):
    for j in range(w):
        print(B[i][j], end=' ')
    print('')

