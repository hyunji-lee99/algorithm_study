import sys

n,k=map(int, sys.stdin.readline().split(' '))
# 국가 번호, 금, 은, 동 메달 개 수
info=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
# k번 국가의 등수는?
# info[1], info[2], info[3] 순으로 정렬
# sort할 때, lambda의 다중 정렬 방식 주의
info.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)

ans_gold, ans_silver, ans_copper=0,0,0

order=0
for num, gold, silver, copper in info:
    if num==k:
        ans_gold, ans_silver, ans_copper=gold, silver, copper
        break

for num, gold, silver, copper in info:
    if gold==ans_gold and silver==ans_silver and copper==ans_copper:
        break
    else:
        order+=1

print(order+1)


