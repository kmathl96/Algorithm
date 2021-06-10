# 쿼드압축 후 개수 세기
# 월간 코드 챌린지 시즌1

# 현재 위치(r,c)에서 해당 크기(n)의 영역이 하나의 숫자로만 이루어져있는지 판단
def check(arr,r,c,n,num):
    for i in range(n):
        for j in range(n):
            if arr[r+i][c+j] != num: return False # 다른 숫자인 경우 False 반환
    # 다시 확인하는 일이 없도록 해당 영역을 -1로 채움
    for i in range(n):
        for j in range(n):
            arr[r+i][c+j] = -1
    return True

def solution(arr):
    answer = [0,0] # 0,1의 개수
    size = len(arr) # 정사각형 영역의 한 변의 길이
    while size > 0: # 크기가 1이 될 때까지 반복
        for r in range(0,len(arr),size):
            for c in range(0,len(arr),size):
                num = arr[r][c] # (r,c)의 숫자
                if num != -1 and check(arr,r,c,size,num): # 하나의 숫자로만 채워진 경우 
                    answer[num] += 1 # 해당 숫자의 개수 +1
        size //= 2 # 크기를 반으로 줄임
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4,9]
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])) # [10,15]