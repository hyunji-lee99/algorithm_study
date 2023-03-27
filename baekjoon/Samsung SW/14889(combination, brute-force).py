n=int(input())
# 이차원 배열 한 줄로 입력받기
s=[list(map(int, input().split(' '))) for _ in range(n)]

# 0부터 n-1까지 번호 부여
member=[i for i in range(n)]

# member 중 n/2명 뽑는 조합
r=n//2
combinations=[]
def combination(index, arr):
    # 일종의 dfs
    # 원하는 수(n/2==r)만큼 원소를 뽑은 경우
    if len(arr)==r:
        combinations.append(arr)
        return
    # 원하는 수에 도달하지 못한 경우
    for i in range(index,len(member)):
        combination(i+1, arr+[member[i]])

combination(0,[])

start_score=0
link_score=0
minvalue=1e9
# combination 대칭관계이므로 n/2까지만 조회
for idx in range(len(combinations)//2):
    start=combinations[idx]
    link=combinations[len(combinations)-idx-1]
    # start팀 능력치 구하기
    for i in range(r-1):
        for j in range(i+1,r):
            start_score+=(s[start[i]][start[j]]+s[start[j]][start[i]])
    # link팀 능력치 구하기
    for i in range(r-1):
        for j in range(i+1,r):
            link_score+=(s[link[i]][link[j]]+s[link[j]][link[i]])
    minvalue=min(minvalue, abs(start_score-link_score))
    # start_score, link_score는 케이스 하나 끝날 때마다 초기화
    start_score=0
    link_score=0

print(minvalue)
