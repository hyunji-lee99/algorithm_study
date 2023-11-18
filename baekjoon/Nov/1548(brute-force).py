# 세 수 x, y, z가 x+y>z, x+z>y, y+z>x의 관계를 만족
# N인 수열 B(b[0], b[1], ..., b[n-1])의 모든 b[i], b[j], b[k]가 삼각관계에 있으면 이 수열은 삼각 수열
# 수열 A가 주어졌을 때, 이 수열에서 적절히 몇 개의 원소를 빼서 이 수열을 삼각 수열로 만들려고 한다. 삼각 수열의 최대 길이를 구하는 프로그램

import sys

n=int(sys.stdin.readline())
B=list(map(int, sys.stdin.readline().split(' ')))


B.sort()

if n>2:
    result=2
    for start in range(n-3):
        end=start+2
        while end<n:
            if B[start]+B[start+1]>B[end]:
                result=max(result, end-start+1)
                end+=1
            else:
                break
    print(result)
else:
    print(n)
