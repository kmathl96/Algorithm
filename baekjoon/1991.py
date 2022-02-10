# 트리 순회
# 트리, 재귀

# 전위 순회 : 루트 -> 왼쪽 자식 -> 오른쪽 자식
def preorder(idx):
    # .이면 노드가 없는 것이므로 종료
    if idx=='.': return

    node = tree[idx] # 인덱스에 해당하는 노드
    print(node[0],end='') # 루트 노드의 값를 먼저 출력
    preorder(node[1])
    preorder(node[2])

# 중위 순회 : 왼쪽 자식 -> 루트 -> 오른쪽 자식
def inorder(idx):
    if idx=='.': return
    node = tree[idx]
    inorder(node[1])
    print(node[0],end='') # 왼쪽 자식 노드 먼저 방문한 뒤 루트 노드의 값 출력
    inorder(node[2])

# 후위 순회 : 왼쪽 자식 -> 오른쪽 자식 -> 루트
def postorder(idx):
    if idx=='.': return
    node = tree[idx]
    postorder(node[1])
    postorder(node[2])
    print(node[0],end='') # 자식 노드들 먼저 방문한 후 루트 노드의 값 출력

N = int(input()) # 이진 트리의 노드의 개수
tree = [[chr(i+65),'.','.'] for i in range(N)] # 노드의 값과 왼쪽 자식과 오른쪽 자식의 인덱스
for _ in range(N):
    info = list(input().split()) # 노드와 왼쪽 자식 노드, 오른쪽 자식 노드
    node = ord(info[0])-65 # 노드의 인덱스

    # 왼쪽 자식 노드가 있는 경우
    if info[1] != '.':
        tree[node][1] = ord(info[1])-65 # 왼쪽 자식 노드의 인덱스 저장
    # 오른쪽 자식 노드가 있는 경우
    if info[2] != '.':
        tree[node][2] = ord(info[2])-65 # 오른쪽 자식 노드의 인덱스 저장

# 루트부터 시작
preorder(0) # 전위 순회
print()
inorder(0) # 중위 순회
print()
postorder(0) # 후위 순회