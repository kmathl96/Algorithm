# 가로수
# 수학, 정수론, 유클리드 호제법

import sys
input = sys.stdin.readline

# 최대공약수 구하기 (유클리드 호제법)
def gcd(a,b):
    # 큰 숫자를 a로, 작은 숫자를 b로 둠
    if a < b: a,b = b,a
    
    # 한 숫자가 0인 경우,
    # 나눠떨어지는 경우이므로 다른 숫자가 최대공약수가 됨
    if not b: return a
    
    if b==1: return 1 # 어떤 수와 1의 최대공약수는 1

    # 작은 수(b)와 큰 수를 작은 수로 나눈 나머지(a%b)의 최대공약수와 같음
    return gcd(b,a%b)

N = int(input()) # 이미 심어져 있는 가로수의 수
trees = list(int(input()) for _ in range(N)) # 가로수의 위치
distances = [trees[i+1]-trees[i] for i in range(N-1)] # 다음 가로수와의 거리

# 가로수를 심을 간격 = 거리들의 공약수
# 간격을 최대화하면 심을 가로수의 개수는 최소화됨 => 최대공약수 구하기
common_distance = distances[0] # 1~2번째 나무의 거리로 초기화
for dist in list(set(distances)):
    common_distance = gcd(common_distance,dist) # 거리들의 최대공약수

# 새로 심을 가로수의 개수
# = (거리를 간격으로 나눈 몫-1)의 합
# = 거리의 합을 간격으로 나눈 몫 - (거리의 개수(=N-1))
print(sum(distances)//common_distance-N+1)