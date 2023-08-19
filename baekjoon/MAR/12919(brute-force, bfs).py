# 두 가지 연산만 가능
# 1. 문자열의 뒤에 A를 추가한다.
# 2. 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
# s->t로 변경가능한지 판단해라



import sys
from collections import deque
from collections import Counter

s=sys.stdin.readline().strip()
t=sys.stdin.readline().strip()

# s-> t로 변경하는 방식은 시간초과 발생함 최악의 경우 2^50까지 완전탐색해야하기 때문

# counter=Counter(t)
# # a,b의 개수
# na=counter['A']
# nb=counter['B']
#
# queue=deque()
# queue.append(s)
# visited=[]
# while queue:
#     cur=queue.popleft()
#     if len(cur)>len(t):
#         print(0)
#         break
#
#     cur_counter=Counter(cur)
#     cur_na=cur_counter['A']
#     cur_nb=cur_counter['B']
#
#     # 1번 연산 가능한지?
#     if cur_na+1<=na:
#         appendA = cur + 'A'
#         if appendA == t:
#             print(1)
#             break
#         else:
#             if appendA not in visited:
#                 queue.append(appendA)
#                 visited.append(appendA)
#
#     # 2번 연산 가능한지?
#     # 문자열 뒤집기 연산 주의
#     if cur_nb+1<=nb:
#         appendB = cur + 'B'
#         appendBreversed=appendB[::-1]
#         if appendBreversed == t:
#             print(1)
#             break
#         else:
#             if appendBreversed not in visited:
#                 queue.append(appendBreversed)
#                 visited.append(appendBreversed)
# else:
#     print(0)

# t-> s로 적절하게 삭제하는 방식으로 탐색해야 함

queue=deque()
queue.append(t)
while queue:
    cur=queue.popleft()
    # cur=''인 경우, cur[-1] 접근했을 때 인덱스 에러 발생
    if len(cur)<=0:
        continue

    if cur == s:
        print(1)
        break
    # 연산 1번을 취소하는 방식이 가능한지?
    if cur[-1]=='A':
        removeA=cur[:-1]
        queue.append(removeA)

    # 연산 2번을 취소하는 방식이 가능한지?
    reverseCur=cur[::-1]
    if reverseCur[-1]=='B':
        removeB=reverseCur[:-1]
        queue.append(removeB)
else:
    print(0)

