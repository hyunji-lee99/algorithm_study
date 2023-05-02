# 37%에서 틀림 -> 최장 접두사를 pre에 저장하는 방식이 매우 중요했음
# -> 다시 풀어볼 문제

import sys
from collections import OrderedDict

n=int(sys.stdin.readline())
words=[sys.stdin.readline().strip() for i in range(n)]
# 중복방지
# 단순하게 set을 사용하면, set 자체가 순서를 무시하기 때문에 기존 배열의 순서가 무너짐.
# OrderDict를 사용하자
words=list(OrderedDict.fromkeys(words))
n=len(words)
# enumrate
# 들어온 순서, 단어 순으로 기록
new_words=list(enumerate(words))
# words를 사전순으로 정렬함
new_words.sort(key=lambda x:x[1])

maxvalue=-1e9
length=[0]*(n)
# 인접한 단어끼리 탐색
for i in range(n-1):
    first=new_words[i][1]
    second=new_words[i+1][1]
    l=min(len(first), len(second))
    cnt=0
    for j in range(l):
        if first[j]!=second[j]:
            break
        else:
            cnt+=1
    # cnt가 maxvalue보다 큰 경우
    if cnt>maxvalue:
        maxvalue=cnt
    # length 배열에 각 인덱스별로 최대 접두사 길이 저장
    length[new_words[i][0]]=max(length[new_words[i][0]], cnt)
    length[new_words[i+1][0]] = max(length[new_words[i+1][0]], cnt)

# 최대 접두사 길이가 maxvalue인 요소를 찾은 상태인지 확인
first=0
for i in range(n):
    if first==0:
        # 최대 접두사 길이가 maxvalue인 요소 찾음
        if length[i]==maxvalue:
            pre=words[i][:maxvalue]
            first=1
            print(words[i])
    else:
        if length[i]==maxvalue and words[i][:maxvalue]==pre:
            print(words[i])
            break

