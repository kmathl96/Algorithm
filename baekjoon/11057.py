# 오르막 수

N = int(input())
num = [1]*10
for i in range(N-1):
    for j in range(1,10):
        num[j] += num[j-1]
print(sum(num)%10007)