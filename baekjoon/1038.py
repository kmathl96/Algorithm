# 감소하는 수
# 브루트포스, 백트래킹

N = int(input()) # N번째 감소하는 수 구하기
numbers = list(range(10)) # 감소하는 수들의 집합
ref_idx,ref_num = 0,0 # 참조할 수(앞자리가 될 수)의 인덱스와 값

# N개 넘을 때까지 구하기
# 감소하는 수의 최댓값은 9876543210이므로, 이 값을 넘어서면 N번째 감소하는 수는 없음
while len(numbers)<=N and ref_num<=987654321:
    ref_idx += 1
    ref_num = numbers[ref_idx]

    # 0~(참조할 수의 일의자리 값-1)을 참조할 수에 붙임
    for num in range(ref_num%10):
        numbers.append(ref_num*10+num)

# N번째 감소하는 수 출력, 없다면 -1 출력
print(numbers[N] if len(numbers)>N else -1)