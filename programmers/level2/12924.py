# 숫자의 표현

def solution(n):
    answer = 1 # 자기자신으로 표현 가능
    for i in range(1,n):
        for j in range(i+1,n):
            sum_ = j*(j+1)//2 - i*(i-1)//2 # 1~j 합에서 1~(i-1) 합을 빼면 i~j 합
            if sum_ == n: answer += 1 # 답 갱신
            if sum_ >= n: break # n보다 커지면 멈춤
    return answer

print(solution(15)) # 4