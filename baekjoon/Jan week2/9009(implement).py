import sys

n=int(sys.stdin.readline())

#피보나치 배열 만들기
fib=[0,1]

#가장 큰 n이 1000000000이므로, 피보나치 값이 1000000000보다 같거나 작은 경우까지만 구하면 됨
#첫 피보나치 수 구하는 데에 사용할 fib 배열의 인덱스와 피보나치 값
x1=0
x2=1
value=1
while(value<=1000000000):
    value=fib[x1]+fib[x2]
    fib.append(value)
    x1+=1
    x2+=1

#저장된 피보나치 배열에서 tmp보다 작거나 같은 수 중 가장 큰 값을 찾아서 tmp에서 빼주고, 나머지를 기준으로 같은 연산 반복. tmp이 0이 되면 끝
for i in range(n):
    tmp=int(sys.stdin.readline())
    result=[]
    while(tmp>0):
        #range 역순으로 쓰는 방식 주의
        for j in range(len(fib)-1,1,-1):
            if fib[j]<=tmp:
                t=fib[j]
                tmp -= t
                result.append(t)
    result.sort()
    for k in result:
        print(k,end=' ')
    #개행 처리
    print('')