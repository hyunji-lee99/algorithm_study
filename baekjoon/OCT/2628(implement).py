import sys

garo, sero = map(int, sys.stdin.readline().split(' '))
num=int(sys.stdin.readline())

garo_cut=[0]*(sero)
sero_cut=[0]*(garo)
# how가 0이면 가로 줄, 1이면 세로 줄
for _ in range(num):
    how, line = map(int, sys.stdin.readline().split(' '))
    if how==0:
        garo_cut[line]=1
    elif how==1:
        sero_cut[line]=1

garo_possible_line=[]
sero_possible_line=[]
cur=1
for i in range(1,garo):
    if i==garo-1:
        if sero_cut[i]==1:
            garo_possible_line.append(cur)
        else:
            garo_possible_line.append(cur+1)
        break
    if sero_cut[i]==1:
        garo_possible_line.append(cur)
        cur=1
    else:
        cur+=1

cur=1
for i in range(1,sero):
    if i==sero-1:
        if garo_cut[i]==1:
            sero_possible_line.append(cur)
        else:
            sero_possible_line.append(cur+1)
        break
    if garo_cut[i]==1:
        sero_possible_line.append(cur)
        cur=1
    else:
        cur+=1

print(max(sero_possible_line)*max(garo_possible_line))
