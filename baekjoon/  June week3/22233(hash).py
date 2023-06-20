import sys


n,m=map(int, sys.stdin.readline().split(' '))
keywords=dict()
for _ in range(n):
    keyword=sys.stdin.readline().strip()
    keywords[keyword]=0


ans=n
for _ in range(m):
    posted_keywords=list(sys.stdin.readline().strip().split(','))
    for k in posted_keywords:
        if (k in keywords.keys()) and (keywords[k]==0):
            keywords[k]=1
            ans-=1
    print(ans)

# dict를 업데이트하면서, 남은 키워드의 개수를 동시에 카운팅하면 시간초과 발생하지 않음.