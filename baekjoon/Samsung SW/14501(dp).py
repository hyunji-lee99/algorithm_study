# dp dp dp dp dp ..
# dp 문제 많이 풀어보자!

n=int(input())
# dummy
tp=[()]
for i in range(n):
    t,p=map(int, input().split(' '))
    tp.append((t,p))

# i번째 날까지 일 했을 때 얻을 수 있는 최대수익을 저장해둠
dp=[0]*(n+1)

for i in range(1,n+1):
    # 퇴사일까지 수행가능한 업무인지 확인
    # n -> n+1로 수정
    # 예를 들어, 5일차에 소요시간이 3일이면 5,6,7일 3일 일할 수 있음
    if i+tp[i][0]<=(n+1):
        # i번 업무를 수행하므로 dp[i]에 수익 더하기
        dp[i]+=tp[i][1]
        # i번 업무를 수행하면 해당 업무가 걸리는 시간을 더해서 며칠부터 업무 수행이 가능한지 계산
        for j in range(i+tp[i][0],n+1):
            # i번 업무를 수행한 dp[j]값이 더 큰지, 수행하지 않은 dp[j]값이 더 큰지 계산
            # 즉, i번 업무를 거칠 것인지 말 것인지?
            dp[j]=max(dp[i],dp[j])

# 얻을 수 있는 최대 수익 출력
print(max(dp))

