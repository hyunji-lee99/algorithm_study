import sys

string=sys.stdin.readline().strip()

for i in range(len(string)//10+1):
    if (i+1)*10>len(string):
        print(string[i*10:])
    else:
        print(string[i*10:(i+1)*10])
