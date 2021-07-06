# 베스트앨범
# 해시

def solution(genres, plays):
    # 각 장르에 속하는 노래들과 총 재생 횟수를 딕셔너리로 만듦
    genres_dic = {genre: [] for genre in set(genres)} # 각 장르에 속하는 노래들의 고유 번호
    genres_cnt = {genre: 0 for genre in set(genres)} # 각 장르의 총 재생 횟수
    for i in range(len(genres)):
        genres_dic[genres[i]].append((plays[i],i)) # (재생 횟수, 고유 번호)
        genres_cnt[genres[i]] += plays[i] # 해당 장르의 총 재생 횟수에 더함

    # 리스트로 만들어서 총 재생 횟수를 기준으로 장르를 내림차순 정렬
    cnts = [(genres_cnt[k],k) for k in genres_dic.keys()]
    cnts.sort(key=lambda x: -x[0])

    # 베스트앨범에 들어갈 노래 넣기
    answer = []
    for cnt,genre in cnts:
        # 해당 장르의 음악들을 재생 횟수 기준 내림차순, 고유 번호 기준 오름차순 정렬
        musics = sorted(genres_dic[genre], key=lambda x: (-x[0],x[1]))
        for i in range(min(len(musics),2)): # 음악이 하나이면 1개, 그 이상이면 2개 넣기
            answer.append(musics[i][1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]