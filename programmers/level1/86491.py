# 최소직사각형

def solution(sizes):
    maxw,maxh = 0,0 # 가장 긴 가로 길이와 세로 길이
    for w,h in sizes: # 각 명함의 가로 길이와 세로 길이
        if w < h: w,h = h,w # 세로 길이가 더 길면 명함을 가로로 눕힘
        if maxw < w: maxw = w # 가장 긴 가로 길이 갱신
        if maxh < h: maxh = h # 가장 긴 세로 길이 갱신
    return maxw*maxh # 명함 지갑의 크기

print(solution([[60,50],[30,70],[60,30],[80,40]])) # 4000
print(solution([[10,7],[12,3],[8,15],[14,7],[5,15]])) # 120
print(solution([[14,4],[19,6],[6,16],[18,7],[7,11]])) # 133