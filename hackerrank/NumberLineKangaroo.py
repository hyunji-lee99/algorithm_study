
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # 속도가 같을 경우엔 무조건 만날 수 없음(속도가 같으면 앞선 캥거루를 뒤따르는 캥거루가 따라잡을 수 없다)
    if v2==v1:
        return 'NO'
    jump = (x1 - x2) / (v2 - v1)
    if jump > 0 and int(jump) == jump:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
