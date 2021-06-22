# 핸드폰 번호 가리기

def solution(phone_number):
    # '*'을 (전화번호 길이-4)만큼 + 전화번호 끝 4자리
    return '*'*(len(phone_number)-4)+phone_number[-4:]

print(solution("01033334444")) # "*******4444"
print(solution("027778888")) # "*****8888"