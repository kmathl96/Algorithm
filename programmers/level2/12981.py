# 영어 끝말잇기
# Summer/Winter Coding(~2018)

def solution(n, words):
    for i in range(1,len(words)): # 두 번째 단어부터 시작
        # 1. 해당 단어가 이미 나왔거나 (중복)
        # 2. 해당 단어의 첫 글자와 앞의 단어의 마지막 글자와 일치하지 않은 경우
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]:
            return [i%n+1,i//n+1] # 해당 사람의 번호(i%n+1)와 차례(i//n+1) 출력
    # 규칙에 한번도 걸리지 않았다면 [0,0] 출력
    return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [3,3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0,0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # [1,3]