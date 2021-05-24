# 최댓값과 최솟값

def solution(s):
    arr = list(map(int,s.split()))
    return f'{min(arr)} {max(arr)}'

print(solution("1 2 3 4")) # "1 4"
print(solution("-1 -2 -3 -4")) # "-4 -1"
print(solution("-1 -1")) # "-1 -1"