# JadenCase 문자열 만들기

def solution(s):
    s = list(s)
    for i in range(len(s)):
        if i and s[i-1] != ' ': # 그 전 문자가 공백이 아닌 경우 소문자로 변경
            s[i] = s[i].lower()
        else: s[i] = s[i].upper() # 그 외는 대문자로 변경
    return "".join(s)

print(solution("3people unFollowed me")) # "3people Unfollowed Me"
print(solution("for the last week")) # "For The Last Week"