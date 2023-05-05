import sys

n,s=map(int, sys.stdin.readline().split(' '))
sequence=list(map(int, sys.stdin.readline().split(' ')))

# 완전탐색은 당연히 시간초과 발생
# length=1
# while length<=n:
#     for i in range(n-length+1):
#         if sum(sequence[i:i+length])>=s:
#             print(length)
#             sys.exit(0)
#     length+=1

# two-pointer 사용
start=0
end=0
minvalue=1e9
# 초기 부분합
sumvalue=sum(sequence[start:end+1])
while start<=end and end<n:
    # 현재 부분합이 s보다 작으면 end 인덱스릃 한 칸 오른쪽으로 이동시키고 sum+=sequence[end]
    if sumvalue<s:
        end += 1
        # end가 범위 넘어가는지 중간 체크 -> 안하면 sequence[n]을 처리해서 index error 발생함
        if end==n:
            break
        sumvalue += sequence[end]
    # 현재 부분합이 s 이상이면 현재 부분합 길이와 최소 부분합 길이 중 더 작은 값으로 업데이트하고
    # sum-=sequence[start]하고, start 인덱스를 한 칸 오른쪽으로 이동시킴
    elif sumvalue>=s:
        minvalue=min(minvalue, end-start+1)
        sumvalue -= sequence[start]
        start+=1

# minvalue가 1e9이면 부분합이 s 이상인 경우가 불가능하다는 뜻
if minvalue==1e9:
    print(0)
else:
    print(minvalue)