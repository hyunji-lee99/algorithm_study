# 이분탐색
import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())

ans=0
left=0
right=n*n
while left<=right:
    mid=(left+right)//2
    # 각 행별로 mid값보다 작거나 같은 수 계산
    cnt=0
    for i in range(1, n+1):
        # i행은 i의 배수의 집합이므로
        # mid를 행을 나타내는 i로 나눠주면 i행에서 몇 번째 위치하는지 알 수 있음
        # i행의 최댓값보다 mid//i가 크다면 n을 더해줌
        cnt+=min(n, mid//i)
        # i가 mid보다 커지면 해당 i행의 값이 모두 mid보다 커지므로 개수를 세어줄 필요가 없음
        if i>mid:
            break
    # mid보다 작은 수의 개수가 k보다 크거나 같다면 mid값을 줄여야 함
    if cnt>=k:
        ans=mid
        right=mid-1
    # mid보다 작은 수의 개수가 k보다 작거나 같다면 mid값을 늘려야 함.
    else:
        left=mid+1


print(ans)