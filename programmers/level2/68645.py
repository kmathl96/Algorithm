# 삼각 달팽이
# 월간 코드 챌린지 시즌1

def solution(n):
    answer = [[] for _ in range(n)] # n행을 갖는 이차원 리스트
    d = 0 # 숫자를 채우는 방향 (0: 아래 방향; 1: 오른쪽 방향; 2: 위 방향)
    r = 0 # 숫자를 채우는 행
    cnt = 0 # 반시계 방향(0-1-2)을 채운 횟수
    num = 1 # 채울 숫자
    while num < n*(n+1)//2+1: # 숫자를 다 채울 때까지 반복
        if not d: # 아래로 채우기
            answer[r].insert(cnt,num) # 왼쪽에서 cnt번째에 숫자 넣기
            num += 1
            r += 1 # 아래 행으로 가기
            if r == n-cnt-1: d = 1 # 오른쪽으로 숫자를 채워야 함 (방향 바꾸기)
        elif d == 1: # 오른쪽으로 채우기
            answer[r] = answer[r][0:cnt] + list(range(num,num+r-2*cnt)) + answer[r][cnt:] # num부터 r-2*cnt개의 숫자 넣기
            num += r-2*cnt # 숫자를 넣은 만큼 num 증가
            d = 2 # 방향 바꾸기
        else: # 위로 채우기
            answer[r].insert(len(answer[r])-cnt,num) # 오른쪽에서 cnt번째에 숫자 넣기
            num += 1
            r -= 1 # 위 행으로 가기
            if len(answer[r]) == r: # 해당 행에 숫자가 다 채워졌을 경우
                cnt += 1 # 반시계 방향으로 숫자를 채웠으므로 증가
                d = 0 # 방향 바꾸기
    return [number for row in answer for number in row] # 모든 행의 숫자를 하나의 행으로 반환

print(solution(4)) # [1,2,9,3,10,8,4,5,6,7]
print(solution(5)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6)) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]