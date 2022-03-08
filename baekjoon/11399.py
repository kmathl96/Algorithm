# ATM
# 그리디, 정렬

N = int(input()) # 사람의 수

# 각 사람이 돈을 인출하는 데 걸리는 시간
# 인출 시간이 짧은 사람부터 인출 => 필요한 시간의 합을 최소로 만듦
# => 오름차순 정렬
P = sorted(list(map(int,input().split())))

# 본인과 뒷사람들이 본인의 인출 시간만큼 더 걸리므로 곱해서 합함
print(sum(P[i]*(N-i) for i in range(N)))