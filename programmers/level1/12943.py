# 콜라츠 추측

def solution(num):
    answer = 0 # 작업 횟수
    for _ in range(500): # 500번 반복
        if num==1: return answer # 1이 되면 answer 반환
        if num&1: num = num*3+1 # 홀수 - 3을 곱하고 1 더함
        else: num //= 2 # 짝수 - 2로 나눔
        answer += 1 # 작업 횟수 갱신
    return -1 # 500번 반복해도 1이 되지 않으면 -1 반환

print(solution(6)) # 8
print(solution(16)) # 4
print(solution(626331)) # -1