import sys
from collections import deque

n,k=map(int, sys.stdin.readline().split(' '))
numbers=list(map(int, sys.stdin.readline().split(' ')))

# init
knumbers=deque(numbers[:k])
cur_sum=sum(knumbers)
max_value=cur_sum
for i in range(k, n):
    cur_sum-=knumbers.popleft()
    cur_sum+=numbers[i]
    knumbers.append(numbers[i])
    max_value=max(max_value, cur_sum)

print(max_value)
