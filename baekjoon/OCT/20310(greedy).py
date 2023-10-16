import sys

numbers=list(sys.stdin.readline().strip())
zero, one = numbers.count('0')//2, numbers.count('1')//2

# 0은 뒤에서부터 지워짐 표시
for idx in range(len(numbers)-1,-1,-1):
    if zero<=0:
        break
    if numbers[idx]=='0':
        numbers[idx]=-1
        zero-=1
# 1은 앞에서부터 지워짐 표시
for idx in range(len(numbers)):
    if one<=0:
        break
    if numbers[idx]=='1':
        numbers[idx]=-1
        one-=1

for idx in range(len(numbers)):
    if numbers[idx]!=-1:
        print(numbers[idx], end='')