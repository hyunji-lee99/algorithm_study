import sys

m,n,k=map(int, sys.stdin.readline().split(' '))
# 개행 문자 처리 필수
secret=list(sys.stdin.readline().strip().split(' '))
button=list(sys.stdin.readline().strip().split(' '))
# 문자 배열을 join으로 하나의 문자열로 합쳐줌
secret=''.join(secret)
button=''.join(button)
if secret in button:
    print('secret')
else:
    print('normal')