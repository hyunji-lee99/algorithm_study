import sys

vowel=set({'a','e','i','o','u'})
while True:
    cur=sys.stdin.readline().strip()
    if cur=='end':
        break
    if len(cur)==1:
        print('<'+cur+'> is acceptable.')
        continue
    condition1=False
    prev=cur[0]
    if prev in vowel:
        condition1=True
    for i in range(1,len(cur)):
        # 조건 1) a,e,i,o,u 중 하나 포함
        if not condition1 and cur[i] in vowel:
            condition1=True
        # 조건 2) 모음 3개 혹은 자음 3개가 연속해서 올 수 없음
        # 모음 연속 3개
        if (i<=len(cur)-2):
            if ((cur[i-1] in vowel) and (cur[i] in vowel) and (cur[i+1] in vowel)) or ((cur[i-1] not in vowel) and (cur[i] not in vowel) and (cur[i+1] not in vowel)):
                print('<' + cur + '> is not acceptable.')
                break
        # 조건 3) 같은 글자가 두 번 연속 올 수 없음('ee', 'oo' 제외)
        if prev==cur[i] and (prev!='o' and prev!='e'):
            print('<'+cur+'> is not acceptable.')
            break
        prev=cur[i]
    else:
        if condition1:
            print('<' + cur + '> is acceptable.')
        else:
            print('<' + cur + '> is not acceptable.')
