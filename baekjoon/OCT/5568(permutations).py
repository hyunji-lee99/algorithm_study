import sys
from itertools import combinations, permutations

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
# n장의 카드 중 k개를 선택해서 만들 수 있는 수의 개수
card=[]
for _ in range(n):
    c=sys.stdin.readline().strip()
    card.append(c)

perm=set(permutations(card, k))
ans=set()
for p in perm:
    s=''.join(p)
    ans.add(s)

print(len(ans))
