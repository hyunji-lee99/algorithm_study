import sys

w, n = map(int, sys.stdin.readline().split(' '))
things = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 무게당 가격순으로 내림차순 sort
things.sort(key=lambda x: x[1], reverse=True)

ans = 0
for weight, price in things:
    # 배낭에 넣을 수 있는 무게가 weight보다 크다면
    if w >= weight:
        w -= weight
        ans += (weight * price)
    else:
        ans += (w * price)
        break

print(ans)
