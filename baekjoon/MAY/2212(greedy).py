# https://velog.io/@jkh9615/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-11000-%EA%B0%95%EC%9D%98%EC%8B%A4-%EB%B0%B0%EC%A0%95-Java-wskzqzk6
# 위 블로그 참고하여 풀었습니다

import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
sensor=list(map(int, sys.stdin.readline().split(' ')))
sensor.sort()

# 차이 배열 구하기
diff=[]
for i in range(n-1):
    diff.append(sensor[i+1]-sensor[i])
# 차이 배열 내림차순
diff.sort(reverse=True)

# k-1개만큼 구간을 뛰어넘을 수 있으므로 차이가 가장 큰 상위 k-1개 구간을 뛰어넘음
print(sum(diff[k-1:]))

