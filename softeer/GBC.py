import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))
limit_info = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
test_info = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(m)]

limit = [0] * 101
test = [0] * 101

cur_limit = 0
for length, li in limit_info:
    for i in range(cur_limit + 1, cur_limit + length + 1):
        limit[i] = li
    cur_limit += length

cur_test = 0
for length, te in test_info:
    for i in range(cur_test + 1, cur_test + length + 1):
        test[i] = te
    cur_test += length

maxvalue = -1e9
for i in range(101):
    maxvalue = max(maxvalue, test[i] - limit[i])

print(maxvalue)
