# 숫자 문자열과 영단어
# 2021 카카오 채용연계형 인턴십

# 각 숫자에 대응되는 영단어 리스트 (index 값과 일치)
nums = ['zero','one','two','three','four','five','six','seven','eight','nine']

def solution(s):
    for i in range(len(nums)):
        s = s.replace(nums[i], str(i)) # 숫자 i에 대응되는 영단어를 i로 변경
    return int(s) # 숫자로 반환

print(solution("one4seveneight")) # 1478
print(solution("23four5six7")) # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123")) # 123