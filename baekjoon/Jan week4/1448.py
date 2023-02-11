#삼각형이 되려면, 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 작아야 함
import sys
#combination으로 3개를 선택하는 경우를 완전탐색하면 메모리초과가 발생함
#내림차순으로 정렬한 후, 가장 큰 값을 기준으로 삼각형이 만들어지는 경우의 수를 발견하면 출력하면 됨.
#단, 3중 for문으로 완전 탐색하는 것은 시간초과 발생
#연달아 붙어있는 3개의 수를 검사했을 때, 불가능하다면 더 작은 다른 수를 더하는 것은 당연히 불가능한 것을 이용
#예를 들어, line=[20,7,6,5,4]일 때, 20 7 6을 검사했을 때 불가능하므로 20 7 5, 20 7 4, 20 6 5,..등은 모두 불가능해지므로
#그대로 한 칸씩 옮겨서 7,6,5를 검사하면 됨.

from itertools import combinations

n=int(sys.stdin.readline())

line=[]
for i in range(n):
    tmp=int(sys.stdin.readline())
    line.append(tmp)

line.sort(reverse=True)

for i in range(0,len(line)-2):
    if line[i]<line[i+1]+line[i+2]:
        print(line[i]+line[i+1]+line[i+2])
        break
else:
    print(-1)

# 3중 for문 -> 시간초과
# for i in range(0,len(line)-2):
#     for j in range(i+1,len(line)-1):
#         for k in range(j+1,len(line)):
#             if line[i]<line[j]+line[k]:
#                 print(line[i]+line[j]+line[k])
#                 sys.exit(0)
# else:
#     print(-1)

# combinations -> 메모리 초과
# for combi in combination:
#     combi=list(combi)
#     combi.sort()
#     if combi[2]>=combi[0]+combi[1]:
#         continue
#     else:
#         if sum(combi)>max:
#             max=sum(combi)
# if max==0:
#     print(-1)
# else:
#     print(max)

