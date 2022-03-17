# 로봇 프로젝트
# 정렬, 투 포인터

import sys
input = sys.stdin.readline

def sol():
    x = int(input())*10000000 # 구멍의 너비 => 센티미터를 나노미터로 바꿈
    n = int(input()) # 레고 조각의 수

    # 두 조각의 길이 차가 가장 큰 것을 출력해야 함
    # 가장 작은 것과 가장 큰 값이랑 비교해서 하나씩 증감시켜가며 답 찾기
    lego = sorted([int(input()) for _ in range(n)]) # 레고 조각의 길이를 오름차순 정렬
    l1,l2 = 0,n-1 # 양 끝 지점의 인덱스 값
    ans = 'danger' # 출력할 문자열 : 구멍을 막을 수 없을 시 출력할 danger로 초기화
    while l1<l2:
        leng = lego[l1]+lego[l2] # 두 조각의 길이의 합

        # 구멍의 너비와 일치하는 경우, 답을 저장하고 종료
        if leng==x:
            ans = f'yes {lego[l1]} {lego[l2]}'
            break
        
        # 포인터의 위치 이동
        # 길이가 긴 경우, 큰 값을 감소시키기
        if leng > x:
            l2 -= 1
        # 길이가 짧은 경우, 작은 값을 증가시키기
        else:
            l1 += 1
    
    print(ans)

# 테스트 케이스의 개수가 정해져있지 않음
# 입력이 종료될 때까지 반복
while True:
    # 입력이 있으면 수행
    try:
        sol()
    # 입력이 없으면 종료
    except:
        break