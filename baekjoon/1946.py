# 신입 사원
# 그리디, 정렬

import sys
input = sys.stdin.readline

def sol():
    ans = [] # 각 테스트 케이스의 결과를 넣을 리스트
    # 입력된 테스트 케이스의 개수만큼 반복
    for _ in range(int(input())):
        N = int(input()) # 지원자의 숫자

        # 지원자의 성적 순위를 저장
        grade = [0]*N # grade[i] = 서류심사 (i+1)위인 지원자의 면접 성적 순위
        for i in range(N):
            s1,s2 = map(int,input().split()) # 서류심사 성적, 면접 성적의 순위
            grade[s1-1] = s2
        
        # 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원 수 구하기
        cnt = 0 # 선발하는 인원 수
        
        # 서류심사 성적 순서대로 탐색
        # 본인보다 서류심사 성적이 높은 사람 중에서 면접 성적이 높은 사람이 있으면 선발되지 못함
        pre = grade[0] # 서류심사 성적 순위가 높은 지원자들 중 가장 높은 면접 성적 순위
        for s in grade:
            # 이전 지원자들의 면접 성적 순위보다 더 높은 경우, 선발됨
            if pre > s:
                pre = s # 최고 면접 성적 순위 갱신
                cnt += 1 # 선발 인원 수 증가
        ans.append(cnt)
    
    # 각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력
    for cnt in ans: print(cnt)

sol()