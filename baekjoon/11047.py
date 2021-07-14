# 동전 0
# 그리디 알고리즘

N,K = map(int,input().split()) # 가지고 있는 동전의 종류, 만들고자 하는 금액
coins = reversed([int(input()) for _ in range(N)]) # 가지고 있는 동전의 가치 (내림차순 정렬)
ans = 0 # 필요한 동전 개수의 최솟값
for coin in coins:
    ans += K//coin # 금액을 동전으로 나눈 몫이 최대 개수
    K %= coin # 금액을 동전으로 나눈 나머지 만큼 남음
    if not K: break # K=0이 되면 종료
print(ans)