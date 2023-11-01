import sys
def factorial(n):
    if n>1:
        return (n*factorial(n-1))
    else:
        return 1

t=int(sys.stdin.readline())
for _ in range(t):
    n,m=map(int, sys.stdin.readline().split(' '))
    # m개 다리 중에 n개를 뽑는 경우의 수
    ans=factorial(m)//(factorial(m-n)*factorial(n))
    print(ans)

# itertools의 combinations의 경우 nCr 기준 시간복잡도가 n! / r! / (n - r)! 이므로, 숫자가 조금만 커져도 오류가 날 가능성이 있다!