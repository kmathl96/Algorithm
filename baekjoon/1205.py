# 등수 구하기
# 구현

# 랭킹 리스트에 있는 점수의 개수, 태수의 새로운 점수, 랭킹 리스트에 올라갈 수 있는 점수의 개수
N,new_score,P = map(int,input().split())

# 랭킹 리스트에 점수가 있는 경우
if N:
    scores = list(map(int,input().split())) # 랭킹 리스트에 있는 점수
    
    # 랭킹 리스트가 꽉 차있는데 새 점수가 이전 점수보다 좋지 않은 경우
    if N == P and min(scores) >= new_score:
        print(-1) # 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮으므로 -1 출력
    else:
        scores.append(new_score) # 새로운 점수 넣기
        
        # 등수 = 오름차순 정렬했을 때의 인덱스값 + 1
        print(sorted(scores,reverse=1).index(new_score)+1)

# 랭킹 리스트에 점수가 없는 경우 => 1등
else: print(1)