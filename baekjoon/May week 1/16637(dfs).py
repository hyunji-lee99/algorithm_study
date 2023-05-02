# dfs를 이용한 재귀연산이 어려웠음
import sys

n=int(sys.stdin.readline())
exp=list(sys.stdin.readline().strip())

def calculate(a,b,op):
    if op=='*':
        return a*b
    elif op=='+':
        return a+b
    elif op=='-':
        return a-b

result=-1e9
def dfs(index, num):
    global result
    if index>n-1:
        result=max(num, result)
        return

    if index==0:
        op='+'
    else:
        op=exp[index-1]

    # 괄호 추가
    if index+2<n:
        br=calculate(int(exp[index]), int(exp[index+2]), exp[index+1])
        dfs(index+4, calculate(num, br, op))
    # 괄호 안묶음
    dfs(index+2, calculate(num, int(exp[index]), op))

dfs(0,0)

print(result)
