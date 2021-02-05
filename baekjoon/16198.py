# 에너지 모으기
# 브루트 포스

def f(arr,w): # 재귀함수
    global ans
    if len(arr)==2: # 첫번째와 마지막 구슬만 남으면 종료
        if ans < w: ans = w # 에너지값이 최대일 경우 갱신
        return
    for i in range(1,len(arr)-1):
        p = arr.pop(i) # 구슬 제거
        # i번째 구슬을 제거했으므로 i-1번째, i번째 구슬의 곱을 현재 에너지에 더함
        f(arr,w+arr[i-1]*arr[i])
        arr.insert(i,p) # 다음을 위해 제자리에 다시 구슬 넣기