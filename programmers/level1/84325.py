# 직업군 추천하기

def solution(table, languages, preference):
    answer = ['',0] # 직업군, 점수
    for row in table:
        priority = list(row.split()) # 직업군과 5가지 언어의 점수
        
        # 점수 = (직업군 언어 점수)*(언어 선호도)의 총합
        # 직업군의 언어를 5가지를 확인하면서, 선호하는 언어인 경우 계산
        # 1. 직업군 언어 점수 : priority의 1~5열 => 5~1점 => i열 언어의 점수는 6-i
        # 2. 언어 선호도 : 해당 언어의 선호 점수를 구함 => preference[languages.index(priority[i])
        score = sum((6-i)*preference[languages.index(priority[i])] for i in range(1,6) if priority[i] in languages)
        
        # 현재 답보다 점수가 더 높거나
        # 점수가 같으면서 직업군 이름이 더 빠른 경우
        if answer[1] < score or (answer[1]==score and answer[0] > priority[0]):
            answer = [priority[0],score] # 답 변경
    
    return answer[0] # 점수가 가장 높은 직업군 반환

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5])) # "HARDWARE"
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5])) # "PORTAL"