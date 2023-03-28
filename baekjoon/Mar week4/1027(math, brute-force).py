# math(기울기), 완전탐색
# 왼쪽 요소는 기울기가 최소 기울기보다 작아야 보임
# 오른쪽 요소는 기울기가 최대 기울기보다 커야 보임

import sys

n=int(sys.stdin.readline())
building=list(map(int, sys.stdin.readline().split(' ')))

def left_search(c):
    cnt=0
    minlean=1e9
    for i in range(c-1,-1,-1):
        lean=(building[c]-building[i])/(c-i)
        if lean<minlean:
            minlean=lean
            cnt+=1
    return cnt

def right_search(c):
    cnt=0
    maxlean=-1e9
    for i in range(c+1, n):
        lean=(building[c]-building[i])/(c-i)
        if lean>maxlean:
            maxlean=lean
            cnt+=1
    return cnt


maxvalue=-1e9

for i in range(n):
    left_cnt=left_search(i)
    right_cnt=right_search(i)
    if left_cnt+right_cnt>maxvalue:
        maxvalue=left_cnt+right_cnt

print(maxvalue)

