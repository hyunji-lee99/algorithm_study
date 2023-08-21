import sys
from itertools import combinations

target=int(sys.stdin.readline())
# 버튼
# 0-9
# 숫자 버튼만 고장남
buttons=[True]*(10)
n=int(sys.stdin.readline())
if n>0:
    impossible=list(map(int, sys.stdin.readline().split(' ')))
else:
    impossible=[]

for imp in impossible:
    buttons[imp]=False

min_diff=sys.maxsize

def find_min_diff(arr):
    global min_diff
    for i in range(10):
        if buttons[i]:
            tmp=arr+str(i)
            min_diff=min(min_diff, abs(target-int(tmp))+len(tmp))
            if len(tmp)<6:
                find_min_diff(tmp)

find_min_diff('')
print(min(min_diff, abs(target-100)))


















