import sys

n=int(sys.stdin.readline())
people=[]
for i in range(n):
    age, name = sys.stdin.readline().strip().split(' ')
    # 제대로 된 정렬을 위해서 숫자는 반드시 int형으로 변환
    # 문자열로 처리하면, '3'보다 '20'이 더 먼저 올 수 있음
    people.append((int(age),int(i), name))

people.sort()

for age, order, name in people:
    print(age, name)
