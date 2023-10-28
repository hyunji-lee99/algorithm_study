import sys
import math

n,l=map(int, sys.stdin.readline().split(' '))

# 물 웅덩이
m=[]
for _ in range(n):
    s,e=map(int, sys.stdin.readline().split(' '))
    m.append([s,e])

m.sort()
ans=0
# 현재 널판지 최대 길이
cur=0
for idx in range(n):
    s,e=m[idx]
    # 현재 커버해야 하는 웅덩이 길이
    cover = e - s
    # 현재 웅덩이 시작 위치보다 널판지가 작게 있으면
    # _______
    #           s   e
    if cur<=s:
        tmp=math.ceil(cover/l)
        ans+=tmp
        cur=s+(tmp*l)
    # 현재 웅덩이 시작 위치보다 널판지가 크게 있으면
    # ----
    #   s  e
    elif cur>s:
        # 커버해야하는 길이가 크게 있는만큼 줄어든다
        rm_cover=cur-s
        cover-=rm_cover
        tmp=math.ceil(cover/l)
        ans+=tmp
        cur=cur+(tmp*l)

print(ans)
