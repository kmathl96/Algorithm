# 디지털 티비
# 구현, 구성적

N = int(input()) # 채널의 수
ch = [input() for _ in range(N)] # 채널의 이름
kbs1_idx,kbs2_idx = ch.index('KBS1'),ch.index('KBS2') # KBS1, KBS2의 채널 번호

# KBS1을 먼저 첫 번째로 이동한 후, KBS2를 두 번째로 이동하는 방법
# KBS1이 KBS2보다 뒤에 있다면, KBS1을 이동시키면 KBS2의 순서가 뒤로 밀림
if kbs1_idx > kbs2_idx:
    kbs2_idx += 1 # KBS2의 채널 번호 1 증가시킴

# KBS1이 있는 채널로 이동 (KBS1의 위치만큼 버튼 1 누름)
# -> KBS1을 첫 번째 순서로 이동시킴 (KBS1의 위치만큼 버튼 4 누름)
# -> KBS2가 있는 채널로 이동 (KBS2의 위치만큼 버튼 1 누름)
# -> KBS2를 두 번째 순서로 이동시킴 ((KBS2의 위치+1)만큼 버튼 4 누름(두 번째 위치이므로))
print('1'*(kbs1_idx)+'4'*(kbs1_idx)+'1'*(kbs2_idx)+'4'*(kbs2_idx-1))