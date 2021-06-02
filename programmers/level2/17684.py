# [3차] 압축
# 2018 KAKAO BLIND RECRUITMENT

def solution(msg):
    answer = []
    # 1. 사전 초기화
    dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    N = len(msg) # 주어진 문자열의 길이
    max_length = 1 # 사전에 있는 단어들 중 가장 긴 단어의 길이
    next_idx = 27 # 사전에 들어갈 다음 단어의 색인 번호
    idx = 0 # 처리할 문자(w)의 index 값
    while idx < N:
        # 2. 사전에서 현재 문자열과 일치하는 가장 긴 문자열 w를 찾음
        # w의 길이는, 가질 수 있는 최대 길이(max_length와 남은 문자열의 길이 중 더 작은 값)부터 1씩 감소시키면서 w 찾기
        for l in range(min(max_length,N-idx),0,-1):
            w = msg[idx:idx+l]
            if w not in dic.keys(): continue # 사전에 없는 경우 넘김
            answer.append(dic[w]) # 3. answer에 w에 해당하는 색인 번호 넣기
            if idx+l+1 < N: # 그 다음 글자가 있는 경우
                wc = msg[idx:idx+l+1] # w+c
                if wc not in dic: # 4. 사전에 없는 경우 넣기
                    dic[wc] = next_idx
                    next_idx += 1 # 다음 색인 번호 갱신
                    max_length = max(max_length, len(wc)) # w+c의 길이가 더 길다면 max_length 갱신
            idx += len(w) # w의 길이만큼 index 값 더해주기
            break # 해당 문자가 사전에 있었으므로 종료하고 다음 문자 처리
    return answer

print(solution("KAKAO")) # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB")) # [1, 2, 27, 29, 28, 31, 30]