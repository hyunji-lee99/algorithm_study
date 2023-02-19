# n : 테스트케이스 개수
# 시간초과
import sys
from collections import Counter

n=int(sys.stdin.readline())
for i in range(n):
    encryp=sys.stdin.readline().strip()
    nonencryp=sys.stdin.readline().strip()
    nonencryp_counter=Counter(nonencryp)
    #비암호화 문자열과 길이가 같은 암호화 문자열 substring의 Counter가 일치할 경우 print YES
    nonencryp_length=len(nonencryp)
    encryp_length=len(encryp)
    for j in range(encryp_length-nonencryp_length+1):
        substring=encryp[j:j+nonencryp_length]
        substring_counter=Counter(substring)
        if substring_counter==nonencryp_counter:
            print('YES')
            break
    else:
        print('NO')



