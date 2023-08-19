import sys


# 최종 상태가 가능한 경우
# 1) X의 개수 = 5, O의 개수 =4 이면서 게임판이 모두 차있음(단, X,0 모두 3칸을 채운 상태가 아님)
# 2) X의 개수 = O의 개수이면서 O가 3칸을 이은 경우
# 3) X의 개수 = O의 개수+1 이면서 X가 3칸을 이은 경우
# X가 쌍대각선을 이루는 경우를 제외하고, 한 줄만 만족해야 함.

def success(tictactoe, xoro):
    # 대각선 만족하는 라인 개수
    dia_line=0
    # 평행선 만족하는 라인 개수
    pal_line=0
    # 3줄을 만족하는 경우 찾기
    # 1줄 이상 만족히면 불가능한 경우이기 때문에 line 변수에 만족하는 줄의 개수를 저장함.
    # 대각선으로 만족하는 경우
    if tictactoe[0][0]==xoro and tictactoe[1][1]==xoro and tictactoe[2][2]==xoro:
        dia_line+=1
    if tictactoe[0][2]==xoro and tictactoe[1][1]==xoro and tictactoe[2][0]==xoro:
        dia_line+=1
    for i in range(3):
        if tictactoe[i][0]==xoro and tictactoe[i][1]==xoro and tictactoe[i][2]==xoro:
            pal_line+=1
        if tictactoe[0][i]==xoro and tictactoe[1][i]==xoro and tictactoe[2][i]==xoro:
            pal_line+=1
    # 1줄만 만족하는 경우
    if dia_line+pal_line==1:
        return True
    elif dia_line==2:
        return True
    else:
        return False



while True:
    tictactoe=sys.stdin.readline().strip()
    if tictactoe=='end':
        sys.exit(0)
    tictactoe2d=[list(tictactoe[:3]),list(tictactoe[3:6]),list(tictactoe[6:])]
    # X의 개수
    numX=tictactoe.count('X')
    # O의 개수
    numY=tictactoe.count('O')
    # X의 개수 = O의 개수 +1 인 경우
    if numX==numY+1:
        # 꽉 채워져 있는데 누구도 이기지 못하고 종료되는 경우
        if numX==5 and numY==4 and not success(tictactoe2d,'X') and not success(tictactoe2d, 'O'):
            print('valid')
        # X가 이기는 경우(한 줄만 만족하면서 'O'는 한줄도 만족하면 안됨)
        elif success(tictactoe2d,'X') and not success(tictactoe2d, 'O'):
            print('valid')
        # 두 경우 모두 아니면 최종 상태에 도달할 수 있는 상태가 아님
        else:
            print('invalid')
    elif numX==numY:
        # O가 이기는 경우
        if success(tictactoe2d,'O') and not success(tictactoe2d,'X'):
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')
