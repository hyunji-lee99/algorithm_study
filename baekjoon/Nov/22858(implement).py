import sys

n,k=map(int, sys.stdin.readline().split(' '))
S=list(map(int, sys.stdin.readline().split(' ')))
D=list(map(int, sys.stdin.readline().split(' ')))

P=[0]*n
for _ in range(k):
    # D[i]번째 카드를 i번째로 가져오는 연산을 취소하자
    # i번째 카드를 D[i]번째로 가져오는 연산 수행
    for idx in range(n):
        P[D[idx]-1]=S[idx]
    S=P.copy()

print(*S, sep=' ')

