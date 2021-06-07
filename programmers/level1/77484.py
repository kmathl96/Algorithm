# 로또의 최고 순위와 최저 순위
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)

def solution(lottos, win_nums):
    min_cnt = len(set(lottos)&set(win_nums)) # 최소 일치 개수는 겹치는 숫자의 개수
    max_cnt = min_cnt + lottos.count(0) # 최대 일치 개수는 최솟값에 0의 개수를 더한 값
    # 일치 개수에 맞게 순위 반환 (2보다 작은 경우 순위는 6)
    return [6 if max_cnt<2 else 7-max_cnt, 6 if min_cnt<2 else 7-min_cnt]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # [1, 1]