import sys

# 지방의 수
n=int(sys.stdin.readline())
# 각 지방의 요청 예산
money=list(map(int, sys.stdin.readline().split(' ')))
# 총 예산
m=int(sys.stdin.readline())

start=0
end=m
maxvalue=0
# 모든 요청이 배정될 수 있는 경우. 즉, 모든 요청의 합이 총 예산보다 작거나 같은 경우
if sum(money)<=m:
    print(max(money))
else:
    while start <= end:
        mid = (start + end) // 2
        # mid=상한액
        # 상한액이 mid일 경우에 총 예산 계산하기
        sum_money = 0
        for mo in money:
            if mo > mid:
                sum_money += mid
            else:
                sum_money += mo
        # 계산한 총 예산이 기존의 총 예산 m보다 클 경우 상한액이 작아져야 함
        if sum_money > m:
            end = mid - 1
        # 계산한 총 예산이 기존의 총 예산 m보다 작거나 같은 경우 상한액이 더 커질 수 있는지 점검하고, 상한액의 max값을 갱신함
        else:
            maxvalue = max(maxvalue, mid)
            start = mid + 1

    print(maxvalue)


