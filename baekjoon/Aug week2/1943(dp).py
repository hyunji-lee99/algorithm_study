import sys

for _ in range(3):
    n=int(sys.stdin.readline())
    coins=[]
    amount=0
    for _ in range(n):
        coin, num=map(int, sys.stdin.readline().strip().split(' '))
        coins.append([coin, num])
        amount+=coin*num
    # 총액이 홀수이면 똑같이 분배할 수 없으므로 0 출력하고 종료
    if amount%2==1:
        print(0)
        continue
    goal=amount//2
    dp=[1]+[0]*(goal)
    for coin, num in coins:
        for n in range(goal,coin-1, -1):
            if dp[n-coin]==1:
                for i in range(num):
                    if n+coin*i<=goal:
                        dp[n+coin*i]=1
                    else:
                        break
    if dp[-1]==1:
        print(1)
    else:
        print(0)
