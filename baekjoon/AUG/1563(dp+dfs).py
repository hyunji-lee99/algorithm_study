import sys
sys.setrecursionlimit(10**5)

n=int(sys.stdin.readline())

dp=[[[-1]*3 for _ in range(4)] for _ in range(n+1)]
def find_case(length, late, absent):
    global n
    if late>=2 or absent>=3:
        return 0
    if length==n:
        return 1
    if dp[length][late][absent]==-1:
        dp[length][late][absent]=(find_case(length+1, late, 0)
                +find_case(length+1, late+1, 0)
                +find_case(length+1, late, absent+1))%1000000
        return dp[length][late][absent]
    else:
        return dp[length][late][absent]

print(find_case(0,0,0))



