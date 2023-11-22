import sys

cash=int(sys.stdin.readline())
rate=list(map(int, sys.stdin.readline().split(' ')))

# 준현이가 가지는 수익
jcash=cash
jrate=0

for cur in rate:
    if jcash<=0:
        break
    if jcash >= cur:
        # 매수할 수 있는 만큼
        r = jcash // cur
        jcash -= (cur * r)
        jrate += r

# 성민이가 가지는 수익
scash=cash
srate=0
# 연속 상승 일수, 연속 하락 일수
increase=1
decrease=1
prev=rate[0]
for cur in rate:
    # 3일 이상 주가 상승, 매수 주가 존재한다면 전량 매도
    if increase >= 3 and srate > 0:
        scash+=(srate*cur)
        srate=0

    # 3일 이상 주가 하락, 매수할 수 있는 현금이 남았다면
    elif decrease >= 3 and scash > 0:
        r=scash//cur
        scash-=(cur*r)
        srate+=r

    if prev < cur:
        increase += 1
        decrease = 1
    elif prev > cur:
        increase = 1
        decrease += 1
    prev = cur


j=jcash+rate[13]*jrate
s=scash+rate[13]*srate

if j>s:
    print('BNP')
elif j<s:
    print('TIMING')
else:
    print('SAMESAME')
