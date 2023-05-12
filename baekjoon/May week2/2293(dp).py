# https://velog.io/@jxlhe46/%EB%B0%B1%EC%A4%80-2293%EB%B2%88.-%EB%8F%99%EC%A0%84-1-bfi120m5
# 위 블로그 아이디어 참고
import sys

n,k=map(int, sys.stdin.readline().split(' '))
coin=[int(sys.stdin.readline()) for _ in range(n)]
# 처음엔 [0]*(k+1)이 n줄 있는 2차원 배열로 선언함
# n이 최대 100, k가 최대 100000이므로 둘다 최대일 경우 10^8로 메모리 초과가 발생함
# 1차원 배열로 변경해서 생각
dp=[0]*(k+1)
# 첫 번째 동전 한 개만 사용했을 때의 경우의 수 구하기
dp[0]=1
for i in range(1, k + 1):
    if i % coin[0] == 0:
        dp[i] =1

# dp[n]=dp[n]+dp[n-coin]
# coin 종류 번호
for i in range(1,n):
    for j in range(coin[i],k+1):
        dp[j]+=dp[j-coin[i]]


print(dp[k])







