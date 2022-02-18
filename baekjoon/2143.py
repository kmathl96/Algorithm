# 두 배열의 합
# 누적 합

# 리스트의 부 배열의 합과 그 개수를 딕셔너리에 넣어서 반환
def sub_sum(arr):
    cnts = dict()
    for i in range(len(arr)):
        sub = 0 # 부 배열의 합
        for j in range(i,len(arr)):
            sub += arr[j]
            # 딕셔너리에 아직 없다면 개수 1로 저장
            if sub not in cnts.keys():
                cnts[sub] = 1
            # 딕셔너리에 있다면 개수 증가
            else: cnts[sub] += 1
    return cnts

T = int(input()) # 두 배열의 부 배열의 합을 더해서 만들고자 하는 수
n = int(input()) # 배열 A의 크기
A = list(map(int,input().split()))
m = int(input()) # 배열 B의 크기
B = list(map(int,input().split()))

# 각 배열의 부 배열의 합의 경우의 수
cntsA,cntsB = sub_sum(A),sub_sum(B)

# A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수 구하기
ans = 0
for k,v in cntsA.items(): # A의 부 배열의 합과 그 개수
    # T와 A의 부배열의 합의 차이 값이 B의 부 배열의 합 중에 있는 경우
    if T-k in cntsB.keys():
        ans += v*cntsB[T-k] # 부 배열의 쌍의 개수(각 개수를 곱한 값)를 더함
print(ans)