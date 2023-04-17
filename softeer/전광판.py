import sys

t=int(sys.stdin.readline())

num={
    '0':'1110111',
    '1':'0010010',
    '2':'1011101',
    '3':'1011011',
    '4':'0111010',
    '5':'1101011',
    '6':'1101111',
    '7':'1110010',
    '8':'1111111',
    '9':'1111011',
    ' ':'00000000'
}

for _ in range(t):
    a,b=sys.stdin.readline().strip().split(' ')
    a=(5-len(a))*' '+a
    b=(5-len(b))*' '+b
    ans=0
    for i in range(5):
        for j in range(7):
            if num[a[i]][j]!=num[b[i]][j]:
                ans+=1
    print(ans)
