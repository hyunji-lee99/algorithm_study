from collections import deque

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
def solution(begin, target, words):
    answer = 0
    # visited, queue, distance 초기화
    visited = []

    # append하면 추가한 배열을 반환하는 것이 아니라, 그 자체로 배열에 변동이 생기는 것 주의
    words.append(begin)
    distance = dict(zip(words, [0] * (len(words))))
    queue = deque()
    queue.append(begin)
    visited.append(begin)

    # words 안에 target이 존재하지 않는 경우

    if target not in words:
        return 0

    while queue:
        cur = queue.popleft()
        if cur == target:
            return distance[cur]
        # words에서 이동할 수 있는 단어가 없는 경우 찾는 용도
        check = 0
        for word in words:
            # cur 단어와 1개만 다른 원소 찾기
            diff = 0
            for i in range(len(word)):
                if cur[i] != word[i]:
                    diff += 1
            if diff == 1:
                if word not in visited:
                    queue.append(word)
                    visited.append(word)
                    distance[word] = distance[cur] + 1
                check = 1
        if check == 0:
            return 0
    return answer

print(solution(begin,target,words))