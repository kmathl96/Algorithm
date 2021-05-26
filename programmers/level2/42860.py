# 조이스틱
# 탐욕법(Greedy)

def solution(name):
    answer = 0
    name = list(name)
    N = len(name)
    idx = 0 # 커서 위치
    while name.count('A') != N: # A가 아닌 문자가 있을 경우 반복
        s = name[idx] # 해당 위치의 알파벳
        if s != 'A': # A가 아닌 경우
            answer += min(ord(s)-65, 91-ord(s)) # 위/아래 중 A와 가까운 방향으로 이동
            name[idx] = 'A'
        for i in range(1,N//2+1): # 양쪽으로 탐색
            if name[(idx+i)%N] != 'A': # 오른쪽으로 탐색
                idx += i # 커서 위치 이동
                answer += i # 이동한 만큼 증가
                break
            if name[(idx-i)%N] != 'A': # 왼쪽으로 탐색
                idx -= i
                answer += i
                break
    return answer

print(solution("JEROEN")) # 56
print(solution("JAN")) # 23

print(solution("BBBAAAB")) # 9
print(solution("ABABAAAAABA")) # 11