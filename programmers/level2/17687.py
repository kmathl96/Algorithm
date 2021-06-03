# [3차] n진수 게임
# 2018 KAKAO BLIND RECRUITMENT

# n진수를 만들기 위해 0~F의 값을 미리 저장
nums = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def solution(n, t, m, p):
    answer = '0' # 0은 먼저 붙임
    for num in range(t*m):
        temp = '' # n진수를 만든 후 answer에 붙임
        while num: # n진수 만들기
            temp = nums[num%n] + temp # n진수는 나머지가 앞에 붙음
            num = num//n
        answer += temp # n진수를 붙임
    return "".join([answer[i] for i in range(p-1,t*m,m)]) # 튜브의 순서에 맞는 글자들만 출력

print(solution(2, 4, 2, 1)) # "0111"
print(solution(16, 16, 2, 1)) # "02468ACE11111111"
print(solution(16, 16, 2, 2)) # "13579BDF01234567"