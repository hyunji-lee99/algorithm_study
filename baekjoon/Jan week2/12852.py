#dp
#dp
import sys
n=int(sys.stdin.readline())

#dp 테이블 생성
dp=[[0,[]] for _ in range(n+1)]

#n이 1인 경우, 초기화
dp[1][0]=0
dp[1][1]=[1]

#각 숫자별로 연산 최솟값 저장
for i in range(2,n+1):
    #3번째 연산(1을 뺀다)
    #현재 i보다 1 작은 숫자의 연산 최솟값에 1을 빼는 연산 횟수를 더해서 +1
    dp[i][0]=dp[i-1][0]+1
    dp[i][1]=dp[i-1][1]+[i]

    #2로 나누어지는 경우
    if i%2==0:
        #연산 전의 수의 연산 최솟값에 2로 나누는 연산 횟수 1 추가한 값이 기존의 연산 횟수보다 더 적은지 확인
        if dp[i][0]>dp[i//2][0]+1:
            dp[i][0]=dp[i//2][0]+1
            dp[i][1]=dp[i//2][1]+[i]
    #3으로 나누어지는 경우
    if i%3==0:
        if dp[i][0]>dp[i//3][0]+1:
            dp[i][0]=dp[i//3][0]+1
            dp[i][1]=dp[i//3][1]+[i]


#n의 최소 연산 횟수 출력
print(dp[n][0])
#n의 연산 순서 출력
#reversed 메소드
dp_order_reverse=list(reversed(dp[n][1]))
for x in dp_order_reverse:
    #print의 end 파라미터로 디폴트값인 개행연산자 바꿔줄 수 있음
    print(x,end=" ")
