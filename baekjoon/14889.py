# 스타트와 링크
# 브루트 포스, 백트래킹

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]
ans = 20000
# 조합 구하기
for i in range(1<<(N-1)):
    start = []
    link = []
    for j in range(N):
        if i&1: start.append(j)
        else: link.append(j)
        i = i//2
        if len(start)>N//2 or len(link)>N//2: break # 한 팀에 전체의 반 이상이 들어간 경우 넘김
    if len(start)!=N//2 or len(link)!=N//2: continue # 각 팀당 반씩 들어가지 않은 경우 넘김
    diff = 0 # 두 팀의 능력치 차이
    for i in range(N//2-1): # i번째 팀원
        for j in range(i+1,N//2): # j번째 팀원
            diff += S[start[i]][start[j]]+S[start[j]][start[i]] # 스타트 팀의 능력치의 합은 더함
            diff -= S[link[i]][link[j]]+S[link[j]][link[i]] # 링크 팀의 능력치의 합은 빼줌
    ans = min(ans,abs(diff)) # 차이 값을 절대값으로 바꾼 뒤 현재 최솟값과 비교하여 갱신
print(ans)