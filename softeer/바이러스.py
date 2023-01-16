import sys

k,p,n=sys.stdin.readline().split(' ')

k=int(k)
p=int(p)
n=int(n)

#범위가 10^8, 10^6까지 커지기 때문에, 매번 곱할 때마다 1000000007로 나눈 나머지로 계산해주면 됨.
#k*p*p*p*p...*p%1000000007 = (k*p%1000000007)*p%1000000007...
for i in range(n):
    k=(k*p)%1000000007

print(k)