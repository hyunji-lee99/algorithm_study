import sys
import re
# $ 표시로 정규식 종료 표시를 해주거나, match가 아닌 fullmatch를 사용해야 문자열 전체가 해당 정규식을 만족하는지 알 수 있다.
p=re.compile('[A-F]?A+F+C+[A-F]?')
t=int(sys.stdin.readline())
for _ in range(t):
    compString=sys.stdin.readline().strip()
    m = p.fullmatch(compString)
    if m:
        print('Infected!')
    else:
        print('Good')
