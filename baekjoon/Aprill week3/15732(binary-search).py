# 이분탐색인 것을 캐치 못했음
import sys

n,k,d=map(int, sys.stdin.readline().split(' '))
box=[0]*(n+1)
rule=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(k)]


def count_dotori(box_number):
    global rule
    total_cnt=0
    for start, end, step in rule:
        # 각 규칙들을 기준으로
        # box_number가 start보다 작을 경우, 범위에 들어가는 도토리가 없음
        if box_number<start:
            cnt=0
        # start~end 사이에 들어갈 경우
        elif start<=box_number<end:
            cnt=(box_number-start)//step+1
        elif box_number>=end:
            cnt=(end-start)//step+1
        total_cnt+=cnt

    if total_cnt>=d:
        return True
    else:
        return False


start=1
end=n
ans=0
while start<=end:
    mid=(start+end)//2
    # 마지막 도토리를 담은 상자의 번호 mid일 때, 담을 수 있는 도토리 개수가 d개 이상이면 d개에 더 가까워질 수 있는지 확인하기 위해서 mid값을 작게 해봄
    if count_dotori(mid):
        ans=mid
        end=mid-1
    else:
        # d개 미만이면 mid값을 올려줘서 d개 이상으로 만들어줘야 함
        start=mid+1


print(ans)

