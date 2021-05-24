# 큰 수 만들기
# 탐욕법(Greedy)

def solution(number, k):
    ans = ""
    idx = 0 # 탐색을 시작할 index 값
    for i in range(len(number)-k): # i번째 숫자 정하기
        mx = '0'
        for j in range(idx,i+k+1): # 시작점부터 해당 순서(i) 뒤의 k번째 숫자까지 탐색
            if mx < number[j]:
                mx = number[j]
                idx = j+1 # ans에 붙일 숫자의 index값의 다음 값 저장
            if mx == '9': break # 시간 단축하기 위함 (9이면 더 탐색할 필요가 없음)
        ans += str(mx)
    return ans

print(solution("1924", 2)) # "94"
print(solution("1231234", 3)) # "3234"
print(solution("4177252841", 4)) # "775841"

print(solution("87654321", 3)) # "87654"
print(solution("18765432", 3)) # "87654"
print(solution("77413258", 2)) # "774358"
print(solution("12345678901234567890", 19)) # "9"
print(solution("01010", 3)) # "11"
print(solution("559913", 1)) # "59913"
print(solution("9191919", 1)) # "991919"
print(solution("00100", 2)) # "100"