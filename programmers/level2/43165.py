# 타겟 넘버
# 깊이/너비 우선 탐색(DFS/BFS)

def solution(numbers, target):
    answer = 0
    st = [(numbers[0],0),(-numbers[0],0)]
    while st:
        n,cnt = st.pop()
        nxt = numbers[cnt+1]
        if cnt == len(numbers)-2:
            if n + nxt == target: answer += 1
            if n - nxt == target: answer += 1
        else:
            st.append((n+nxt, cnt+1))
            st.append((n-nxt, cnt+1))
    return answer

print(solution([1, 1, 1, 1, 1], 3)) # 5