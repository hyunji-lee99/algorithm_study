# n, m : 한 줄에 연속된 나무의 수, 상근이가 집에 가져가야 하는 나무의 길이
import sys

n,m=map(int, sys.stdin.readline().strip().split(' '))
trees=list(map(int, sys.stdin.readline().split(' ')))

start=0
end=max(trees)
max=-1
while start<=end:
    # 기존에 int((start+end)//2) 때문에 시간초과 발생함
    # int() 함수의 시간복잡도가 추가되서 그런 듯(O(log n) 추정)
    # python에서 //은 정수 몫을 반환하므로 따로 int 형변환을 해 줄 필요가 없음
    mid=(start+end)//2
    #가져갈 수 있는 나무 길이 계산
    height=0
    for tree in trees:
        if tree>mid:
            height+=(tree-mid)

    # 이런 식으로 체크해주면 값이 딱 떨어지는 경우만 수행 가능함.
    # 조금 크게 가져갈 수 밖에 없는 경우는 해결할 수가 없음
    # start>end가 될 때까지 max값을 업데이트해주는 방식으로 풀어야 함
    # if height==m:
    #     print(mid)
    #     break

    if height<m:
        #height가 목표한 m보다 작으므로 mid값이 더 작아져야 함
        end=mid-1
    elif height>=m:
        # height가 목표한 m보다 크므로 mid값이 더 커져야 함
        start=mid+1
        if mid>max:
            max=mid

print(max)