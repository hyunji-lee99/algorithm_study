# 3X3 이차원 배열 A[r][c]==k가 되기 위한 최소시간을 구하라
# zip을 이용한 전치행렬
# zip(*iterable) -> 동일한 개수로 들어오는 자료형을 묶어줌. 개수가 다른 경우엔 가장 짧은 개수를 기준으로 묶어줌
# ex)
# iterable=[[1,2,3],[4,5,6],[7,8,9]]
# *iterable => [1,2,3], [4,5,6], [7,8,9]
# *를 붙여줌으로서 iterable을 unpacking함.
# zip(*iterable) = (1,4,7), (2,5,8), (3,6,9)

# 인덱스를 사용하기 보단 최대한 값에 접근하는 방식으로 for문을 사용해보자

r,c,k=map(int, input().split(' '))

A=[]
for i in range(3):
    tmp=list(map(int, input().split(' ')))
    A.append(tmp)

def calculate(matrix, method):
    new_matrix=[]
    maxlength=3
    for idx in range(len(matrix)):
        num_cnt=[]
        new_row=[]
        for num in set(matrix[idx]):
            if num!=0:
                num_cnt.append((num, matrix[idx].count(num)))
        # sorted 다중 정렬
        num_cnt=sorted(num_cnt, key=lambda x:(x[1],x[0]))
        for num, cnt in num_cnt:
            # append보다 좋은 방법
            new_row+=[num, cnt]
        # 최대 길이 갱신
        maxlength=max(maxlength, len(new_row))
        new_matrix.append(new_row)
    for mat in new_matrix:
        if len(mat)<maxlength:
            # while, append보다 좋은 방법
            mat += [0]*(maxlength-len(mat))
    if method=='R':
        return new_matrix
    elif method=='C':
        # 전치행렬로 돌려보내기
        return list(zip(*new_matrix))


time=0
while time<=100:
    # 배열의 인덱스는 1부터 시작한다. 즉, r=1이면 0번 행을 뜻함
    # r-1, c-1 범위 제한을 넣어주면 인덱스 에러 해결됨. 왜 넣어야 하지?
    # 4 4 1
    # 1 2 1
    # 2 1 3
    # 3 3 3
    # 위와 같은 테스트케이스의 경우, 연산 과정에서 2차원 배열의 크기가 커지면 확인해야 하는데, 바로 A[3][3]을 확인해서 에러 발생
    # A[r][c]를 확인가능한지 먼저 파악해주려면 넣어야 함!!
    if 0<=r-1<len(A) and 0<=c-1<len(A[0]) and A[r - 1][c - 1] == k:
        print(time)
        break
    # 행의 길이 >= 열의 길이
    if len(A)>=len(A[0]):
        A=calculate(A, 'R')
    else:
        A=calculate(list(zip(*A)),'C')
    time+=1
else:
    print(-1)



# 기존 지저분한 코드
# set을 이용한 중복제거, zip을 이용한 전치행렬로 풀 수 있음(이 코드로 발생하는 인덱스 에러나 정답 오류도 해결 가능)
# r,c,k=map(int, input().split(' '))
#
# A=[]
# for i in range(3):
#     tmp=list(map(int, input().split(' ')))
#     A.append(tmp)
#
# time=0
# while time<=100:
#     # 배열의 인덱스는 1부터 시작한다. 즉, r=1이면 0번 행을 뜻함
#     if A[r - 1][c - 1] == k:
#         print(time)
#         break
#     # 행의 길이 >= 열의 길이
#     rowlen=len(A)
#     collen=len(A[0])
#     if rowlen>=collen:
#         # 3X3 배열이므로 길이가 3보다 작아질 순 없어야 함
#         maxvalue=3
#         for idx in range(rowlen):
#             tmp=[]
#             visited=[]
#             for i in range(collen):
#                 if A[idx][i]!=0 and A[idx][i] not in visited:
#                     tmp.append((A[idx][i], A[idx].count(A[idx][i])))
#                     visited.append(A[idx][i])
#             tmp=sorted(tmp,key=lambda x:(x[1],x[0]))
#             sorted_tmp=[]
#             for t in tmp:
#                 sorted_tmp.append(t[0])
#                 sorted_tmp.append(t[1])
#             # 행 또는 열의 크기가 100을 넘어가는 경우엔 100까지만 살리고 나머진 버린다
#             if len(sorted_tmp)>100:
#                 sorted_tmp=sorted_tmp[:100]
#             A[idx]=sorted_tmp.copy()
#             maxvalue=max(maxvalue,len(sorted_tmp))
#         # 가장 큰 열 길이로 맞추기
#         for arr in A:
#             if len(arr)<maxvalue:
#                 while len(arr)!=maxvalue:
#                     arr.append(0)
#     # 행 길이 < 열 길이
#     else:
#         maxvalue=3
#         coltmp=[]
#         for idx in range(collen):
#             tmp=[]
#             visited=[]
#             col=[arr[idx] for arr in A]
#             for i in range(rowlen):
#                 if col[i]!=0 and col[i] not in visited:
#                     tmp.append((col[i], col.count(col[i])))
#                     visited.append(col[i])
#             tmp=sorted(tmp, key=lambda x:(x[1],x[0]))
#             sorted_tmp=[]
#             for t in tmp:
#                 sorted_tmp.append(t[0])
#                 sorted_tmp.append(t[1])
#
#             # 행 또는 열의 크기가 100을 넘어가는 경우엔 100까지만 살리고 나머진 버린다
#             if len(sorted_tmp) > 100:
#                 sorted_tmp = sorted_tmp[:100]
#
#             coltmp.append(sorted_tmp)
#             maxvalue=max(maxvalue,len(sorted_tmp))
#         # 최대 행 길이로 확장하기, coltmp 최대 행 길이로 확장하기
#         if len(A)<maxvalue:
#             while len(A)!=maxvalue:
#                 A.append([0]*collen)
#         for ct in coltmp:
#             if len(ct)<maxvalue:
#                 while len(ct)!=maxvalue:
#                     ct.append(0)
#         # coltmp를 A에 반영
#         for i in range(len(coltmp)):
#             for j in range(len(coltmp[i])):
#                 A[j][i]=coltmp[i][j]
#     time+=1
# else:
#     print(-1)
#
#
