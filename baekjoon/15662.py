# 톱니바퀴 (2)
# 구현, 시뮬레이션

from collections import deque

T = int(input()) # 톱니바퀴의 개수
wheels = [deque(input()) for _ in range(T)] # 톱니바퀴의 상태

# 입력된 회전 횟수만큼 회전
for _ in range(int(input())):
    num,d = map(int,input().split()) # 회전시킨 톱니바퀴의 번호, 방향
    num -= 1 # 실제 인덱스는 번호보다 1 작기 때문에 감소시킴

    # 현재 톱니바퀴의 왼쪽/오른쪽 톱니바퀴와 맞닿는 면의 극 저장
    left,right = wheels[num][-2],wheels[num][2]
    wheels[num].rotate(d) # 현재 톱니바퀴 회전

    # 왼쪽에 있는 톱니바퀴들 회전
    for l in range(num-1,-1,-1):
        # 회전시킬 톱니바퀴의 왼쪽 톱니바퀴의 오른쪽 면(회전시킬 톱니바퀴와 맞닿는 면)과 비교
        if wheels[l][2] != left:
            left = wheels[l][-2] # 왼쪽 톱니바퀴의 왼쪽 면으로 변경
            
            # 원래 회전시킬 톱니바퀴와 인덱스를 비교하여 회전 방향 결정
            wheels[l].rotate(d if l&1==num&1 else -d)
        
        # 같은 극이면, 나머지 톱니바퀴들도 회전하지 않으므로 종료
        else: break
    
    # 마찬가지로, 오른쪽에 있는 톱니바퀴들 회전
    for r in range(num+1,T):
        if wheels[r][-2] != right:
            right = wheels[r][2]
            wheels[r].rotate(d if r&1==num&1 else -d)
        else: break

# 12시 방향이 S극(1)인 톱니바퀴의 개수 출력
ans = 0
for i in range(T):
    if wheels[i][0]=='1': ans += 1
print(ans)