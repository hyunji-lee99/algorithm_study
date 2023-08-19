import sys

n,m=map(int, sys.stdin.readline().split(' '))
numbers=list(map(int, sys.stdin.readline().split(' ')))
ans=0
end=0
cur=0
# 투 포인터
for start in range(n):
    # 일종의 완전 탐색 방식 -> pypy에서만 패스
    # cur_sum = numbers[start]
    # if cur_sum == m:
    #     ans += 1
    # for end in range(start + 1, n):
    #     if cur_sum >= m:
    #         break
    #     cur_sum = cur_sum + numbers[end]
    #     if cur_sum == m:
    #         ans += 1
    while cur<m and end<n:
        cur+=numbers[end]
        end+=1
    if cur==m:
        ans+=1
    cur-=numbers[start]

print(ans)






