import sys

hexagram=[]
for _ in range(5):
    line=list(sys.stdin.readline().strip())
    hexagram.append(line)

# A~L
visited=[0]*(13)
# x의 좌표
X=[]
# x의 개수
X_cnt=0
for i in range(5):
    for j in range(9):
        if hexagram[i][j]=='x':
            X.append((i,j))
            X_cnt+=1
        elif hexagram[i][j]=='.':
            pass
        else:
            visited[ord(hexagram[i][j])-65+1]=1


def calculate_hexagram():
    if (ord(hexagram[0][4])-65+1)+(ord(hexagram[1][3])-65+1)+(ord(hexagram[2][2])-65+1)+(ord(hexagram[3][1])-65+1)!=26:
        return False
    if (ord(hexagram[0][4])-65+1)+(ord(hexagram[1][5])-65+1)+(ord(hexagram[2][6])-65+1)+(ord(hexagram[3][7])-65+1)!=26:
        return False
    if (ord(hexagram[1][1])-65+1)+(ord(hexagram[1][3])-65+1)+(ord(hexagram[1][5])-65+1)+(ord(hexagram[1][7])-65+1)!=26:
        return False
    if (ord(hexagram[3][1])-65+1)+(ord(hexagram[3][3])-65+1)+(ord(hexagram[3][5])-65+1)+(ord(hexagram[3][7])-65+1)!=26:
        return False
    if (ord(hexagram[1][1])-65+1)+(ord(hexagram[2][2])-65+1)+(ord(hexagram[3][3])-65+1)+(ord(hexagram[4][4])-65+1)!=26:
        return False
    if (ord(hexagram[1][7])-65+1)+(ord(hexagram[2][6])-65+1)+(ord(hexagram[3][5])-65+1)+(ord(hexagram[4][4])-65+1)!=26:
        return False
    return True

# idx : 배열 X에 저장된 x가 위치한 idx번째 좌표
# cnt : 다른 알파벳으로 채워진 x의 개수
def DFS(idx, cnt):
    if cnt==X_cnt:
        # 모든 줄의 합이 26이면 hexagram 출력하고 프로그램 종료
        if calculate_hexagram():
            for hex in hexagram:
                print(*hex, sep='')
            sys.exit(0)
        # 아니라면 DFS return
        return

    for i in range(1,13):
        # 이미 채워진 알파벳이라면 다음 알파벳 체크
        if visited[i]==1:
            continue
        # 현재 알파벳으로 현재 idx에 해당하는 x의 위치를 채운다면
        visited[i]=1
        hexagram[X[idx][0]][X[idx][1]]=chr(65+i-1)
        DFS(idx+1, cnt+1)
        hexagram[X[idx][0]][X[idx][1]]='x'
        visited[i]=0

DFS(0,0)






