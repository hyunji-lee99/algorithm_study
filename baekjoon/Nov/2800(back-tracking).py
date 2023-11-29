import sys

arr=list(sys.stdin.readline().strip())
answer=set()

bracket=[]
stack=[]
# 괄호 쌍 구하기
for idx in range(len(arr)):
    if arr[idx]=='(':
        stack.append(idx)
    elif arr[idx]==')':
        open=stack.pop()
        bracket.append((open, idx))

visited=[False]*len(bracket)
arr_visited=[True]*len(arr)

# 백트래킹을 사용하자
# n은 현재 삭제할 괄호 번호
# cnt는 삭제된 괄호의 개수
def backtracking(n,cnt):
    # 삭제된 괄호의 개수가 0개 이상이라면 answer에 답 추가
    if n==len(bracket):
        if cnt>0:
            # arr_visited를 이용한 답 추가
            tmp = ''
            for i in range(len(arr_visited)):
                if arr_visited[i]:
                    tmp += arr[i]
            answer.add(tmp)
        return

    # 해당 괄호 삭제 안하는 경우
    backtracking(n+1, cnt)
    # 해당 괄호 삭제 하는 경우
    arr_visited[bracket[n][0]]=False
    arr_visited[bracket[n][1]]=False
    backtracking(n+1, cnt+1)
    arr_visited[bracket[n][0]]=True
    arr_visited[bracket[n][1]]=True


backtracking(0,0)

print(*sorted(list(answer)), sep='\n')
