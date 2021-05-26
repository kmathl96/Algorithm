# 다음 큰 숫자

# 2진수로 변환했을 때 1의 개수 세기
def cnt1(num,N):
    cnt = 0
    while num>0:
        if num&1: cnt += 1
        if cnt > N: # 1의 개수가 N보다 커질 경우 답이 아니므로 바로 0을 반환하여 시간 단축
            return 0
        num = num//2
    return cnt

def solution(n):
    answer = n
    N = cnt1(n,1001)
    while True: # 답을 찾을 때까지 1씩 증가시키며 반복
        answer += 1
        if cnt1(answer,N)==N: break
    return answer

print(solution(78)) # 83
print(solution(15)) # 23