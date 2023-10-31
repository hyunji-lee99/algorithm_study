import sys
n=int(sys.stdin.readline())
string_Array=set([sys.stdin.readline().strip() for _ in range(n)])
# 중복 제거를 위해 set을 사용하면 sort를 사용할 수 없고, sorted를 사용한다
print(*sorted(string_Array,key=lambda x:(len(x),x)),sep='\n')