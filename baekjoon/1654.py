# 랜선 자르기
# 이분 탐색, 매개 변수 탐색

K,N = map(int,input().split()) # 이미 가지고 있는 랜선 개수, 필요한 랜선 개수
LANs = [int(input()) for _ in range(K)] # 가지고 있는 랜선들의 길이

# 이분 탐색
start,end = 1,max(LANs) # 랜선의 길이의 최솟값과 최댓값으로 초기화
while start<=end:
    mid = (start+end)//2 # 가운데 값
    # 만들어진 랜선 개수(각 랜선을 mid 값으로 나눴을 때의 몫의 합)가 N 이상인 경우, start값 갱신
    if sum([num//mid for num in LANs]) >= N: start = mid+1
    else: end = mid-1 # 아닌 경우, end 값 갱신
print(end) # end 값 반환 (만들 수 있는 최대 랜선의 길이)