n,m,h=map(int, input().split(' '))
# dummy 포함
ladder=[[0]*n for _ in range(h+1)]
for i in range(m):
    a,b=map(int, input().split(' '))
    ladder[a][b]=1

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



