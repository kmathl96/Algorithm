# DSLR
# BFS

from collections import deque

cmd = ['D','S','L','R'] # 명령어
for _ in range(int(input())): # 테스트 케이스 개수 만큼 반복
    A,B = map(int,input().split()) # 레지스터의 초기 값, 최종 값
    visited = [0]*10000 # 중복 체크 방지
    visited[A] = 1
    q = deque([(A,'')]) # 명령어 나열
    while q:
        n,s = q.popleft() # 레지스터의 값과 명령어 나열

        # 최종 값과 일치하는 경우, 명령어 나열을 출력하고 종료
        if n == B:
            print(s)
            break

        # 명령어를 순서대로 실행
        nums = [(2*n)%10000,(n-1)%10000,(n*10+n//1000)%10000,n%10*1000+n//10] # 결과 값
        for i in range(4):
            if not visited[nums[i]]: # 아직 체크한 적 없는 값인 경우
                q.append((nums[i],s+cmd[i])) # 결과 값과 명령어 나열을 갱신하여 큐에 넣기
                visited[nums[i]] = 1