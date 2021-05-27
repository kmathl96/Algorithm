# [1차] 캐시
# 2018 KAKAO BLIND RECRUITMENT

from collections import deque

def solution(cacheSize, cities):
    if not cacheSize: # 캐시 크기가 0인 경우
        return 5*len(cities) # 모든 경우가 cache miss
    answer = 0 # 실행 시간
    cache = deque()
    for city in cities:
        city = city.upper() # 대소문자 구분하지 않으므로 대문자로 통일
        # 1. cache hit
        if city in cache:
            answer += 1
            cache.remove(city) # 캐시에서 해당 도시 삭제
        # 2. cache miss
        else:
            answer += 5
            if len(cache) == cacheSize: # 캐시가 다 찬 경우
                cache.popleft() # 처음 데이터(제일 예전에 처리) 삭제
        cache.append(city) # 캐시에 해당 도시 저장
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25