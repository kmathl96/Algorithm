# [3차] 방금그곡
# 2018 KAKAO BLIND RECRUITMENT

# 멜로디를 리스트에 넣기
def melody_list(melody):
    N = len(melody) # 멜로디의 길이
    lst,idx = [],0 # 각 노트를 넣을 리스트와 처리할 노트의 index값
    while idx < N:
        # 뒷 문자가 #인 경우, #까지 같이 처리하고 # 다음 문자로 index 갱신
        if idx < N-1 and melody[idx+1]=='#':
            lst.append(melody[idx:idx+2])
            idx += 2
        # 아닌 경우, 해당 문자 넣고 그다음 문자로 index 갱신
        else:
            lst.append(melody[idx:idx+1])
            idx += 1
    return lst

def solution(m, musicinfos):
    # 각 음악이 실제로 재생된 멜로디 만들기
    new_musicinfos = [] # 각 음악의 제목과 재생된 멜로디를 넣을 리스트
    for i in range(len(musicinfos)):
        start,end,title,info = musicinfos[i].split(',') # 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
        time = (int(end[:2])-int(start[:2]))*60 + int(end[3:5])-int(start[3:5]) # 재생된 시간
        info_list = melody_list(info) # 해당 음악의 악보 정보를 리스트로 만들기
        N = len(info_list) # 악보의 길이
        info = info_list * (time//N) + info_list[:time%N] # 재생된 시간 만큼 악보 정보를 이어붙임
        new_musicinfos.append([title,info]) # 음악 제목과 재생된 멜로디 리스트 넣기
    
    # 재생된 음악들이 네오가 기억한 멜로디와 얼마나 일치하는지 확인
    m_list = melody_list(m) # 네오가 기억한 멜로디를 리스트로 만들기
    M = len(m_list)
    # 일치하는 최대 노트 개수(최소 : 네오 멜로디의 노트 개수), 그 경우의 재생 시간과 answer를 초기화
    mx_cnt,mx_t,answer = M,0,'(None)'
    for title,info in new_musicinfos: # 음악의 제목과 재생된 멜로디
        t = len(info) # 재생된 시간
        for s in range(t): # 시작하는 index값
            if m_list[0] != info[s]: continue # 해당 노트가 네오의 멜로디 시작 노트와 다를 경우 넘어감
            cnt = 0 # 노트 일치 횟수
            for i in range(min(M,t-s)):
                if m_list[i] == info[s+i]: cnt += 1 # 노트가 일치하면 cnt 갱신
                else: break # 일치하지 않는 경우, 종료
            # 일치 홋수는 같고 재생시간이 더 긴 경우 또는 일치 횟수가 더 큰 경우
            if (mx_cnt == cnt and mx_t < t) or mx_cnt < cnt:
                answer,mx_cnt,mx_t = title,cnt,t # answer, 최대 일치 횟수와 해당 음악의 재생 시간을 갱신
    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "HELLO"
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) # "FOO"
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "WORLD"