# 선분과 점
# 이분 탐색, 기하학, 3차원 기하학, 삼분 탐색

# 점 (x,y,z)과 점 C(Cx,Cy,Cz) 사이의 거리
def dist(x,y,z):
    return ((x-Cx)**2+(y-Cy)**2+(z-Cz)**2)**0.5

Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz = map(int,input().split()) # 세 점 A, B, C의 좌표
ans = dist(Bx,By,Bz) # 선분 AB와 점 C와의 거리의 최솟값 : 두 점 B, C 사이의 거리로 초기화
while True:
    Mx,My,Mz = (Ax+Bx)/2,(Ay+By)/2,(Az+Bz)/2 # 선분 AB의 중간 지점인 M의 좌표
    d = dist(Mx,My,Mz) # 두 점 M, C 사이의 거리
    if abs(ans-d) < 0.0000001: break # ans와 d의 차가 허용되는 정도(10^(-6))보다 작다면 종료
    if ans > d: ans = d # d가 더 작다면 ans 갱신

    # 두 점 A, B 중 점 C와 더 먼 점을 점 M의 좌표로 변경
    if dist(Ax,Ay,Az) >= dist(Bx,By,Bz): Ax,Ay,Az = Mx,My,Mz
    else: Bx,By,Bz = Mx,My,Mz
print(ans)