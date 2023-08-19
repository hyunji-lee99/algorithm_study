import sys
sys.setrecursionlimit(100000)

n,m=map(int, sys.stdin.readline().split())

# union-find 알고리즘을 사용
# 집합의 root 번호를 나타내는 배열 사용
root_set=[x for x in range(n+1)]

def find(num):
    global root_set
    if num!=root_set[num]:
        root_set[num] = find(root_set[num])
    return root_set[num]
    # if num==root_set[num]:
    #     return num
    # else:
    #     root_set[num]=find(root_set[num])

def union(x,y):
    global root_set
    x=find(x)
    y=find(y)
    root_set[y]=x


for _ in range(m):
    command, n1, n2=map(int, sys.stdin.readline().split())
    if command==0:
        # 두 번호가 속한 집합을 합친다.
        union(n1,n2)
    elif command==1:
        # 두 번호가 같은 집합에 속하는지 확인한다.
        if find(n1)==find(n2):
            print('YES')
        else:
            print('NO')
