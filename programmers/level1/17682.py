# [1차] 다트 게임
# 2018 KAKAO BLIND RECRUITMENT

def solution(dartResult):
    answer = [] # 각 기회마다 얻은 점수를 넣을 리스트
    idx = 0 # 탐색 위치 초기화
    while idx < len(dartResult):
        val = dartResult[idx] # 탐색할 문자
        if val in '1234567890': # 정수인 경우
            if dartResult[idx+1] == '0': # 뒷문자가 0인 경우 = 10점
                answer.append(10) # 숫자 넣기
                idx += 1 # 뒷문자(0)는 탐색하지 않으므로 idx 값을 1 증가 (맨밑에 idx 값을 1 증가시킬 것)
            else: answer.append(int(val)) # 숫자 넣기
        elif val == 'D': answer[-1] = answer[-1]**2 # 점수 제곱
        elif val == 'T': answer[-1] = answer[-1]**3 # 점수 세제곱
        elif val == '*': # 스타상의 경우
            answer[-1] *= 2 # 점수 두 배
            if len(answer) > 1: answer[-2] *= 2 # 직전 점수가 있을 경우 그 점수도 두 배
        elif val == '#': answer[-1] = -answer[-1] # 아차상의 경우 마이너스
        idx += 1 # 다음 문자 탐색
    return sum(answer) # 점수 총합 출력

print(solution('1S2D*3T')) # 37
print(solution('1D2S#10S')) # 9
print(solution('1D2S0T')) # 3
print(solution('1S*2T*3S')) # 23
print(solution('1D#2S*3S')) # 5
print(solution('1T2D3D#')) # -4
print(solution('1D2S3T*')) # 59