# 가로수
# 수학, 정수론, 유클리드 호제법

import sys
input = sys.stdin.readline

def gcd(a,b):
    if a < b: a,b = b,a
    if not b: return a
    if b==1: return 1
    return gcd(b,a%b)

N = int(input())
trees = list(int(input()) for _ in range(N))
distances = [trees[i+1]-trees[i] for i in range(N-1)]
common_distance = distances[0]
for dist in list(set(distances)):
    common_distance = gcd(common_distance,dist)
print(sum(distances)//common_distance-N+1)