# AC
# 구현, 문자열, 파싱, 덱

from collections import deque

def ac(functions,q):
    # 실제로 배열을 뒤집지는 않고, 뒤집혀있는지 여부에 따라 처리
    is_reversed = 0 # 주어진 배열에서 뒤집힌 상태인지 여부를 저장
    for f in functions:
        # i) 뒤집기
        if f=='R':
            is_reversed = 1-is_reversed # 여부를 반대로 저장
        # ii) 버리기
        else:
            # 배열에 수가 있는 경우
            if q:
                # 뒤집혀 있는 경우, 마지막 수를 버림
                if is_reversed: q.pop()
                # 그렇지 않은 경우, 첫 번째 수를 버림
                else: q.popleft()
            # 배열이 비어있는 경우, 에러 발생
            else: return 'error'

    # 뒤집혀 있는 경우, 배열을 뒤집기
    if is_reversed: q.reverse()

    # 제시된 형태로 배열을 변환하여 리턴
    return '['+','.join(map(str,q))+']'

def sol():
    T = int(input()) # 테스트 케이스의 개수
    ans = [] # 각 테스트 케이스의 결과를 저장할 배열
    for _ in range(T):
        p = input().replace('RR', '') # 수행할 함수
        input() # 배열에 들어있는 수의 개수 (사용하지 않으므로 따로 저장하지 않음)
        q = deque(eval(input())) # 주어진 정수 배열을 큐로 저장
        ans.append(ac(p,q)) # 함수를 수행한 결과를 ans에 저장
    
    # 각 테스트 케이스의 결과들 출력
    print('\n'.join(ans))

sol()