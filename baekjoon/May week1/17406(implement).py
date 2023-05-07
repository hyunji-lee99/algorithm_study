import sys
from itertools import permutations

n,m,k=map(int, sys.stdin.readline().split(' '))
# dummy
A=[[0]*(m+1)]+[[0]+list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
command=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(k)]
# 순열 뽑기 용 command 순서 인덱스
pick=[x for x in range(k)]
# 순열 생성
nPr=list(permutations(pick, k))
def rotate(r,c,s):
    global A
    # 가장 왼쪽 윗 칸에서 시작
    starty=r-s
    startx=c-s
    # 몇 칸씩 이동할지
    step=s*2
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    copy_A=[arr[:] for arr in A]
    while starty!=r and startx!=c:
        for di in directions:
            for i in range(step):
                dy=starty+di[0]
                dx=startx+di[1]
                A[dy][dx]=copy_A[starty][startx]
                starty+=di[0]
                startx+=di[1]
        starty+=1
        startx+=1
        # step을 2로 나눠줘야 하는 줄 알고 헤맸음.. 2를 빼줬어야 함!
        step-=2



def calculate_minvalue():
    global A
    minvalue=1e9
    for i in range(1, n+1):
        sumValue=sum(A[i])
        minvalue=min(minvalue, sumValue)
    return minvalue

ans=1e9
original_A=[arr[:] for arr in A]
for p in nPr:
    for c in list(p):
        row,col,s=command[c]
        rotate(row,col,s)
    ans=min(ans, calculate_minvalue())
    # A 원상복구 시켜야 함
    A=[arr[:] for arr in original_A]

print(ans)
