import sys

n=int(sys.stdin.readline())
first=list(sys.stdin.readline().strip())
list=list(list(sys.stdin.readline().strip()) for _ in range(n-1))

ans=0
for word in list:
    comp=first.copy()
    # 차이의 개수
    cnt=0
    for w in word:
        if w in comp:
            comp.remove(w)
        else:
            cnt+=1
    # word가 더 길 경우엔 cnt가 2 보다 작아야 하고, word가 더 짧은 경우엔 남은 comp의 길이가 2보다 작아야 한다.
    if cnt<2 and len(comp)<2:
        ans+=1

print(ans)

