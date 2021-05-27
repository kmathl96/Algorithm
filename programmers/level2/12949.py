# 행렬의 곱셈

def solution(arr1, arr2):
    answer = []
    for r in range(len(arr1)):
        row = []
        for i in range(len(arr2[0])):
            row.append(sum([arr1[r][c]*arr2[c][i] for c in range(len(arr2))]))
        answer.append(row)
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])) # [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])) # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]