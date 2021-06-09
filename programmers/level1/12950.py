# 행렬의 덧셈

def solution(arr1, arr2):
    return [[arr1[i][j]+arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

print(solution([[1,2],[2,3]], [[3,4],[5,6]])) # [[4,6],[7,9]]
print(solution([[1],[2]], [[3],[4]])) # [[4],[6]]