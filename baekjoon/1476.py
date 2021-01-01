# 날짜 계산
# 기초 - 브루트 포스

E,S,M = map(int,input().split())
ans = 1
while (E,S,M)!=(1,1,1):
    E,S,M = E-1,S-1,M-1
    # 각 변수가 0이 되면 범위의 최대값으로 초기화
    if E==0: E = 15
    if S==0: S = 28
    if M==0: M = 19
    ans += 1
print(ans)