# 암호코드
# 다이나믹 프로그래밍

cipher = input() # 암호
N = len(cipher) # 암호의 길이
dp = [0]*(N+1) # 각 자리까지 해석했을 때의 해석의 가짓수
dp[0] = 1
for i in range(1,N+1):
    # 현재 글자가 0이 아닌(1~9) 경우, A~I로 바꾸기
    if int(cipher[i-1]):
        dp[i] = dp[i-1] # 이전 글자까지의 가짓수 저장
    # 현재 글자가 0이면서 첫 글자이거나 이전 글자가 2보다 큰 경우, 암호가 잘못된 것임
    elif i<2 or int(cipher[i-2])>2:
        break # 더 탐색하지 않고 종료

    # 이전 글자를 포함해서 10~26인 경우, J~Z로 바꾸기
    if i>1 and (cipher[i-2]=='1' or cipher[i-2]=='2' and int(cipher[i-1])<=6):
        dp[i] = (dp[i]+dp[i-2])%1000000 # 전전 글자까지의 가짓수 저장

# N번째 글자까지 했을 때의 해석의 가짓수 출력
print(dp[N])