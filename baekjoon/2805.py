# 나무 자르기
# 이분 탐색

N,M = map(int,input().split()) # 나무 개수, 필요한 나무 길이
trees = list(map(int,input().split())) # 각 나무의 길이
start,end = 0,max(trees) # 절단기의 높이의 최솟값과 최댓값으로 초기화
while start <= end:
    mid = (start+end)//2 # 중간 값

    # 가져갈 나무의 길이(= 높이에 맞게 자르고난 나머지의 합)가 M보다 크거나 같으면 start값 갱신
    # 절단기의 높이보다 나무가 작은 경우, 두 값의 차가 아니라 0으로 계산해야 함
    # 1. max(length-mid, 0)으로 계산한 경우, 시간 초과
    # 2. length-mid if length > mid else 0으로 계산한 경우 Pass
    if sum([length-mid if length>mid else 0 for length in trees]) >= M: start = mid+1
    else: end = mid-1 # 가져갈 나무의 길이가 M보다 작으면 end값 갱신
print(end)