# 소수 찾기
# 완전탐색

from itertools import permutations

def solution(numbers):
    nums = []
    n = list(numbers)
    for i in range(1,len(n)+1):
        nums += list(map(int,map("".join, set(permutations(n,i)))))
    answer = 0
    for j in set(nums):
        if j < 2: continue
        is_prime = True
        for k in range(2,int(j**0.5)+1):
            if j%k == 0: # 나눠지면 소수가 아님
                is_prime = False
                break
        if is_prime: answer += 1
    return answer

print(solution("17")) # 3
print(solution("011")) # 2