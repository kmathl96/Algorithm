# 징검다리
# 이분탐색

def solution(distance, rocks, n):
    rocks.sort() # 바위의 좌표 정렬
    
    start,end = 1,distance # 각 지점 사이의 거리의 최솟값과 최댓값
    while start <= end:
        mid = (start+end)//2 # 기준 거리 : 거리의 최솟값과 최댓값의 중간값
        cur,cnt = 0,0 # 직전 지점의 좌표, 바위 제거 횟수
        for rock in rocks:
            # 전 지점과 현재 바위와의 거리가 기준 거리보다 작은 경우, 바위 제거
            if rock-cur < mid: cnt += 1
            else: cur = rock # 바위를 제거 하지 않으므로, cur를 현재 좌표로 갱신
        if distance-cur < mid: cnt += 1 # 도착 지점과의 거리도 고려

        if cnt > n: end = mid-1 # 바위 제거 횟수가 n보다 큰 경우 end 값 갱신
        else: start = mid+1 # 거리의 최솟값인 start 값 갱신
    return end # 최댓값 반환

print(solution(25, [2, 14, 11, 21, 17], 2)) # 4

print(solution(16, [4,8,11], 2)) # 8