# 탐색 길이를 하나씩 늘려가면서 완전 탐색하는 것은 시간초과!
# 문자열에서 각 알파벳의 인덱스를 저장해두고, 해당 알파벳의 인덱스가 k보다 같거나 많은 경우에만 탐색 진행

import sys

n=int(sys.stdin.readline())

# 완전탐색 시간초과
# def bf_string(string, k):
#     L=len(string)
#     # superaquatornado
#     three_minvalue=len(string)
#     four_maxvalue=k
#     flag=False
#     for length in range(k, L+1):
#         for i in range(L-length):
#             # 'su', 'up', 'pe',...
#             search_string=string[i:i+length]
#             set_search_string=set(search_string)
#             for s in set_search_string:
#                 if search_string.count(s)==k:
#                     flag=True
#                     # 어떤 값이 k개인 문자열
#                     three_minvalue=min(three_minvalue, length)
#                     # 문자열의 첫 번째와 마지막 글자가 *해당 문자*로 같은 가장 긴 연속 문자열의 길이
#                     if search_string[0]==s and search_string[0]==search_string[-1]:
#                         four_maxvalue=max(four_maxvalue, length)
#
#     if flag:
#         return three_minvalue, four_maxvalue
#
# for i in range(n):
#     string=sys.stdin.readline().strip()
#     k=int(sys.stdin.readline())
#     ans = bf_string(string, k)
#     if ans!=None:
#         print(ans[0], ans[1])
#     else:
#         print(-1)

def searching(string, k):
    global alphabet
    minvalue=1e9
    maxvalue=k
    # 알파벳의 개수와 인덱스 구하기
    for i in range(len(string)):
        alphabet[string[i]].append(i)
    # 만족하는 문자열이 있는지 확인
    flag=False
    for key, items in alphabet.items():
        if len(items)>=k:
            for item in items:
                # 해당 인덱스에서 탐색하면서 특정 문자가 k개가 되면 break
                numberofk=0
                for idx in range(item, len(string)):
                    if string[idx]==key:
                        numberofk+=1
                    if numberofk==k:
                        flag=True
                        minvalue=min(idx-item+1, minvalue)
                        if string[idx]==string[item]:
                            maxvalue=max(idx-item+1, maxvalue)
                        break
    if flag:
        print(minvalue, maxvalue)
    else:
        print(-1)



for i in range(n):
    string=sys.stdin.readline().strip()
    k=int(sys.stdin.readline())
    alphabet={
        'a':[], 'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[]
        ,'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]
    }
    searching(string, k)