n,m,h=map(int, input().split(' '))
# dummy 포함
# 실제론 1,..,n-1 열만 이용하더라도, 선택가능한 사다리를 탐색하는 과정에서 맨 끝 값 들의 계산을 용이하게 하기 위해 n+1로 두어야 함
ladder=[[0]*(n+1) for _ in range(h+1)]
for i in range(m):
    a,b=map(int, input().split(' '))
    ladder[a][b]=1

# python3에서 시간초과, pypy3에서 통과 -> i번 사다리가 i번으로 연결되는지 확인하는 search_ladder에서 시간을 줄여야 python3에서도 통과할듯
def search_ladder(index,ladder):
    height=1
    cur=index
    while height<=h:
        if cur==1:
            for i in range(height,h+1):
                if ladder[i][cur]==1:
                    cur+=1
                    height+=1
                    break
                else:
                    height+=1
        elif cur==n:
            for i in range(height,h+1):
                if ladder[i][cur-1]==1:
                    cur-=1
                    height+=1
                    break
                else:
                    height+=1
        else:
            for i in range(height, h+1):
                if ladder[i][cur-1]==1:
                    cur-=1
                    height+=1
                    break
                elif ladder[i][cur]==1:
                    cur+=1
                    height+=1
                    break
                else:
                    height+=1
    return cur

def isFinish(ladder):
    # i번 세로선의 결과가 i번인지 확인
    for i in range(1,n+1):
        if search_ladder(i,ladder)==i:
            continue
        else:
            return False
    # 결과가 모두 i번이면
    return True

# 사다리를 놓을 수 있는 곳 탐색하기

# def search_index(ladder):
#     candidate = []
#     for i in range(1, h + 1):
#         for j in range(1, n):
#             if ladder[i][j] == 0 and ladder[i][j - 1] == 0 and ladder[i][j + 1] == 0:
#                 candidate.append((i, j))
#     return candidate

# 시간초과 발생
# candidate1=search_index(ladder)
# for cy1,cx1 in candidate1:
#     copy_ladder1=[arr[:] for arr in ladder]
#     # 한 개 선택하고
#     copy_ladder1[cy1][cx1]=1
#     # 종료할 수 있는지 확인
#     if isFinish(copy_ladder1):
#         minvalue=min(minvalue, 1)
#     # 사다리 놓을 수 있는 위치 계산
#     candidate2=search_index(copy_ladder1)
#     for cy2,cx2 in candidate2:
#         copy_ladder2=[arr[:] for arr in copy_ladder1]
#         # 하나 더 선택하고(두 개 선택하고)
#         copy_ladder2[cy2][cx2]=1
#         if isFinish(copy_ladder2):
#             minvalue=min(minvalue,2)
#         candidate3=search_index(copy_ladder2)
#         for cy3, cx3 in candidate3:
#             copy_ladder3=[arr[:] for arr in copy_ladder2]
#             copy_ladder3[cy3][cx3]=1
#             if isFinish(copy_ladder3):
#                 minvalue=min(minvalue,3)

# dfs로 풀어보자
minvalue=4
def dfs_ladder(cnt):
    global minvalue
    if isFinish(ladder):
        minvalue=min(minvalue, cnt)
        return
    # cnt가 3인데 isFinish에서 걸리지 않았다는 건 3 이하론 불가능한 것, cnt가 minvalue보다 같거나 크다면 체크할 필요가 없음
    if cnt==3 or cnt>=minvalue:
        return
    for i in range(1,h+1):
        for j in range(1,n):
            if ladder[i][j]==0 and ladder[i][j+1]==0 and ladder[i][j-1]==0:
                # 사다리 놓을 곳 하나씩 탐색
                ladder[i][j]=1
                dfs_ladder(cnt+1)
                # 모두 탐색하고 나면 사다리 제거
                ladder[i][j]=0


dfs_ladder(0)

if minvalue==4:
    print(-1)
else:
    print(minvalue)

