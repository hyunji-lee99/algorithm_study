import sys

t=int(sys.stdin.readline())

def calculate(express):
    if ' ' in express:
        express=express.replace(' ','')
    return eval(express)

def combination(num, arr):
    global n, ans
    if num==n:
        if calculate(arr)==0:
            ans.append(arr)
        return
    combination(num+1, arr+'+'+str(num+1))
    combination(num+1, arr+'-'+str(num+1))
    combination(num+1, arr+' '+str(num+1))

for _ in range(t):
    n=int(sys.stdin.readline())
    ans=[]
    combination(1, '1')
    ans.sort()
    for a in ans:
        print(a)
    print('')














