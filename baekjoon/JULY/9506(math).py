import sys
import math


while True:
    num=int(sys.stdin.readline())
    if num==-1:
        sys.exit(0)
    divisor=[]
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            divisor.append(i)
    # reversed 시간복잡도 O(1), sort 시간복잡도 O(nlogn)
    for div in reversed(divisor):
        divisor.append(num//div)

    if sum(divisor)==num-1:
        # 완전수
        print(str(num)+' = 1 + ', end='')
        print(*divisor, sep=' + ')
    else:
        print(str(num)+' is NOT perfect.')

