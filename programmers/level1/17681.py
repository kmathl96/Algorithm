# [1차] 비밀지도
# 2018 KAKAO BLIND RECRUITMENT

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s = ''
        num1, num2 = arr1[i], arr2[i] # 이진수로 만들 숫자
        for _ in range(n): # 이진수 비교
            if num1&1 or num2&1: s = '#'+s # 둘 중 하나 이상이 해당 자리에서의 값이 1인 경우 '#' 붙임
            else: s = ' '+s # 아닌 경우 공백 붙임
            num1,num2 = num1//2,num2//2
        answer.append(s)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])) # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])) # ["######", "### #", "## ##", " #### ", " #####", "### # "]