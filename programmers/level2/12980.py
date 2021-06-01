# 점프와 순간 이동
# Summer/Winter Coding(~2018)

def solution(n):
    ans = 0
    while n: # n 위치에서부터 거꾸로 0으로 가기
        if n&1: ans += 1 # 2로 나눠지지 않는 경우 1칸 점프
        n = n//2 # 순간이동
    return ans

print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5