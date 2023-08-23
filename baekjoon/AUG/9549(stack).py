import sys
from collections import deque

n=int(sys.stdin.readline())
for _ in range(n):
    # 암호화된 문자열
    encode=list(sys.stdin.readline().strip())
    # 기존 문자열
    decode=list(sys.stdin.readline().strip())
    encode_numbers=[0]*(26)
    decode_numbers=[0]*(26)
    stack=deque()
    for idx in range(len(decode)):
        # 'a'의 아스키코드
        encode_numbers[ord(encode[idx])-97]+=1
        stack.append(encode[idx])
        decode_numbers[ord(decode[idx])-97]+=1

    if len(encode)==len(decode):
        if encode_numbers == decode_numbers:
            print('YES')
        else:
            print('NO')
        continue

    for i in range(len(decode),len(encode)):
        # 제일 앞 문자열 빼고 문자 개수 삭제
        encode_numbers[ord(stack.popleft())-97]-=1
        # 다음 문자열 넣고 문자 개수 추가
        stack.append(encode[i])
        encode_numbers[ord(encode[i])-97]+=1
        if encode_numbers==decode_numbers:
            print('YES')
            break
    else:
        print('NO')





