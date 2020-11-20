# 예산
# Summer/Winter Coding(~2018)

def solution(d, budget):
    answer = 0
    for i in sorted(d):
        if budget - i < 0: break
        budget -= i
        answer += 1
    return answer

print(solution([1,3,2,5,4],9)) # 3
print(solution([2,2,3,3],10)) # 4