# 공유기 설치
# 이분 탐색

# 실행 속도를 줄이기 위함
import sys
input = sys.stdin.readline

N,C = map(int,input().split()) # 집의 개수와 공유기의 개수
houses = sorted([int(input()) for _ in range(N)]) # 집의 좌표 (오름차순 정렬)

# 공유기 사이의 거리의 최솟값(s)과 최댓값(e)
# 최댓값(e) : 첫 좌표에 하나를 설치하고, 그다음부터 (C-1)개를 설치할 때의 공유기 거리의 최댓값
s,e = 1,(houses[-1]-houses[0])//(C-1)

while s<=e:
    gap = (s+e)//2 # 공유기 사이 거리
    # 해당 거리(gap) 이상 띄우면서 C개 이상의 공유기를 설치할 수 있는지 확인
    # 맨 첫 좌표에 공유기를 설치하고 시작
    cnt,installed = 1,houses[0] # 공유기를 설치한 횟수, 직전에 설치된 좌표
    for i in range(1,N):
        if cnt == C: break # C개 설치 되면 종료
        # 설치된 집과의 거리가 gap보다 큰 경우, 공유기 설치
        if houses[i]-installed >= gap:
            installed = houses[i] # 설치된 좌표 변경
            cnt += 1 # 공유기 설치횟수 증가
    
    if cnt >= C: # 공유기 설치 횟수가 C 이상인 경우
        s = gap+1 # 최소 거리 갱신
        ans = gap # ans 갱신
    else: e = gap-1 # C 만큼 공유기를 설치하지 못하는 경우, 최대 거리 갱신
print(ans)