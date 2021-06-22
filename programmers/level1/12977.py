# 소수 만들기
# Summer/Winter Coding(~2018)

from itertools import combinations

# 소수 리스트 만들기
primes = [2,3]
for num in range(5,3000):
    is_prime = 1
    for p in primes:
        if not num%p: # 어떤 수로 나누어 떨어지는 경우 소수가 아님
            is_prime = 0
            break
    if is_prime: primes.append(num)

def solution(nums):
    answer = 0
    for case in combinations(nums, 3): # 원소의 개수가 3인 모든 조합
        if sum(case) in primes: answer += 1 # 합이 소수인 경우 답 갱신
    return answer

print(solution([1,2,3,4])) # 1
print(solution([1,2,7,6,4])) # 4