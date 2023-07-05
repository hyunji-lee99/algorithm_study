import sys

n=int(sys.stdin.readline())
balls=list(sys.stdin.readline().strip())

# B 또는 R만 존재하는 경우 0 출력하고 종료
if 'B' not in balls:
    print(0)
    sys.exit(0)
if 'R' not in balls:
    print(0)
    sys.exit(0)

# 빨간색을 왼쪽으로 모으는 경우, 오른쪽으로 모으는 경우
# 파란색을 왼쪽으로 모으는 경우, 오른쪽으로 모으는 경우
# 4가지 경우의 수를 구해서 최솟값을 구하자

# 1) 빨간색을 왼쪽으로 모으는 경우
# 파란색이 나온 이후의 빨간색의 개수를 모두 세어주면 됨.
red_left=0
is_blue_left=False
for ball in balls:
    if ball=='R' and is_blue_left:
        red_left+=1
    elif ball=='B' and not is_blue_left:
        is_blue_left=True

# 2) 빨간색을 오른쪽으로 모으는 경우
red_right=0
is_blue_right=False
for ball in reversed(balls):
    if ball=='R' and is_blue_right:
        red_right+=1
    elif ball=='B' and not is_blue_right:
        is_blue_right=True

# 3) 파란색을 왼쪽으로 모으는 경우
blue_left=0
is_red_left=False
for ball in balls:
    if ball=='B' and is_red_left:
        blue_left+=1
    elif ball=='R' and not is_red_left:
        is_red_left=True

# 4) 파란색을 오른쪽으로 모으는 경우
blue_right=0
is_red_right=False
for ball in reversed(balls):
    if ball=='B' and is_red_right:
        blue_right+=1
    elif ball=='R' and not is_red_right:
        is_red_right=True

print(min(red_left, red_right, blue_left, blue_right))




