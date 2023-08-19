import sys

t=int(sys.stdin.readline())
# 성냥개비 개수별로 만들 수 있는 가장 작은 수
# 2~7
# numbers=['','','1','7','4','2','0','8']
numbers=[0,0,1,7,4,2,0,8]
# 가장 작은 수 구하기
#dp=['9999999999999999999']*(101)
dp=[sys.maxsize]*(101)
# dp init
for i in range(2,8):
    if i==6:
        # dp[i]='6'
        dp[i]=6
    else:
        dp[i]=numbers[i]
for idx in range(8,101):
    for j in range(2,8):
        # if int(dp[idx])>int(dp[idx-j]+numbers[j]):
            # dp[idx]=dp[idx-j]+numbers[j]
        dp[idx]=min(dp[idx], dp[idx-j]*10+numbers[j])

for _ in range(t):
    num=int(sys.stdin.readline())
    # 가장 큰 수 구하기
    largest=''
    # 홀수일 경우
    if num%2==1:
        largest+='7'
        largest+='1'*(num//2-1)
    else:
        # 짝수일 경우
        largest+='1'*(num//2)
    smallest=dp[num]
    print(smallest, largest)
