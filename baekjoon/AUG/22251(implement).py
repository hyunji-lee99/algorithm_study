import sys

# N층까지 존재
# K 자리 수 디스플레이 표현
# 최대 P개의 LED 반전
# 현재 X층에 멈춰있음
N,K,P,X=map(int, sys.stdin.readline().split(' '))

# LED를 배열로 표현
numbers=[ # 0 1 2 3 4 5 6 7 8 9
    [True, True,True,False,True,True,True],
    [False,False,True,False,False,True,False],
    [True, False,True,True,True,False,True],
    [True,False,True,True,False,True,True],
    [False, True,True,True,False,True,False],
    [True,True,False,True,False,True,True],
    [True,True,False,True,True,True,True],
    [True,False,True,False,False,True,False],
    [True,True,True,True,True,True,True],
    [True,True,True,True,False,True,True]
]

# 정수를 받아서 numbers 배열 형식으로 변환하는 함수
def change_to_arr(num):
    global numbers
    cur = []
    mod = num
    exp = K - 1
    while mod > 0:
        div = pow(10, exp)
        cur.append(numbers[mod // div])
        mod %= div
        exp -= 1
    # 0으로 끝나는 수 처리
    while exp>=0:
        cur.append(numbers[0])
        exp-=1
    return cur

# 두 배열의 차이의 개수를 구함
def diffNumber(arr1, arr2):
    diff=0
    for i in range(len(arr1)):
        for j in range(7):
            if arr1[i][j]!=arr2[i][j]:
                diff+=1
    return diff

ans=0
curX=change_to_arr(X)
for num in range(1, N+1):
    numArr=change_to_arr(num)
    diff=diffNumber(curX, numArr)
    if 1<=diff<=P:
        ans+=1

print(ans)