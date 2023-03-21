# 완전탐색, 조합
# 각 케이스별로 변화하는 office 배열을 저장해서, 저장된 다음 cctv 번호를 차례로 순회하면서 저장된 배열을 업데이트하고, 모든 cctv의 경우의 수를 반영한 배열
# 을 기준으로 0의 개수, 즉 사각지대를 계산해서 최솟값을 계산함.
n,m=map(int, input().split(' '))

office=[]
for i in range(n):
    tmp=list(map(int, input().strip().split(' ')))
    office.append(tmp)

cctv=[]
#cctv 위치 및 번호 저장
for i in range(n):
    for j in range(m):
        # 빈칸(0)도 아니고, 벽(6)도 아니면
        if office[i][j]!=0 and office[i][j]!=6:
            # cctv 번호화 위치 인덱스 저장
            cctv.append((office[i][j],i,j))

def cctv1(y,x,poffice):
    office_copy1 = [arr[:] for arr in poffice]
    for i in range(y - 1, -1, -1):
        # 벽을 만나면
        if office_copy1[i][x] == 6:
            break
        # cctv를 만나면
        elif office_copy1[i][x] != 0 and office_copy1[i][x] != 6:
            continue
        else:
            office_copy1[i][x] = '#'
    office_arr.append(office_copy1)
    # >
    office_copy2 = [arr[:] for arr in poffice]
    for i in range(x + 1, m):
        # 벽을 만나면
        if office_copy2[y][i] == 6:
            break
        # cctv를 만나면
        elif office_copy2[y][i] != 0 and office_copy2[y][i] != 6:
            continue
        else:
            office_copy2[y][i] = '#'
    office_arr.append(office_copy2)
    # v
    office_copy3 = [arr[:] for arr in poffice]
    for i in range(y + 1, n):
        # 벽을 만나면
        if office_copy3[i][x] == 6:
            break
        # cctv를 만나면
        elif office_copy3[i][x] != 0 and office_copy3[i][x] != 6:
            continue
        else:
            office_copy3[i][x] = '#'
    office_arr.append(office_copy3)
    # <
    office_copy4 = [arr[:] for arr in poffice]
    for i in range(x - 1, -1, -1):
        # 벽을 만나면
        if office_copy4[y][i] == 6:
            break
        # cctv를 만나면
        elif office_copy4[y][i] != 0 and office_copy4[y][i] != 6:
            continue
        else:
            office_copy4[y][i] = '#'
    office_arr.append(office_copy4)

def cctv2(y,x,poffice):
    # < >
    office_copy=[arr[:] for arr in poffice]
    for i in range(x+1,m):
        if office_copy[y][i]==6:
            break
        elif office_copy[y][i]!=0 and office_copy[y][i]!=6:
            continue
        else:
            office_copy[y][i]='#'
    for i in range(x-1,-1,-1):
        if office_copy[y][i]==6:
            break
        elif office_copy[y][i]!=0 and office_copy[y][i]!=6:
            continue
        else:
            office_copy[y][i]='#'
    office_arr.append(office_copy)
    # ^
    # v
    office_copy = [arr[:] for arr in poffice]
    for i in range(y-1,-1,-1):
        if office_copy[i][x]==6:
            break
        elif office_copy[i][x]!=0 and office_copy[i][x]!=6:
            continue
        else:
            office_copy[i][x]='#'
    for i in range(y+1, n):
        if office_copy[i][x]==6:
            break
        elif office_copy[i][x]!=0 and office_copy[i][x]!=6:
            continue
        else:
            office_copy[i][x]='#'
    office_arr.append(office_copy)

def cctv3(y,x,poffice):
    # ^ >
    office_copy=[arr[:] for arr in poffice]
    for i in range(y-1,-1,-1):
        if office_copy[i][x]==6:
            break
        elif office_copy[i][x]!=0 and office_copy[i][x]!=6:
            continue
        else:
            office_copy[i][x]='#'
    for i in range(x+1,m):
        if office_copy[y][i]==6:
            break
        elif office_copy[y][i]!=0 and office_copy[y][i]!=6:
            continue
        else:
            office_copy[y][i]='#'
    office_arr.append(office_copy)

    # v >
    office_copy = [arr[:] for arr in poffice]
    for i in range(y+1,n):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(x + 1, m):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    office_arr.append(office_copy)

    # < v
    office_copy = [arr[:] for arr in poffice]
    for i in range(y + 1, n):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(x-1,-1,-1):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    office_arr.append(office_copy)

    # < ^
    office_copy = [arr[:] for arr in poffice]
    for i in range(y - 1, -1, -1):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(x - 1, -1, -1):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    office_arr.append(office_copy)

def cctv4(y,x,poffice):
    # < ^ >
    office_copy = [arr[:] for arr in poffice]
    for i in range(x - 1, -1, -1):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    for i in range(y-1,-1,-1):
        if office_copy[i][x]==6:
            break
        elif office_copy[i][x]!=0 and office_copy[i][x]!=6:
            continue
        else:
            office_copy[i][x]='#'
    for i in range(x+1,m):
        if office_copy[y][i]==6:
            break
        elif office_copy[y][i]!=0 and office_copy[y][i]!=6:
            continue
        else:
            office_copy[y][i]='#'
    office_arr.append(office_copy)

    # ^
    #   >
    # V
    office_copy = [arr[:] for arr in poffice]
    for i in range(y + 1, n):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(y - 1, -1, -1):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(x + 1, m):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    office_arr.append(office_copy)

    # < v >
    office_copy = [arr[:] for arr in poffice]
    for i in range(x - 1, -1, -1):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    for i in range(y + 1, n):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(x + 1, m):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    office_arr.append(office_copy)

    #   ^
    # <
    #   v
    office_copy = [arr[:] for arr in poffice]
    for i in range(y + 1, n):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(y - 1, -1, -1):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(x - 1, -1, -1):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    office_arr.append(office_copy)

def cctv5(y,x,poffice):
    #   ^
    # <
    #   v
    office_copy = [arr[:] for arr in poffice]
    for i in range(y + 1, n):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(y - 1, -1, -1):
        if office_copy[i][x] == 6:
            break
        elif office_copy[i][x] != 0 and office_copy[i][x] != 6:
            continue
        else:
            office_copy[i][x] = '#'
    for i in range(x - 1, -1, -1):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    for i in range(x + 1, m):
        if office_copy[y][i] == 6:
            break
        elif office_copy[y][i] != 0 and office_copy[y][i] != 6:
            continue
        else:
            office_copy[y][i] = '#'
    office_arr.append(office_copy)


office_arr=[]
office_arr.append([arr[:] for arr in office])
while cctv:
    num, y, x=cctv.pop(0)
    cnt=len(office_arr)
    # office arr를 복사(3차워 배열 복사)
    office_arr_copy=[d1[:] for d1 in [d2[:] for d2 in office_arr]]
    for poffice in office_arr_copy:
        if num == 1:
            cctv1(y, x, poffice)
        elif num == 2:
            cctv2(y, x, poffice)
        elif num==3:
            cctv3(y,x,poffice)
        elif num==4:
            cctv4(y,x,poffice)
        elif num==5:
            cctv5(y,x,poffice)

    for i in range(cnt):
        office_arr.pop(0)


def calculate(poffice):
    ans=0
    for i in range(n):
        for j in range(m):
            if poffice[i][j]==0:
                ans+=1
    return ans

minvalue=1e9
for poffice in office_arr:
    minvalue=min(calculate(poffice),minvalue)

print(minvalue)
