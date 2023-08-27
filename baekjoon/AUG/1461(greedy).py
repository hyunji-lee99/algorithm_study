import sys
from collections import deque

n,m=map(int, sys.stdin.readline().strip().split(' '))
books=list(map(int, sys.stdin.readline().strip().split(' ')))

books.sort()

# 절댓값이 가장 큰 인덱스가 양수인지 음수인지?
maxidx=0
if abs(books[-1])>abs(books[0]):
    maxidx=-1

plus=deque()
minus=deque()
for book in books:
    if book>0:
        plus.append(book)
    else:
        minus.append(book)

# 음수 영역 기준 최소 발자국 구하기
ans_minus=0
mod_minus=len(minus)%m
step=0
if minus and len(minus)<=m:
    if minus[0]==books[maxidx]:
        ans_minus+=abs(minus[0])
    else:
        ans_minus+=abs(minus[0])*2
else:
    if mod_minus != 0:
        for _ in range(mod_minus):
            step = minus.pop()
        ans_minus += (abs(step) * 2)

    while minus:
        if len(minus) <= m:
            if minus[0] == books[maxidx]:
                ans_minus += abs(minus[0])
                break
        for _ in range(m):
            step = minus.pop()
        ans_minus += (abs(step) * 2)

# 양수 영역 기준 최소 발자국 구하기
ans_plus=0
mod_plus=len(plus)%m
step=0
if plus and len(plus)<=m:
    if plus[-1]==books[maxidx]:
        ans_plus+=plus[-1]
    else:
        ans_plus+=plus[-1]*2
else:
    if mod_plus != 0:
        for _ in range(mod_plus):
            step = plus.popleft()
        ans_plus += (step * 2)

    while plus:
        if len(plus) <= m:
            if plus[-1] == books[maxidx]:
                ans_plus += plus[-1]
                break
        for _ in range(m):
            step = plus.popleft()
        ans_plus += (step * 2)

print(ans_plus+ans_minus)




