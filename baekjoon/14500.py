# 테트로미노
# 브루트 포스
# 테트로미노가 차지하는 칸의 범위(1*4,2*2,2*3,3*2,4*1)별로 최대값을 구함
# 해당 위치의 '열'을 기준으로, 테트로미노를 놓을 수 있는지 여부 판단

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = []
for r in range(N):
    for c in range(M):
        # 4*1 (세로로 긴 직사각형)
        if r < N-3: ans.append(sum([arr[r+i][c] for i in range(4)]))
        if c > M-2: continue # 밑의 테트로미노들은 해당 열에서 더 이상 놓을 수 없음
        # 2*2 (정사각형)
        if r < N-1: ans.append(sum(arr[r][c:c+2])+sum(arr[r+1][c:c+2]))
        # 3*2 (L,N,ㅏ,ㅓ 같은 모양의 테트로미노)
        if r < N-2: ans.append(max(arr[r][c]+arr[r+1][c]+arr[r+2][c]+max(arr[r+2][c+1],arr[r][c+1]),arr[r][c+1]+arr[r+1][c+1]+arr[r+2][c+1]+max(arr[r][c],arr[r+2][c]),arr[r+1][c]+arr[r+1][c+1]+max(arr[r][c:c+2])+max(arr[r+2][c:c+2])))
        if c > M-3: continue
        # 2*3 (Z,ㅗ,ㅜ 같은 모양의 테트로미노)
        if r < N-1: ans.append(max(sum(arr[r][c:c+3])+max(arr[r+1][c:c+3]),sum(arr[r+1][c:c+3])+max(arr[r][c:c+3]),sum(arr[r][c:c+2])+sum(arr[r+1][c+1:c+3]),sum(arr[r][c+1:c+3])+sum(arr[r+1][c:c+2])))
        if c > M-4: continue
        # 1*4 (가로로 긴 직사각형)
        ans.append(sum(arr[r][c:c+4]))
print(max(ans))