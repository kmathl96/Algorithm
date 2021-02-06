# 드래곤 커브
# 구현, 시뮬레이션

def rot(curve,end):
    global arr
    n = len(curve)
    for i in range(n-2,-1,-1):
        # 특정 점(x0,y0)을 기준으로 점(x1,y1)를 회전 변환 시킴
        # 좌표 평면으로 생각했을 때,
        # 점(x1,y1)를 각각 x0,y0 만큼 이동시켜서 회전 변환한 뒤 다시 x0,y0 만큼 이동
        # x2 = cos(90º)*(x1-x0) - sin(90º)*(y1-y0) + x0
        #    = 0*(x1-x0) - 1*(y1-y0) + x0
        #    = y0 - y1 + x0
        # y2 = sin(90º)*(x1-x0) + cos(90º)*(y1-y0) + y0
        #    = 1*(x1-x0) - 0*(y1-y0) + y0
        #    = x1 - x0 + y0
        x2,y2 = end[1]-curve[i][1]+end[0],curve[i][0]-end[0]+end[1]
        # 문제에서 주어진 좌표평면 내에 있고, 아직 드래곤 커브를 이루는 점이 아닌 경우
        if 0<=x2<101 and 0<=y2<101 and (x2,y2) not in curve:
            arr[x2][y2] = 1
            curve.append((x2,y2))

N = int(input())
arr = [[0 for i in range(101)] for j in range(101)] # 드래곤 커브를 이루는 점
dxdy = [(1,0),(0,-1),(-1,0),(0,1)] # 방향
for _ in range(N):
    x,y,d,g = map(int,input().split())
    nx,ny = x+dxdy[d][0],y+dxdy[d][1] # 0세대의 끝점
    curve = [(x,y),(nx,ny)] # 0세대의 드래곤 커브
    arr[x][y],arr[nx][ny] = 1,1
    while g: # g만큼 반복
        rot(curve,(curve[-1][0],curve[-1][1]))
        g -= 1

# 1*1 정사각형을 이루는 드래곤 커브의 개수 세기
ans = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] and arr[r][c+1] and arr[r+1][c] and arr[r+1][c+1]: ans += 1
print(ans)