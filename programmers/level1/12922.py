# 수박수박수박수박수박수?

def solution(n):
    return "".join(['박' if i%2 else '수' for i in range(n)])

print(solution(3)) # '수박수'
print(solution(4)) # '수박수박'