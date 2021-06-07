# 행렬 테두리 회전하기
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)

def solution(rows, columns, queries):
    answer = []
    arr = [[r*columns+c+1 for c in range(columns)] for r in range(rows)] # 주어진 행렬
    for x1,y1,x2,y2 in queries: # 쿼리 반복
        mn = min(arr[x1-1][y1-1:y2]+arr[x2-1][y1-1:y2]) # 최솟값 초기화 - 직사각형 맨윗줄과 맨아랫줄에서 가장 작은 값
        val1 = arr[x1-1].pop(y2-1) # 위 테두리의 가장 오른쪽 값 제거 (다음 행에 넣을 것)
        val2 = arr[x2-1].pop(y1-1) # 아래 테두리의 가장 왼쪽 값 제거 (이전 행에 넣을 것)
        for x in range(x2-x1-1): # 직사각형 왼쪽/오른쪽 테두리의 숫자들을 움직임
            val1,arr[x1+x][y2-1] = arr[x1+x][y2-1],val1 # val1을 오른쪽에 넣고, 해당 위치의 값을 val1에 저장 (다음 행에 넣을 것)
            val2,arr[x2-x-2][y1-1] = arr[x2-x-2][y1-1],val2 # val2을 왼쪽에 넣고, 해당 위치의 값을 val2에 저장 (이전 행에 넣을 것)
            mn = min(mn, val1, val2) # 최솟값 갱신
        arr[x2-1].insert(y2-1, val1) # 맨마지막 값을 아래 테두리 오른쪽에 넣기
        arr[x1-1].insert(y1-1, val2) # 맨마지막 값을 위 테두리 왼쪽에 넣기
        answer.append(mn)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]])) # [1]