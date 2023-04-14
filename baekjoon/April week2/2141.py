import sys

n=int(sys.stdin.readline())

village=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
village.sort(key=lambda x:x[0])
start=village[0][0]
end=village[-1][0]
minvalue=1e9
minloc=1e9
while start<=end:
    mid=(start+end)//2
    # 우체국이 mid에 위치할 때 왼편 거리 합 구하기
    leftsum=0
    rightsum=0
    for i in range(n):
        if village[i][0]<mid:
            #leftsum+=((mid-village[i][0])*village[i][1])
            leftsum+=village[i][1]
        else:
            #rightsum+=((village[i][0]-mid)*village[i][1])
            rightsum+=village[i][1]
    # 왼쪽 거리 합이 오른쪽 거리 합보다 크면 왼쪽에 위치하는 것이 더 유리함
    if leftsum>rightsum:
        end=mid-1
    else:
        start=mid+1

    if minvalue>(leftsum+rightsum):
        minvalue=leftsum+rightsum
        minloc=mid
    elif minvalue==(leftsum+rightsum):
        minloc=min(minloc, mid)


print(minloc)