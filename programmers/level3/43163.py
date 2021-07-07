# 단어 변환
# 깊이/너비 우선 탐색(DFS/BFS)

from collections import deque

def solution(begin, target, words):
    N = len(words) # 단어의 개수
    visited = [0]*N # words의 단어들을 만들 수 있는지 여부

    # BFS
    q = deque([(begin,0)])
    while q:
        cur,cnt = q.popleft() # 현재 단어와 현재 단어를 만드는 데 걸린 횟수
        if cur == target: return cnt # target과 같으면 횟수 반환
        for i in range(N):
            if visited[i]: continue # 이미 만들어본 단어라면 넘어감

            # 각각의 문자들이 다른지 확인하고 다른 문자의 개수 세기
            is_different = 0 # 해당 단어와 다른 문자의 개수
            for s in range(len(begin)):
                # 해당 문자가 다른 경우, 개수 갱신
                if cur[s] != words[i][s]:
                    is_different += 1
                    if is_different > 1: break # 2개 이상이면 종료
            # 하나의 알파벳만 다른 경우
            if is_different == 1:
                visited[i] = 1 # 그 단어로 바꿀 수 있음을 확인
                q.append((words[i],cnt+1)) # 그 단어와 횟수를 q에 넣기
    return 0 # target으로 만들지 못하면 0 반환

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0