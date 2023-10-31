import sys

n=int(sys.stdin.readline())
ans=0
for _ in range(n):
    checking_string=sys.stdin.readline().strip()
    # 문자열의 길이가 1이면 무조건 그룹 단어
    if len(checking_string)==1:
        ans+=1
        continue
    prev=checking_string[0]
    visited=set()
    visited.add(checking_string[0])
    for i in range(1,len(checking_string)):
        cur=checking_string[i]
        # 이전 문자와 다른 새로운 문자가 나왔는데 이미 방문한 문자라면 그룹 단어가 아니다
        if prev!=cur and cur in visited:
            break
        prev=cur
        visited.add(cur)
    else:
        ans+=1

print(ans)