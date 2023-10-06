import sys
from collections import deque

n=int(sys.stdin.readline())
buildings=[int(sys.stdin.readline()) for _ in range(n)]

# 각 관리인이 볼 수 있는 빌딩의 개수
ans=[0]*n

stack=deque()
stack.append((buildings[-1], n-1))
for i in range(n-2,-1,-1):
    # stack의 top부터 시작해서 현재 빌딩의 위치보다 작은 빌딩 pop하고 ans 배열에 pop된 개수만큼 추가
    # ans 배열에 해당 빌딩의 번호에서 볼 수 있었지만, 해당 빌딩보다 작아서 pop된 개수도 추가해줌
    pop_number=0
    while stack and stack[-1][0]<buildings[i]:
        height, num=stack.pop()
        if ans[num]>0:
            pop_number+=ans[num]
        pop_number+=1
    ans[i]=pop_number
    # 자신보다 작은 건물 모두 pop한 뒤에 자신 추가
    stack.append((buildings[i], i))

print(sum(ans))