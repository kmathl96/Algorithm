# 입국심사
# 이분탐색

def solution(n, times):
    start,end = 1,max(times)*n # 모든 사람이 심사를 받는 데 걸리는 시간의 최솟값과 최댓값
    while start<=end:
        mid = (start+end)//2
        # 해당 시간(mid) 내에 각 심사관이 심사할 수 있는 사람 수 = 각 심사 시간(time)으로 mid를 나눈 값
        # 심사할 수 있는 사람 수의 총합이 n명보다 많은 경우, end 갱신
        if n <= sum([mid//time for time in times]): end = mid-1
        else: start = mid+1 # n명보다 적은 경우, start 값 갱신
    return start # 최솟값을 반환

print(solution(6, [7,10])) # 28