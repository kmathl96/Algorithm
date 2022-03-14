# 올림픽
# 구현, 정렬

import sys
input = sys.stdin.readline

N,K = map(int,input().split()) # 국가의 수, 등수를 알고 싶은 국가

# 메달 정보 저장
medals = []
for _ in range(N):
    num,g,s,b = map(int,input().split()) # 국가를 나타내는 정수와 이 국가가 얻은 금, 은, 동메달의 수
    medals.append([[g,s,b],num])

# 등수 구하기
medals.sort(reverse=1) # 내림차순으로 정렬
rank,cnt,pre = 0,1,[0,0,0] # 등수, 동점자 수, 이전 등수의 메달 수
for i in range(N):
    # 이전 등수와 메달 수가 같은 경우
    if pre == medals[i][0]:
        cnt += 1 # 동점자 수 증가
    # 이전 등수와 메달 수가 다른 경우, 더 등수가 낮음
    else:
        pre = medals[i][0] # 이전 등수의 메달 수 갱신
        rank += cnt # 등수 갱신
        cnt = 1 # 동점자 수 초기화
    
    # 등수를 알고 싶은 국가인 경우, 종료
    if medals[i][1] == K: break

# 국가 K의 등수 출력
print(rank)