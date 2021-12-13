# 스티커
# 다이나믹 프로그래밍

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]

    # 스티커의 개수가 총 2개인 경우
    if n==1:
        print(max(arr[0][0],arr[1][0])) # 둘 중에 더 큰 값 출력
        continue
    
    arr[0][1] += arr[1][0] # 왼쪽 밑의 값을 더함
    arr[1][1] += arr[0][0] # 왼쪽 위의 값을 더함
    for i in range(2,n):
        # 대각선 밑의 값과 그 왼쪽 값을 비교하여 큰 값 더함
        arr[0][i] += max(arr[1][i-1],arr[1][i-2])
        # 대각선 위의 값과 그 왼쪽 값을 비교하여 큰 값 더함
        arr[1][i] += max(arr[0][i-1],arr[0][i-2])
    print(max(arr[0][-1],arr[1][-1])) # 맨 마지막 열의 두 값 중 더 큰 값 출력