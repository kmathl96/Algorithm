# 단어 변환
# 깊이/너비 우선 탐색(DFS/BFS)

from collections import deque

def solution(begin, target, words):
    answer = 0
    N = len(words)
    visited = [0]*N
    q = deque([(begin,0)])
    while q:
        cur,cnt = q.popleft()
        if cur == target: return cnt
        for i in range(N):
            if visited[i]: continue
            is_different = 0
            for s in range(len(begin)):
                if cur[s] != words[i][s]:
                    is_different += 1
                    if is_different > 1: break
            if is_different == 1:
                visited[i] = 1
                q.append((words[i],cnt+1))
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0