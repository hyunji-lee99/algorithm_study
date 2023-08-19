import sys

t=int(sys.stdin.readline())
numbers=[int(sys.stdin.readline()) for _ in range(t)]

fib=[[] for _ in range(41)]
fib[0]=[1,0]
fib[1]=[0,1]
for i in range(2,41):
    fib[i]=[fib[i-1][0]+fib[i-2][0], fib[i-1][1]+fib[i-2][1]]

for num in numbers:
    print(fib[num][0], fib[num][1])

