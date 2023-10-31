import sys

t=int(sys.stdin.readline())
for _ in range(t):
    w=sys.stdin.readline().strip()
    k=int(sys.stdin.readline())
    index={}
    # 문자열 w에 존재하는 문자의 인덱스 정보 저장
    for idx in range(len(w)):
        try:
            index[w[idx]].append(idx)
        except:
            index[w[idx]]=[idx]

    minLength=1e9
    maxLength=-1e9
    # 만족하는 문자열이 있는지 확인
    flag=False
    # 저장된 인덱스의 개수 k개 이상인 문자인 경우 가장 짧은 문자열, 가장 긴 문자열 탐색
    # 짧은 문자열이나, 긴 문자열이나 시작과 끝은 해당 문자여야 함
    for char, indexs in index.items():
        if len(indexs)>=k:
            for idx in range(len(indexs)-k+1):
                #  가장 짧은 문자열 구하기
                minLength=min(minLength, indexs[idx+k-1]-indexs[idx]+1)
                # 가장 긴 문자열 구하기
                maxLength = max(maxLength, indexs[idx+k-1] - indexs[idx] + 1)
            flag=True

    if flag:
        print(minLength, maxLength)
    else:
        print(-1)
