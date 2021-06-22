# 폰켓몬
# 찾아라 프로그래밍 마에스터

def solution(nums):
    # set으로 중복 값을 제거하면 폰켓몬 종류 수를 구할 수 있음 (=len(set(nums)))
    # 1) 폰켓몬의 종류가 N/2보다 많으면, 최대 N/2가지 종류를 선택할 수 있음
    # 2) 폰켓몬의 종류가 N/2마리보다 적으면, 최대로 선택할 수 있는 종류 수는 폰켓몬의 종류 수와 같음 
    return min(len(nums)//2,len(set(nums))) 

print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2