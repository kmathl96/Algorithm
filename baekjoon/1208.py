# 부분수열의 합 2
# 이분 탐색

from itertools import combinations

N,S = map(int,input().split()) # 정수의 개수와 정수
seq = list(map(int,input().split())) # 길이 N의 수열

# 수열을 두 집합으로 나누고 => seq[:N//2],seq[N//2:]
# 두 집합의 각 부분집합의 요소의 합을 구하기
# 하나는 오름차순, 다른 하나는 내림차순으로 정렬
sum1 = sorted([sum(comb) for r in range(N//2+1) for comb in combinations(seq[:N//2], r)])
sum2 = sorted([sum(comb) for r in range(N-N//2+1) for comb in combinations(seq[N//2:], r)],reverse=1)
l,r = 0,0 # 각 부분 합 리스트의 포인터
ans = 0 # 부분 수열의 원소를 다 더한 값이 S가 되는 경우의 수

# 포인터가 유효한 위치를 가리키는 경우 계속 반복
while l<len(sum1) and r<len(sum2):
    subsum = sum1[l] + sum2[r] # 포인터가 가리키는 요소의 합

    # S보다 작은 경우
    if subsum < S:
        # 더 큰 수를 확인하기 위해 sum1의 포인터 이동
        l += 1
    
    # S보다 큰 경우
    elif subsum > S:
        # 더 작은 수를 확인하기 위해 sum2의 포인터 이동
        r += 1
    
    # S와 같은 경우
    else:
        # 각 포인터가 가리키는 값과 같은 값을 가진 요소의 개수 찾기
        cnt1,cnt2 = 1,1 # 개수
        
        # sum1에서 찾기
        l += 1
        while l<len(sum1) and sum1[l]==sum1[l-1]: # 같은 값인 경우
            cnt1 += 1 # 개수 증가
            l += 1 # 포인터 이동
        # sum2에서 찾기
        r += 1
        while r<len(sum2) and sum2[r]==sum2[r-1]:
            cnt2 += 1
            r += 1
        
        # 각 개수의 곱만큼 S를 만들 수 있음
        ans += cnt1*cnt2

# S가 0인 경우
if S == 0:
    # 길이 0인 부분 수열의 경우도 포함되어 있으므로 1 감소
    ans -= 1

print(ans)