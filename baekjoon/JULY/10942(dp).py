import sys

# 숫자의 개수
n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split(' ')))
# dummy
numbers.insert(0,0)
# 질문의 개수
m=int(sys.stdin.readline())


dp=[[False]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i]=True

for i in range(1, n):
    if numbers[i]==numbers[i+1]:
        dp[i][i+1]=True


for i in range(3,n+1):
    for j in range(1,i-1):
        if numbers[i]==numbers[j] and dp[j+1][i-1]:
            dp[j][i]=True


for _ in range(m):
    s,e=map(int, sys.stdin.readline().split(' '))
    # 시간 초과 코드(최악의 경우 10^6*10^3)
    # check=numbers[s:e+1]
    # for i in range(len(check)//2):
    #     if check[i]==check[len(check)-i-1]:
    #         continue
    #     else:
    #         print(0)
    #         break
    # else:
    #     print(1)
    if dp[s][e]:
        print(1)
    else:
        print(0)




