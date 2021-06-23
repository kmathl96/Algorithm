# 디스크 컨트롤러
# 힙(Heap)

import heapq

def solution(jobs):
    N = len(jobs) # 요청이 들어온 작업 개수
    jobs.sort() # 요청이 들어온 순서대로 정렬
    time = jobs[0][0] + jobs[0][1] # 현재 시간을 맨 첫 작업을 수행했을 때의 시간으로 초기화
    answer,cnt = jobs[0][1],1 # 요청부터 종료까지 걸린 시간과 종료된 작업 개수
    idx = 1 # 처리할 작업의 index
    heap = [] # 현재 수행할 수 있는 작업들 (현재 시간 전에 요청이 들어온 작업들)
    while cnt < N: # 전부 수행할 때까지 반복
        while idx < N: # 작업을 순서대로 처리
            job = jobs[idx] # 처리할 작업
            if job[0] > time: break # 해당 작업이 요청 시점이 현재 시간보다 뒤이면 멈춤
            heapq.heappush(heap, (job[1],job[0])) # 소요시간 기준으로 정렬하기 위해 (소요시간, 요청 시점)를 heap에 넣음
            idx += 1 # 다음 작업의 index로 갱신
        if not heap: # 수행할 수 있는 작업이 없는 경우
            cur = (job[1],job[0]) # 위에서 처리하려고 했으나 요청 시점 때문에 못한 작업을 수행
            idx += 1 # 다음 작업을 처리하기 위해 갱신
            time = cur[1] # 현재 시간을 작업 요청 시점으로 갱신
        else: cur = heapq.heappop(heap) # 소요시간이 가장 작은 작업 수행
        time += cur[0] # 현재 시간에 소요시간을 더함
        answer += time-cur[1] # 요청부터 종료까지 걸린 시간(현재 시간에서 요청 시점을 뺀 값)을 더함
        cnt += 1 # 종료된 작업 개수 갱신
    return int(answer/N) # 평균을 구해서 소수점 이하 수 버리고 반환

print(solution([[0, 3], [1, 9], [2, 6]])) # 9

print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])) # 72
print(solution([[0, 5], [2, 10], [100000000000, 2]]))