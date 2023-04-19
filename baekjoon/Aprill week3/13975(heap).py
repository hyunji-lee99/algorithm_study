# 모든 파일에 대해서 가장 크기가 작은 두 파일을 계속 합쳐주면 최소 나옴
# 우선순위 큐 쓰면 될 듯
import heapq
import sys
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    size=list(map(int, sys.stdin.readline().split(' ')))
    # 입력받은 size 배열을 heap으로 선언해줌(오름차순 정렬되고, 원소를 넣다 빼도 정렬을 계속 유지시켜주니까) 리턴값을 주는 게 아니라는 것 주의!
    heapq.heapify(size)
    ans=0
    while True:
        # 가장 작은 두 원소 pop
        a=heapq.heappop(size)
        b=heapq.heappop(size)
        # 두 원소 합친 비용 ans에 추가
        ans+=(a+b)
        # size에 아직 원소가 남아있을 경우
        if size:
            heapq.heappush(size, a+b)
        # size에 남은 원소가 없는 경우 -> 종료
        else:
            break
    print(ans)

