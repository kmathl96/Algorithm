# 부분수열의 합
# 브루트포스

from itertools import combinations

N = int(input()) # 수열 S의 크기
S = list(map(int,input().split())) # 수열

# 부분 수열은 조합으로 나타낼 수 있음
# 모든 조합의 요소의 합을 저장하고 중복은 제거
sums = set([sum(comb) for n in range(1,N+1) for comb in combinations(S,n)])
ans = 2**N # 부분 수열의 합으로 나올 수 없는 가장 작은 자연수 : 최댓값으로 초기화

# 1부터 순서대로 탐색
for num in range(1,2**N):
    # 합이 될 수 없는 경우 ans를 바꾸고 종료
    if num not in sums:
        ans = num
        break
print(ans)