# 리모컨
# 브루트포스

N = int(input()) # 이동하려고 하는 채널
# 고장난 버튼이 있는 경우 고장난 버튼을 입력 받고, 없는 경우 빈 set로 초기화
if int(input()): broken = set(input().split())
else: broken = set()
ans = abs(N-100) # 최소 횟수 : 100번 채널에서 +/-로 이동하는 방법의 횟수

# 0~1000000번 채널 순회 (N보다 큰 채널에서 -로 이동하는 경우 고려)
for i in range(1000000):
    cnt = len(str(i))+abs(N-i) # 해당 채널을 누르고 +/-로 N번 채널까지 이동하는 데 버튼 누르는 횟수
    # ans보다 작고, 해당 채널의 숫자들이 고장난 버튼이 아닌 경우 ans 갱신
    if cnt < ans and not set(str(i))&broken: ans = cnt
print(ans)