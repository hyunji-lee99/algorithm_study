import sys

h,w = map(int,sys.stdin.readline().split(' '))
blocks=list(map(int, sys.stdin.readline().split(' ')))

total=0
for i in range(1,w-1):
    left_max=max(blocks[:i])
    right_max=max(blocks[i+1:])
    add_value=min(left_max, right_max)-blocks[i]
    if add_value>0:
        total+=add_value

print(total)
