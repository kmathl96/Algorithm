# 마법사 상어와 파이어볼
# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

# 파이어볼의 정보를 이용해, 위치에 맞게 격자(맵)에 파이어볼 넣기
def set_map(fireball):
    for _ in range(len(fireball)):
        r,c,m,s,d = fireball.pop()
        map_[r][c].append((m,s,d))

dr,dc = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1] # 파이어볼의 방향
N,M,K = map(int,input().split()) # 격자의 크기, 파이어볼의 개수, 이동할 횟수
map_ = [[[] for i in range(N+1)] for j in range(N+1)] # 격자 : 각 칸을 빈 리스트로 초기화
fireball = [list(map(int,input().split())) for _ in range(M)] # 파이어볼의 정보
set_map(fireball) # 격자에 파이어볼 넣기

# K번 이동
for _ in range(K):
    # 1. 모든 파이어볼 이동
    for r in range(1,N+1):
        for c in range(1,N+1):
            if not map_[r][c]: continue # 해당 칸에 파이어볼이 없으면 넘어감
            for m,s,d in map_[r][c]:
                # 해당 방향(d)으로 속력(s)만큼 움직임
                # 1행-N행, 1열-N열이 연결되어 있음 => 나머지 연산을 활용해 처리
                nr,nc = (r+dr[d]*s-1)%N+1,(c+dc[d]*s-1)%N+1
                fireball.append((nr,nc,m,s,d))
            map_[r][c] = []
    set_map(fireball)
    # 2. 2개 이상인 파이어볼 처리
    for r in range(1,N+1):
        for c in range(1,N+1):
            n = len(map_[r][c]) # 해당 칸의 파이어볼 개수
            if n < 2: continue # 2개 미만이면 넘어감
            # 2-1. 하나로 합치기
            # 모든 파이어볼의 질량과 속력의 합, 방향(첫 파이어볼의 방향의 홀수 여부로 초기화)
            new_m,new_s,new_d = 0,0,map_[r][c][0][2]&1
            flag = 0 # 모든 파이어볼의 방향이 일치하는지 여부
            for m,s,d in map_[r][c]:
                new_m += m
                new_s += s
                # 현재 파이어볼의 방향의 홀수 여부가 첫 파이어볼과 다른 경우
                if d&1 != new_d: flag = 1 # flag 변경
            # 2-3. 나누어질 파이어볼의 질량, 속력, 방향 구하기
            new_m //= 5
            new_s //= n
            map_[r][c] = []
            # 2-4. 질량이 0인 파이어볼은 소멸, 아닌 경우는 넣기
            if new_m:
                # 2-2. 4개의 파이어볼로 나눠서 그 자리에 넣기
                for i in range(4):
                    # 방향 : 모두 같으면 (0,2,4,6), 다르면 (1,3,5,7)
                    # flag : 모두 같으면 0, 다르면 1
                    # => 2*i + flag
                    map_[r][c].append((new_m,new_s,flag+2*i))

# 남아있는 파이어볼의 질량의 합 구하기
ans = 0
for r in range(1,N+1):
    for c in range(1,N+1):
        if not map_[r][c]: continue # 파이어볼이 없으면 넘어감
        for m,s,d in map_[r][c]:
            ans += m
print(ans)