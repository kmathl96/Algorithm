# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    return [x*(i+1) for i in range(n)] # x의 배수를 n개 만큼 리스트에 넣어 반환

print(solution(2, 5)) # [2,4,6,8,10]
print(solution(4, 3)) # [4,8,12]
print(solution(-4, 2)) # [-4, -8]