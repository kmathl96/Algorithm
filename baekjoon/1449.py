# 수리공 항승
# 그리디, 정렬

def sol():
    N,L = map(int,input().split()) # 물이 새는 곳의 개수, 테이프의 길이
    pipe = sorted(map(int,input().split())) # 물이 새는 곳의 위치
    cnt = 0 # 항승이가 필요한 테이프의 개수를 출력
    idx = 0 # 이전에 붙인 테이프의 오른쪽 끝의 위치

    # 물이 새는 곳을 순서대로 확인
    for i in pipe:
        # 테이프가 붙어있지 않은 경우
        if idx < i:
            cnt += 1 # 테이프를 붙임
            idx = i+L-1 # 테이프의 오른쪽 끝의 위치 갱신
    print(cnt)

sol()