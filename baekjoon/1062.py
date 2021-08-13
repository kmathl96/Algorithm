# 가르침
# 브루트포스, 비트마스킹, 백트래킹

from itertools import combinations

# 배워야 하는 글자들을 이진수로 변환
def to_binary(arr):
    res = 0
    for s in arr: # 단어를 읽기 위해 배워야 하는 글자
        res |= (1<<ord(s)-97) # 합집합
    return res

N,K = map(int,input().split()) # 단어의 개수, 가르칠 글자의 개수
antatica = set('antic') # 기본 단어 anta, tica
base = to_binary(list('antic')) # 기본으로 알아야 할 단어

# 남극 언어의 단어 저장 (중복된 글자와 'a', 'n', 't', 'i', 'c' 제거)
words = [set(input())-antatica for _ in range(N)]

ans = 0 # 읽을 수 있는 단어의 최대 개수
if K > 4: # 기본 단어를 알아야 하므로 5 이상이어야 함
    # 단어들을 읽기 위해 배워야 하는 모든 글자들
    need_str = set(s for word in words for s in word)

    # 이진수로 변환된 단어 집합
    binary_words = [to_binary(word) for word in words]
    
    # 가르칠 글자 개수(K-기본 단어 구성 글자 5개)가 배워야 하는 글자보다 많은 경우
    if len(need_str) <= K-5: ans = N # 모든 단어를 읽을 수 있음
    else:
        # 배워야 하는 글자들 (K-5)개로 구성된 모든 조합
        for c in combinations(need_str, K-5):

            # 배운 글자들 => XOR(^)을 이용해 뒤집음 => 배우지 않은 글자들
            not_learned = (base | to_binary(c)) ^ ((1<<26)-1)

            # 배우지 않은 글자들과 겹치는 글자가 없다면 1, 있다면 0
            # 총합 = 읽을 수 있는 단어의 개수
            cnt = sum(0 if not_learned&word else 1 for word in binary_words)
            if cnt > ans: ans = cnt # 최대 개수 갱신
print(ans)