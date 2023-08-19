import sys

n,k=map(int, sys.stdin.readline().split(' '))
students=list(map(int, sys.stdin.readline().split(' ')))

# 아이디어 도출이 어려웠음
# 원생들을 k개 조로 나누려면, 각 원생들간의 경계를 k-1개만큼 세울 수 있음
# 인접한 원생과 차이가 큰 k-1개를 빼고, 나머지 차이를 모두 더해주면 최소값
# 예를 들어,
# 5 3
# 1 3 5 6 10
# diff=[2,2,1,4]
# 정렬하면 [1,2,2,4]
# 차이가 큰 2(k-1)개 빼주고, 더하면 최소값 3
# => 차이가 가장 큰 6과 10 사이에 경계 하나, 다음으로 큰 3과 5 사이에 하나 경계를 세우는 것
# 1 3 / 5 6 / 10

diff=[]
for i in range(n-1):
    diff.append(students[i+1]-students[i])

diff.sort(reverse=True)
print(sum(diff[k-1:]))
