# 더하기 사이클
# 수학, 구현

N = int(input()) # 0보다 크거나 같고, 99보다 작거나 같은 정수
cycle = 0 # 사이클의 길이
num = N # 새로운 수
while True:
    # 1. 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만듦
    # 2. 각 자리의 숫자를 더함
    # 3. 주어진 수의 가장 오른쪽 자리 수(num%10)와
    #    앞에서 구한 합의 가장 오른쪽 자리 수((num//10+num%10)%10)를 이어 붙임
    num = num%10*10 + (num//10+num%10)%10
    
    cycle += 1 # 사이클의 길이 증가

    # 원래 수로 돌아오면 종료
    if num==N: break

print(cycle)