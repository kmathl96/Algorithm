# 괄호 추가하기
# 브루트포스

# 연산자에 따라 두 정수를 계산하여 반환
def cal(a,b,op):
    if op=='+': return a+b
    elif op=='-': return a-b
    else: return a*b

N = int(input())
ops = list(input())
mn = -(2**31) # 결과의 최솟값
ans = mn # 최솟값으로 초기화
for i in range(1<<(N-1)//2): # 연산의 횟수에 따라 조합 구함
    cur = int(ops[0]) # 현재 값을 첫 숫자로 초기화
    j = 0 # 연산자의 위치를 계산하기 위한 변수

    # i가 2로 나눠지면 괄호 추가하지 않고, 나눠지지 않으면 괄호를 추가
    while 2*j+1 < N: # 해당 연산자의 위치(2*j+1)가 입력 연산의 길이(N)보다 커지면 종료
        # 현재 연산과 다음 연산 연속으로 괄호를 추가하는 경우는 존재하지 않으므로 break
        if i&1 and (i//2)&1:
            cur = mn # ans 값이 변경되지 않도록 최솟값으로 변경
            break
        # 현재 연산에서는 괄호 없이, 다음 연산은 괄호 추가하는 경우
        if not (i&1) and 2*j+4 < N and (i//2)&1:
            # 다음 연산을 먼저 한 후, 그 결과값으로 현재 연산을 수행
            cur = cal(cur,cal(int(ops[2*j+2]),int(ops[2*j+4]),ops[2*j+3]),ops[2*j+1])
            # 다음 연산까지 같이 수행하므로, i를 2로 나누고 연산 위치를 다음으로 옮겨 줌
            i = i//2
            j += 1
        # 현재 괄호를 추가하는 경우 연산 수행
        else: cur = cal(cur,int(ops[2*j+2]),ops[2*j+1])
        i = i//2 # 다음 연산에서 괄호를 추가할지 판단하기 위해 2로 나눔
        j += 1 # 다음 연산을 하기 위해 연산자의 위치 + 1
    ans = max(ans,cur) # 여태까지의 최댓값과 현재 값을 비교하여 큰 값 저장
print(ans)