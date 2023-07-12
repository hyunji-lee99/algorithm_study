import sys

n=int(sys.stdin.readline())

point=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 신발끈 공식을 사용한다
def ex_product(p1, p2):
    global point
    v0=point[0]
    v1=point[p1]
    v2=point[p2]
    return 0.5*(v0[0]*v1[1]+v1[0]*v2[1]+v2[0]*v0[1]-v1[0]*v0[1]-v2[0]*v1[1]-v0[0]*v2[1])

ans=0
for i in range(1,n-1):
    ans+=ex_product(i,i+1)

print(abs(ans))

