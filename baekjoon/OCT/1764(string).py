import sys

n,m=map(int, sys.stdin.readline().split(' '))

count={}
for _ in range(n+m):
    name=sys.stdin.readline().strip()
    try:
        count[name]+=1
    except:
        count[name]=1

ans=[]
numberOfAns=0
for name, cnt in count.items():
    if cnt==2:
        ans.append(name)
        numberOfAns+=1

ans.sort()
print(numberOfAns)
print(*ans, sep='\n')

# arr1 & arr2 -> arr1, arr2의 공통 요소 추출 가능