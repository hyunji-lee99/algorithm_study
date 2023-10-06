import sys

t=int(sys.stdin.readline())
for _ in range(t):
    days=int(sys.stdin.readline())
    prices=list(map(int, sys.stdin.readline().split(' ')))
    max_price=0
    profit=0
    for d in range(days-1,-1,-1):
        if prices[d]>max_price:
            max_price=prices[d]
        elif prices[d]<max_price:
            profit+=(max_price-prices[d])
    print(profit)

