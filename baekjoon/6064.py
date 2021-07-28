# 카잉 달력
# 수학, 정수론, 중국인의 나머지 정리

# 최대공약수 구하기
def gcd(a,b):
    if not b: return a
    return gcd(b,a%b)

for _ in range(int(input())):
    M,N,x,y = map(int,input().split()) # <M:N>이 마지막 해
    ans = -1 # <x:y>가 나타내는 해 (유효하지 않다면 -1 출력)

    # 최소공배수 구하기 => 마지막 해
    if M > N: lcm = (M*N)//gcd(M,N)
    else: lcm = (M*N)//gcd(N,M)

    for num in range((x-1)%M+1,lcm+1,M):
        # 유효한 값을 갖는 경우, 답으로 저장하고 종료
        if (num-1)%N+1==y:
            ans = num
            break
    print(ans)