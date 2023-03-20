n,m=map(int, input().split(' '))

paper=[]
for i in range(n):
    tmp=list(map(int, input().strip().split(' ')))
    paper.append(tmp)

ans=0
#폴리노미오를 회전하거나, 대칭하는 경우 모두 포함해서 총 19가지 정도의 경우의 수가 나옴
for i in range(n):
    for j in range(m):
        # 1) 첫번째 경우의 수
        if j+3<m:
            c1=paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i][j+3]
            ans=max(ans, c1)
        # 2) 두번째 경우의 수
        if i+3<n:
            c2 = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j]
            ans=max(ans,c2)
        # 3) 세번째 경우의 수
        if i+1<n and j+1<m:
            c3=paper[i][j]+paper[i+1][j]+paper[i][j+1]+paper[i+1][j+1]
            ans=max(ans,c3)
        # 4) 4,5,6,10,12,15,16,18번째 경우의 수
        if i+2<n and j+1<m:
            c4=paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+2][j+1]
            c5=paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i][j+1]
            c6=paper[i][j+1]+paper[i+1][j+1]+paper[i+2][j+1]+paper[i+2][j]
            c10=paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i+2][j+1]
            c12=paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j+1]
            c15=paper[i+1][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i+2][j+1]
            c16=paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+1][j+1]
            c18=paper[i][j+1]+paper[i+1][j]+paper[i+1][j+1]+paper[i+2][j]
            ans=max(ans, c4, c5, c6, c10, c12, c15, c16,c18)
        # 5) 7,8,9,11,13,14,17,19번째 경우의 수
        if i+1<n and j+2<m:
            c7=paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i+1][j]
            c8=paper[i][j]+paper[i+1][j]+paper[i+1][j+1]+paper[i+1][j+2]
            c9=paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i+1][j+2]
            c11=paper[i+1][j]+paper[i+1][j+1]+paper[i+1][j+2]+paper[i][j+2]
            c13=paper[i+1][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i][j+2]
            c14=paper[i][j]+paper[i][j+1]+paper[i][j+2]+paper[i+1][j+1]
            c17=paper[i+1][j]+paper[i+1][j+1]+paper[i+1][j+2]+paper[i][j+1]
            c19=paper[i][j]+paper[i][j+1]+paper[i+1][j+1]+paper[i+1][j+2]
            ans=max(ans, c7,c8,c9,c11,c13,c14,c17,c19)

print(ans)