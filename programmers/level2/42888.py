# 오픈채팅방
# 2019 KAKAO BLIND RECRUITMENT

def solution(record):
    answer = []
    users = {} # 아이디와 닉네임 저장
    for r in record:
        r = r.split()
        u_id = r[1]
        if r[0] != 'Leave':
            users[u_id] = r[2]
    for r in record:
        r = r.split()
        u_id = r[1]
        if r[0] == 'Enter':
            answer.append(users[u_id] + "님이 들어왔습니다.")
        elif r[0] == 'Leave':
            answer.append(users[u_id] + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])) # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]