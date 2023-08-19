import sys

abstring=list(sys.stdin.readline().strip())

#a의 개수만큼 연속 a string이 있어야 함!
numberofa=abstring.count('a')

min=1e9
for i in range(len(abstring)):
    if i+numberofa<=len(abstring):
        searchArr=abstring[i:i+numberofa]
        change=searchArr.count('b')
        if change<min:
            min=change
    else:
        searchArr=abstring[i:len(abstring)]+abstring[0:numberofa-(len(abstring)-i)]
        change=searchArr.count('b')
        if change<min:
            min=change

print(min)

#아이디어가 중요한 문제였음!