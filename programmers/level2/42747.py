# H-Index
# 정렬

def solution(citations):
    citations.sort(reverse=1)
    for h in range(citations[0],-1,-1):
        cnt = 0
        for c in citations:
            if c >= h: cnt += 1
        if cnt >= h: return h

print(solution([3,0,6,1,5])) # 3