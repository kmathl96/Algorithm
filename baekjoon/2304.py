# 창고 다각형
# 브루트포스, 스택

N = int(input())

# 기둥의 높이를 저장
arr = [0]*1001
for _ in range(N):
    x,y = map(int,input().split())
    arr[x] = y

# 기둥의 높이 중 최댓값과 그 위치
ans = max(arr)
mx_idx = arr.index(ans)

# 왼쪽에서부터 접근
left,cur = 0,0 # 위치와 높이 초기화
for i in range(mx_idx+1): # 최대 높이의 기둥의 위치까지 수행
    if arr[i] >= cur: # 같은 높이의 지붕을 가짐
        ans += cur*(i-left) # 위치의 차이*기둥의 높이 만큼 더함
        cur = arr[i] # 해당 기둥의 높이 저장
        left = i # 해당 기둥의 위치 저장
# 오른쪽에서부터 접근
right,cur = 0,0
for i in range(1000,mx_idx-1,-1):
    if arr[i] >= cur:
        ans += cur*(right-i)
        cur = arr[i]
        right = i
print(ans)