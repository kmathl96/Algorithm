# 최소 스패닝 트리
# 그래프, 최소 스패닝 트리

def find_set(x):
    if p[x]!=x: p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    px,py = find_set(x),find_set(y)
    if rank[px]>rank[py]: p[py] = px
    else:
        p[px] = py
        if rank[px]==rank[py]: rank[py] += 1

V,E = map(int,input().split())
edges = sorted([list(map(int,input().split())) for _ in range(E)], key=lambda x: x[2])
p = list(range(V+1))
rank = [0]*(V+1)
ans = 0
cnt = 0
for e in edges:
    if find_set(e[0])==find_set(e[1]): continue
    union(e[0],e[1])
    ans += e[2]
    cnt += 1
    if cnt==V-1: break
print(ans)