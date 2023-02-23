# 1-n까지 자연수 중 m개를 고른 수열
# 고른 수열은 비내림차순이어야 하며, 사전순으로 증가하는 순서로 출력
# 중복해서 고를 수 있음
import sys
from itertools import combinations_with_replacement

n,m=map(int,sys.stdin.readline().split(' '))
numbers=[i for i in range(1,n+1)]

cwr=list(combinations_with_replacement(numbers,m))

for c in cwr:
    for i in c:
        print(i,end=' ')
    print('')
