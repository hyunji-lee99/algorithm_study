#그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하시오.
#스패닝 트리 : 모든 노드들을 연결하면서 사이클은 존재하지 않는 부분 그래프
#최소 스패닝 트리 : 스패닝 트리 중 그 가중치의 합이 최소인 트리
# 최소 스패닝 트리 -> 크루스칼 알고리즘 적용
# 크루스칼 알고리즘, union-find 사용
# 1. 주어진 모든 간선 정보에 대해 오름차순으로 정렬
# 2. 정렬된 간선 정보를 하나씩 확인하면서 현재의 간선이 노드들 간의 사이클을 발생시키는지 확인
# 3. 만약 사이클이 발생하지 않는 경우, 최소 스패닝 트리에 포함시키고 사이클이 발생할 경우, 최소 스패닝 트리에 포함시키지 않음
# 4. 1~3번 과정을 모든 간선 정보에 대해 반복 수행
# 사이클이 발생한다는 것은? 노드들의 부모노드가 같다면 사이클이 발생.(부모 테이블 따로 생성)
# 예를 들어, 간선 3-4를 추가하려고 하니까 둘다 부모노드가 1이라면 사이클 발생

import sys
#v: 정점의 개수
#e: 간선의 개수
v,e=map(int, sys.stdin.readline().strip().split(' '))
#부모노드 리스트는 자기 자신의 노드번호로 초기화
parent=[x for x in range(v+1)]

def find_parent(x):
    if parent[x]!=x:
        return find_parent(parent[x])
    return x

def union(x,y):
    parent_x=find_parent(x)
    parent_y=find_parent(y)
    if parent_x<parent_y:
        parent[parent_y]=parent_x
    else:
        parent[parent_x]=parent_y

edge=[]
for i in range(e):
    n1,n2,w=map(int, sys.stdin.readline().strip().split(' '))
    edge.append((n1,n2,w))

#lambda식으로 sorting하는 방법 주의
sorted_edge=sorted(edge, key=lambda x:x[2])
weight=0
for n1,n2,w in sorted_edge:
    #사이클을 생성하는지 확인
    if find_parent(n1)!=find_parent(n2):
        # union-find 사용
        union(n1, n2)
        weight+=w

print(weight)