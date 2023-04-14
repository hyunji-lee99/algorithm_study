import sys

n=int(sys.stdin.readline())
# 0단계 -> 4
# 1단계 -> 9
# 2단계 -> 25
# 3단계 -> 81
# (2^n+1)^2 규칙 찾음
print(pow(pow(2,n)+1,2))