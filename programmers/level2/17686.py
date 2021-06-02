# [3차] 파일명 정렬
# 2018 KAKAO BLIND RECRUITMENT

def solution(files):
    filenames = [] # 각 파일 이름을 HEAD, NUMBER, TAIL로 나눠서 저장할 리스트
    for filename in files:
        for i in range(len(filename)):
            s1 = ord(filename[i])
            if 48 <= s1 <= 57: # 숫자인 경우
                head = filename[:i] # 첫 문자부터 그전 문자까지 HEAD
                number = filename[i:i+5] # 5글자는 NUMBER로 저장
                tail = filename[i+5:] # 그 뒤의 문자열은 TAIL
                for j in range(len(number)): # NUMBER 안에 문자가 있는지 찾기
                    s2 = ord(number[j])
                    if s2 < 48 or s2 > 57: # 숫자가 아닌 경우 NUMBER, TAIL 변경 후 종료
                        number = filename[i:i+j]
                        tail = filename[i+j:]
                        break
                filenames.append([head,number,tail])
                break
    # 1. HEAD 기준으로 정렬 - 대소문자 구분을 하지 않으므로 소문자로 바꿔서 처리
    # 2. NUMBER 기준으로 정렬 - 문자열로 저장돼있으므로 숫자로 바꿔서 처리
    filenames.sort(key=lambda x: (x[0].lower(),int(x[1])))
    return ["".join(map(str,filename)) for filename in filenames] # HEAD, NUMBER, TAIL로 나뉘어있는 각 파일을 다시 문자열로 만들어서 반환

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])) # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])) # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

print(solution(["foo9.txt", "foo010bar020.zip", "F-15", "F15"])) # ['F15', 'F-15', 'foo9.txt', 'foo010bar020.zip']