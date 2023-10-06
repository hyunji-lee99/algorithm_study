import sys
from bisect import bisect_left

n,m=map(int, sys.stdin.readline().split(' '))
level_info=[]
rate_info=[]
for _ in range(n):
    l, r = sys.stdin.readline().strip().split(' ')
    level_info.append(l)
    rate_info.append(int(r))

for _ in range(m):
    rate=int(sys.stdin.readline())
    # 해당 rate가 어느 범위에 해당하는지 이분탐색으로 탐색한다.
    # 단순 for문을 이용해서 탐색할 경우 최악의 경우 모든 캐릭터의 레벨을 파악하는 데에 10^5 * 10^5 시간복잡도가 발생하여 시간초과가 날 수 있다.
    # 직접 구현
    # start, end =0, n-1
    # result=''
    # while start<=end:
    #     mid=(start+end)//2
    #     # mid번째 레벨이 rate보다 크거나 같다면, 더 작은 레벨을 만족하는지 확인
    #     if rate_info[mid]>=rate:
    #         end=mid-1
    #         result=level_info[mid]
    #     else:
    #         start=mid+1
    # print(result)

    # bisect 라이브러리 사용
    rl=bisect_left(rate_info, rate)
    print(level_info[rl])
