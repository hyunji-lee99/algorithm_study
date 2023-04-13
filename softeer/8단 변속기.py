import sys

gear=list(map(int, sys.stdin.readline().split(' ')))
# ascending 테스트
for i in range(7):
    if gear[i]+1==gear[i+1]:
        continue
    else:
        break
else:
    print('ascending')
    sys.exit(0)
#descending 테스트
for i in range(7):
    if gear[i]-1==gear[i+1]:
        continue
    else:
        break
else:
    print('descending')
    sys.exit(0)

print('mixed')