# 빗물
# 구현, 시뮬레이션

H,W = map(int,input().split())
blocks = list(map(int,input().split()))
water = 0
idx = 0
while idx < W-1:
    height = blocks[idx]
    new_idx = idx+1
    temp_height = blocks[idx+1]
    is_changed = 0
    for j in range(idx+1,W):
        if height <= blocks[j]:
            is_changed = 1
            new_idx = j
            break
        elif temp_height < blocks[j]:
            temp_height = blocks[j]
            new_idx = j
    if not is_changed: height = temp_height
    for k in range(idx+1,new_idx):
        water += height-blocks[k]
    idx = new_idx
print(water)