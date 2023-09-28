import sys
from itertools import combinations

n,k=map(int, sys.stdin.readline().strip().split(' '))
# (a,n,t,i,c) 5글자를 포함할 수 있지 않으면 아무런 단어도 말할 수 없다
if k<5:
    print(0)
    sys.exit(0)

# 선택된 글자
# 소문자 a의 아스키 코드 97
selected=[0]*26
selected[ord('a')-97]=1
selected[ord('n')-97]=1
selected[ord('t')-97]=1
selected[ord('i')-97]=1
selected[ord('c')-97]=1
k-=5
# 필요한 글자
required=set()
# 단어들
words=[]
for _ in range(n):
    word=list(sys.stdin.readline().strip())
    words.append(word)
    # 앞 뒤 기본 단어 빼고 탐색
    for i in range(4, len(word)-4):
        if selected[ord(word[i])-97]==0:
            required.add(word[i])

ans=0
# 만약 k가 전체 글자 수보다 크다면 모두 가능
if k>len(required):
    combinations_char=[]
    combinations_char.append(required)
else:
    combinations_char=list(combinations(required, k))
for combi in combinations_char:
    # 선택되었다 표시
    for c in combi:
        selected[ord(c)-97]=1
    # 가능한 단어의 수 구하기
    num=0
    for word in words:
        isPossible = True
        for i in range(4, len(word)-4):
            if selected[ord(word[i])-97]==0:
                isPossible=False
                break
        if isPossible:
            num+=1
    ans=max(ans, num)
    # 선택 해제
    for c in combi:
        selected[ord(c)-97]=0

print(ans)




