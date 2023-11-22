import sys

n,k=map(int,sys.stdin.readline().split(' '))

import math


def change(num, k, ans):
    if num >= k:
        tmp = str(num % k) + ans
        return change(num // k, k, tmp)
    else:
        tmp = str(num) + ans
        return tmp


def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    change_number = change(n, k, '')
    stack = [change_number[0]]
    for i in range(1, len(change_number)):
        if change_number[i] == '0':
            if stack:
                # 스택에 남아있는 수가 소수인지 확인
                if isPrime(int(''.join(stack))):
                    answer += 1
                # 확인한 후에는 스택 비우기
                stack.clear()
        else:
            stack.append(change_number[i])
    if stack and isPrime(int(''.join(stack))):
        answer += 1
    return answer

print(solution(n,k))