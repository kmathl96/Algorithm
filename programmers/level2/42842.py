# 카펫
# 완전탐색

def solution(brown, yellow):
    tot = brown + yellow # 격자의 총 개수
    col = 3 # 가로 길이

    while True:
        row = tot//col # 세로 길이

        # 1. 격자의 총 개수가 가로 길이로 나눈 것이 세로 길이이므로, 나누어 떨어져야 함
        # 2. 문제의 제한 사항 : 가로 길이 >= 세로 길이
        # 3. 갈색 격자의 개수가 계산한 값과 일치하는지 판단
        if not tot%col and row <= col and brown == 2*(row+col-2):
            return [col,row]
            
        col += 1 # 해당 경우가 답이 아닐 경우 가로 길이를 증가시켜서 반복

print(solution(10, 2)) # [4, 3]
print(solution(8, 1)) # [3, 3]
print(solution(24, 24)) # [8, 6]