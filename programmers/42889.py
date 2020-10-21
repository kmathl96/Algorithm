# 실패율
# 2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    fail = []
    cnt = len(stages)
    for i in range(N):
        if cnt == 0: fail.append((i+1,1))
        else: fail.append((i+1,(cnt-stages.count(i+1))/cnt))
        cnt -= stages.count(i+1)
    return [idx for idx,v in sorted(fail, key=lambda x: (x[1], x[0]))]

print(solution(5,[2,1,2,6,2,4,3,3])) # [3,4,2,1,5]
print(solution(4,[4,4,4,4,4])) # [4,1,2,3]
print(solution(8,[1,2,3,4,5,6,7])) # [7,6,5,4,3,2,1,8]