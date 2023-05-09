import sys
import math

ap=int(sys.stdin.readline())/100
bp=int(sys.stdin.readline())/100

# 1-(A,B팀 모두 소수가 아닌 득점을 할 경우)
# 득점할 수 있는 모든 점수 경우의 수
notprimenumber=[0,1,4,6,8,9,10,12,14,15,16,18]
# A,B팀 모두 소수가 아닌 득점을 할 경우의 확률
pnp=0
def combination(r):
    #18Cr을 구하는 함수
    # math.comb(n,r), math.perm(n,r) (순열, 조합의 개수를 알려주는 함수지만, python 3.8 이상만 가능함)
    # math.factorial을 이용해서 순열공식 구현해서 품
    return math.factorial(18)/(math.factorial(18-r)*math.factorial(r))

# 득점할 확률이 a이고, 18개 중 4개의 득점을 할 확률 = 18C4 * a^4 * (1-a)^14
for i in notprimenumber:
    for j in notprimenumber:
        # 18Ci*pow(ap, i)*pow(1-ap, 18-i)*18Cj*pow(bp, j)*pow(1-bp, 18-j)
        pnp+=combination(i)*pow(ap, i)*pow(1-ap, 18-i)*combination(j)*pow(bp,j)*pow(1-bp, 18-j)


print(1-pnp)
