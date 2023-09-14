import sys

n=int(sys.stdin.readline())
# 전체 기둥이 몇 번째 인덱스까지 있는지
maxL=-1e9
# 가장 높은 기둥 높이
maxH=-1e9
# 가장 높은 기둥 높이의 제일 뒤쪽 인덱스
maxIndex=0
heights=[]
for _ in range(n):
    l,h=map(int, sys.stdin.readline().strip().split(' '))
    heights.append((l,h))
    if l>maxL:
        maxL=l
    if h>=maxH:
        maxH=h
        maxIndex=l

size=[0]*(maxL+1)
for l,h in heights:
    size[l]=h

left_ans=0
left_cur_max=0
for idx in range(maxIndex+1):
    if size[idx]>left_cur_max:
        left_cur_max=size[idx]
    left_ans+=left_cur_max

right_ans=0
right_cur_max=0
for idx in range(maxL,maxIndex,-1):
    if size[idx]>right_cur_max:
        right_cur_max=size[idx]
    right_ans+=right_cur_max

print(left_ans+right_ans)
