N,L=map(int, input().split(' '))
area=[list(map(int, input().split(' '))) for _ in range(N)]

ans=0
def search_way(arr):
    # arr는 지나갈 수 있는 길인지 확인해야 하는 배열
    slopes=[0]*N
    visited=[0]*N
    # 현재 경사로의 높이
    cur=arr[0]
    for i in range(1,N):
        if arr[i]==cur:
            continue
        elif (arr[i]-cur)==1:
            # 새로 검사하는 값이 cur값보다 1 큰 경우
            # 더 작은 부분의 위치에서 L만큼 균등한 높이를 가지는 공간이 있는지 체크
            checkL=0
            for idx in range(i-1,-1,-1):
                # 중간에 L을 만족하면 break
                if checkL==L:
                    break
                if arr[idx]==cur and slopes[idx]==0:
                    checkL+=1
                else:
                    break
            # 균동한 높이를 가지는 공간이 있음
            if checkL==L:
                # 현재 검사하는 높이가 arr[i] 값이 됨
                cur=arr[i]
                # 경사로 설치한 것 기록
                for j in range(i-1,i-1-L,-1):
                    slopes[j]=1
            else:
                # 통행 불가능
                return False
        elif (cur-arr[i])==1:
            # 새로 검사하는 값이 cur값보다 1 작은 경우
            checkL=0
            for idx in range(i,N):
                if checkL == L:
                    break
                if arr[idx]==arr[i] and slopes[idx]==0:
                    checkL+=1
                else:
                    break
            if checkL==L:
                cur=arr[i]
                for j in range(i, i+L):
                    slopes[j]=1
            else:
                # 통행 불가능
                return False
        else:
            # 값이 같거나 차이가 1이 아닌 경우
            return False
    return True


# 행 기준 탐색
for arr in area:
    if search_way(arr):
        ans+=1

# 전치행렬
area=list(zip(*area))
# 열 기준 탐색
for arr in area:
    if search_way(arr):
        ans+=1

print(ans)

