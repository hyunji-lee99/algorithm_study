# 투 포인터
import sys

n=int(sys.stdin.readline())
ac=list(map(int, sys.stdin.readline().split(' ')))

start=0
end=n-1
minvalue=abs(ac[start]+ac[end])
resA=ac[start]
resB=ac[end]

while start<end:
    cal=ac[start]+ac[end]
    if abs(cal)<minvalue:
        resA=ac[start]
        resB=ac[end]
        minvalue=abs(cal)
    # cal값이 0보다 작으면 start값을 한 칸 오른쪽으로
    # 이유는? 양수라면 양수가 있을 확률이 있는 end를 -1, 음수라면 더 큰 값을 더해야하므로 start을 +1 해주면서 원하는 값을 찾습니다.
    # 즉, 0에 가까운 값을 찾기 위해서 음수하면 더 큰 값을 더해봐야 하고, 양수라면 더 작은 값을 더해봐야 하니까
    if cal<0:
        start+=1
    elif cal>0:
        end-=1
    else:
        break

print(resA, resB)