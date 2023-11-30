import sys

input=sys.stdin.readline
n=int(input())
place=list(map(int, input().split(' ')))

# 누적합 구하기
# 계산할 때마다 탐색하는 것보다 미리 누적합을 구해놓고 사용
sumHoney=[]
sumHoney.append(place[0])
for i in range(1,n):
    sumHoney.append(sumHoney[i-1]+place[i])

# 벌 벌 꿀통
rightjar=0
for i in range(1,n-1):
    # 첫 번째 벌은 0번 인덱스 고정, 꿀통은 마지막 인덱스 고정
    # 두 번째 벌이 i번 인덱스에 위치하는 경우 얻을 수 있는 꿀의 합 중 최댓값 구함
    beeone=sumHoney[n-1]-sumHoney[0]-place[i]
    beetwo=sumHoney[n-1]-sumHoney[i]
    rightjar=max(rightjar, beeone+beetwo)

# 벌 꿀통 벌
# 양쪽 끝에 벌이 위치하고, 중간에 꿀통이 위치해야 함
# 장소의 개수 n이 홀수인지, 짝수인지에 따라 다름
# 홀수는 중간 요소가 1개지만 짝수는 중간 요소가 2개
middlejar=0
jar=n//2
if n%2==1:
    beeone=sumHoney[jar]-sumHoney[0]
    beetwo=sumHoney[n-1]-sumHoney[jar-1]-place[n-1]
    middlejar=max(middlejar, beeone+beetwo)
else:
    middlejar=max(middlejar, (sumHoney[jar]-sumHoney[0])+(sumHoney[n-1]-sumHoney[jar-1]-place[n-1]),
                  (sumHoney[jar-1]-sumHoney[0])+(sumHoney[n-1]-sumHoney[jar-2]-place[n-1]))

leftjar=0
# 꿀통 벌 벌
for i in range(1,n-1):
    # 두 번째 벌은 마지막 인덱스 고정, 첫 번째 벌이 i번 인덱스에 위치하는 경우 얻을 수 있는 꿀의 합 중 최댓값
    beetwo=sumHoney[n-1]-place[n-1]-place[i]
    beeone=sumHoney[i]-place[i]
    leftjar=max(leftjar, beeone+beetwo)

print(max(rightjar, middlejar, leftjar))
