# 빗물
# 구현, 시뮬레이션

H,W = map(int,input().split()) # 세로 길이와 가로 길이
blocks = list(map(int,input().split())) # 블록이 쌓인 높이
water = 0 # 고이는 빗물의 양
idx = 0 # 기준 블록의 인덱스 값
while idx < W-1:
    height = blocks[idx] # 빗물이 쌓이는 높이 : 기준 블록의 높이로 초기화
    new_idx = idx+1 # 다음 기준이 될 블록의 인덱스 값 : 다음 인덱스로 초기화
    flag = 0 # 기준 블록 높이 이상인 블록의 존재 여부
    
    # 기준 블록의 높이 이상인 블록이 없을 경우
    # 그 중 최대 높이만큼 빗물이 쌓임
    # 다음 블록의 높이로 초기화
    temp_height = blocks[idx+1]
    
    # 기준 블록의 오른쪽 블록들 탐색하면서 다음 기준 블록 갱신
    for j in range(idx+1,W):
        if height <= blocks[j]: # 기준 블록의 높이 이상인 경우 탐색 종료
            flag = 1
            new_idx = j
            break
        elif temp_height < blocks[j]: # 탐색한 블록들 중에서 제일 높이가 큰 블록인 경우
            temp_height = blocks[j] # 오른쪽 블록들 높이 중 최댓값 갱신
            new_idx = j
    
    # 기준 블록보다 높은 블록이 없다면 그 중에서 제일 높은 것만큼 빗물이 쌓임
    if not flag: height = temp_height
    
    # 기준 블록부터 다음 기준 블록까지 빗물이 고인 양 더하기
    for k in range(idx+1,new_idx):
        water += height-blocks[k]

    idx = new_idx # 기준 블록의 인덱스 값 갱신

print(water)