# (x,y) -> area[y][x]로 판단하지 말자
n=int(input())
# dummy
A=[[0]*(n+1)]+[[0]+list(map(int, input().split(' '))) for _ in range(n)]

# d1, d2 ≥ 1,
# 1 ≤ x < x+d1+d2 ≤ N,
# 1 ≤ y-d1 < y < y+d2 ≤ N

# 완전탐색으로 x,y,d1,d2 구하기?
candidate=[]
for d1 in range(1, n):
    for d2 in range(1,n):
        for x in range(1,n):
            for y in range(1,n):
                if 1<=x<x+d1+d2<=n and 1<=y-d1<y<y+d2<=n:
                    candidate.append((x,y,d1,d2))

minvalue=1e9

for x,y,d1,d2 in candidate:
    area=[[0]*(n+1) for _ in range(n+1)]

    # 5번 선거구 채우기
    # 경계선
    for d_one in range(d1 + 1):
        area[x + d_one][y - d_one] = 5
        area[x + d2 + d_one][y + d2 - d_one] = 5
    for d_two in range(d2 + 1):
        area[x + d_two][y + d_two] = 5
        area[x + d1 + d_two][y - d1 + d_two] = 5

    # 경계선 안 쪽 채우기
    for i in range(x+1, x+d1+d2):
        start=False
        for j in range(1, n+1):
            #처음으로 5를 만나면 start
            if not start and area[i][j]==5:
                start=True
            # 이미 시작된 상태에서 5를 만나면 break
            elif start and area[i][j]==5:
                break
            elif start:
                area[i][j]=5

    # 1번 선거구
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if area[i][j]!=5:
                area[i][j] = 1

    # 2번 선거구
    for i in range(1, x + d2 + 1):
        for j in range(y + 1, n + 1):
            if area[i][j] != 5:
                area[i][j] = 2

    # 3번 선거구
    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if area[i][j] != 5:
                area[i][j] = 3

    # 4번 선거구
    for i in range(x + d2 + 1, n + 1):
        for j in range(y - d1 + d2, n + 1):
            if area[i][j] != 5:
                area[i][j] = 4


    one=0
    two=0
    three=0
    four=0
    five=0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if area[i][j]==1:
                one+=A[i][j]
            elif area[i][j]==2:
                two+=A[i][j]
            elif area[i][j]==3:
                three+=A[i][j]
            elif area[i][j]==4:
                four+=A[i][j]
            elif area[i][j]==5:
                five+=A[i][j]

    minv=min(one, two, three, four, five)
    maxv=max(one, two, three, four, five)

    minvalue=min(minvalue, maxv-minv)

print(minvalue)




