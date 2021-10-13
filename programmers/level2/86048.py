# 입실 퇴실

def solution(enter, leave):
    answer = [0]*len(enter)
    st = [] # 입실해있는 사람
    idx = 0 # 입실할 사람의 인덱스 값

    # 퇴실 순서대로 확인
    for num in leave:

        # 아직 입실하지 않은 경우, 해당 사람이 입실할 때까지 입실 반복
        while num not in st:
            st.append(enter[idx]) # 입실 순서대로 입실
            idx += 1 # 다음 입실할 사람
        
        st.pop(st.index(num)) # 퇴실

        # 마주친 사람들 횟수 세기
        for n in st:
            answer[n-1] += 1
            answer[num-1] += 1
    return answer

print(solution([1,3,2], [1,2,3])) # [0,1,1]
print(solution([1,4,2,3], [2,1,3,4])) # [2,2,1,3]
print(solution([3,2,1], [2,1,3])) # [1,1,2]
print(solution([3,2,1], [1,3,2])) # [2,2,2]
print(solution([1,4,2,3], [2,1,4,3])) # [2,2,0,2]