# 프린터 큐
# 큐

from collections import deque

for _ in range(int(input())): # 테스트케이스의 수만큼 반복
    N,M = map(int,input().split()) # 문서의 개수와 몇 번째로 인쇄되었는지 궁금한 문서
    docs = list(map(int,input().split())) # 문서의 중요도
    q = deque(range(N)) # 문서 번호
    cnt = 0 # 인쇄 횟수
    while q:
        idx = q.popleft() # 가장 앞에 있는 문서의 번호
        # 해당 문서의 중요도가 중요도의 최댓값보다 작은 경우
        # (= 나머지 문서들 중 중요도가 높은 문서가 있음)
        if docs[idx] < max(docs): q.append(idx) # 가장 뒤에 재배치
        else: # 그렇지 않은 경우, 인쇄
            docs[idx] = 0 # 중요도를 0으로 변경
            cnt += 1 # 인쇄 횟수 증가
            if idx == M: break # 궁금한 문서인 경우 종료
    print(cnt)