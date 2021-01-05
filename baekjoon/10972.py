# 다음 순열
# 브루트 포스
# 백준 10973. 이전 순열과 같은 알고리즘
# 뒤에서부터 탐색하여, 내림차순인 구간을 찾음
# 해당 숫자보다 크면서 뒤의 숫자들 중에선 제일 작은 수를 찾아서 자리를 바꿈
# 뒤의 숫자들을 오름차순으로 정렬

N = int(input())
num = list(map(int,input().split()))
tmp = num.index(N)
for i in range(N-2,-1,-1):
    if num[i] > num[i+1]: continue
    for j in range(i+1,N):
        if num[i] < num[j] < num[tmp]: tmp = j
    num[tmp],num[i] = num[i],num[tmp]
    break
print(" ".join(map(str,num[:i+1]+sorted(num[i+1:]))) if tmp else -1)