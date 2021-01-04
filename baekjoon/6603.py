# 로또
# 브루트 포스

from itertools import combinations

while 1:
    arr = list(map(int,input().split()))
    if arr==[0]: break # 0 입력되면 종료
    for case in list(combinations(arr[1:],6)): # 6개 원소를 갖는 조합 리스트
        print(*case)
    print()