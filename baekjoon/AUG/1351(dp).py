import sys

n,p,q=map(int, sys.stdin.readline().split(' '))
# A=[0]*(n+1)
# A[0]=1
# for i in range(1,n+1):
#     A[i]=A[i//p]+A[i//q]

A={}
A[0]=1
def recursion_find_An(num):
    if num in A.keys():
        return A[num]
    A[num]=recursion_find_An(num//p)+recursion_find_An(num//q)
    return A[num]

recursion_find_An(n)
print(A[n])