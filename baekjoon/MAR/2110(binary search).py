import sys
n,c=map(int, sys.stdin.readline().split(' '))

house=[int(sys.stdin.readline()) for _ in range(n)]

# 이분탐색을 위한 sorting
# 각 집간의 거리를 가지고 이분탐색함.
house.sort()

# 최소값은 1, 최대값은 첫 집과 마지막 집의 거리
start=1
end=house[-1]-house[0]

ans=start
while start<=end:
    mid=(start+end)//2
    prev=house[0]
    cnt=1
    for i in range(1,n):
        # 현재 mid 값만큼 공유기 간의 거리를 가지려면 필요한 공유기 개수를 구함
        if (house[i]-prev)>=mid:
            cnt+=1
            prev=house[i]
    # cnt값이 공유기 제한 개수인 c보다 크거나 같으면, 공유기간 거리를 늘려야 함.
    if cnt>=c:
        ans=max(ans, mid)
        start=mid+1
    else:
        # cnt값이 c보다 작으면, 공유기간 거리를 줄여야 함
        end=mid-1

print(ans)
