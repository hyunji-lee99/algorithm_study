import sys

# 칭호의 개수 n, 캐릭터의 개수 m
n,m=map(int, sys.stdin.readline().split(' '))

# 칭호의 종류와 상한값 level
level=[]
for i in range(n):
    l, v=sys.stdin.readline().split(' ')
    level.append((l, int(v)))


def search_level(c):
    global level
    # n=최대 10^5, m=최대 10^5 -> 완전 탐색하면 시간초과 발생함
    # for le in level:
    #     if c<=le[1]:
    #         return le[0]

    # 이분탐색을 활용하자
    start=0
    end=n-1
    result=''
    while start<=end:
        mid=(start+end)//2
        # level mid값이 c보다 클 경우, 더 작은 mid값이 존재하는지 확인
        if level[mid][1]>=c:
            result=level[mid][0]
            end=mid-1
        else:
            start=mid+1
    return result

for i in range(m):
    charecter=int(sys.stdin.readline())
    print(search_level(charecter))

