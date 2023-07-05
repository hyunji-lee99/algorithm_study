import sys
from collections import deque

t=int(sys.stdin.readline())
for _ in range(t):
    height=list(map(int, sys.stdin.readline().split(' ')))
    # case number 제거
    cnum=height[0]
    height=height[1:]
    # 뒤로 물러선 횟수
    cnt=0
    line=deque()
    for h in height:
        # 자기 앞에 자신보다 키 큰 사람이 있는지 확인
        # any 문법 주의 - 조건을 만족하는 요소가 하나라도 있다면 True 반환
        # 참고) all은 모든 요소가 조건을 만족해야 True 반환
        # 자기보다 키 큰 사람이 있다면
        if any(num > h for num in line):
            for i in range(len(line)):
                if h<line[i]:
                    cnt += (len(line) - i)
                    line.insert(i,h)
                    break
        # 자기보다 키 큰 사람이 없다면
        else:
            line.append(h)
    print(str(cnum)+' '+str(cnt))

