
n,m=map(int, input().split(' '))

area=[]
for i in range(n):
    tmp=list(map(int, input().split(' ')))
    area.append(tmp)

# 빈 칸, 바이러스 위치 인덱스
blank=[]
virus=[]
for i in range(n):
    for j in range(m):
        if area[i][j]==0:
            blank.append((i,j))
        elif area[i][j]==2:
            virus.append((i,j))
def spread_virus():
    # 진짜 area, virus는 건들지말고, copy해서 사용
    # 2차원 배열은 단순 copy나 [:] 형식은 copyarea가 바뀌면 area도 바뀌는 결과가 나옴(1차원 배열 복사하듯이 해서 틀린 값 나왔음)
    # 2차원 배열의 얇은 복사는 [arr[:] for arr in area] 형식으로
    # 라이브러리 사용이 가능하다면 from copy import deepcopy 사용
    copyarea=[arr[:] for arr in area]
    copyvirus = [arr[:] for arr in virus]
    visitied=[[0]*m for _ in range(n)]
    visitied[copyvirus[0][0]][copyvirus[0][1]]=1
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    while copyvirus:
        cury,curx=copyvirus.pop(0)
        for dir in directions:
            dy=cury+dir[1]
            dx=curx+dir[0]
            # 범위 안에 해당하면서, 방문한 적 없고, 빈 칸인 경우
            if 0<=dy<n and 0<=dx<m and visitied[dy][dx]==0 and copyarea[dy][dx]==0:
                copyvirus.append((dy,dx))
                visitied[dy][dx]=1
                copyarea[dy][dx]=2
    # 바이러스를 모두 퍼트린 후의 안전 영역
    safezone=[(i,j) for i in range(n) for j in range(m) if copyarea[i][j]==0]
    return len(safezone)


ans=0
#벽 세울 빈칸 정하기
for i in range(len(blank)-2):
    for j in range(i+1,len(blank)-1):
        for k in range(j+1,len(blank)):
            one=blank[i]
            two=blank[j]
            three=blank[k]
            # 선택한 벽 세우기
            area[one[0]][one[1]]=1
            area[two[0]][two[1]] = 1
            area[three[0]][three[1]] = 1
            # bfs 이용해서 바이러스 퍼트리고, 안전영역 구하고, 최대값 갱신
            ans=max(ans, spread_virus())
            # 선택한 벽 다시 해제
            area[one[0]][one[1]] = 0
            area[two[0]][two[1]] = 0
            area[three[0]][three[1]] = 0

print(ans)





