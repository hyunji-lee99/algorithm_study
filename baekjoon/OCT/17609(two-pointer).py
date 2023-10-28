import sys

n=int(sys.stdin.readline())

def isPallindrome(left, right, delete, str):
    while left<right:
        if str[left]!=str[right]:
            if delete==0:
                if isPallindrome(left+1, right, 1, str)==0 or isPallindrome(left, right-1, 1, str)==0:
                    return 1
                return 2
            return 2
        else:
            left+=1
            right-=1
    return 0

for _ in range(n):
    str=sys.stdin.readline().strip()
    # 삭제된 개수
    delete=0
    print(isPallindrome(0, len(str)-1,0, str))
