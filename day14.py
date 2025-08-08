'''1번 문제 (기초 개념)

문제: 루트부터 리프까지의 경로 길이 합 구하기

루트 노드가 1번인 트리가 주어집니다. 각 간선은 양방향입니다. 모든 리프 노드까지의 경로 길이(간선 수)를 더한 값을 구하세요.
'''
n = int(input()) # 정점 개수
tree = [[] for _ in range(n+1)] # 정점 개수보다 1추가 왜냐하면 인덱스0은 사용하지 않기에

for _ in range(n-1): # 선은 점보다 하나 작음 고로 n-1
    a,b = map(int, input().split()) # 선이 양방향으로 연결되는 두개의 점 입력
    tree[a].append(b) # 양방향이므로 append 두번
    tree[b].append(a)

total_de = 0 # 프린트할 깊이값 초기화
vis = [False] * (n+1)  # 지났다고 표시할 visit 초기화

def dfs(node, dep): #dfs함수 생성
    global total_de
    vis[node] = True # 노드를 지나면
    is_leaf = True # 리프도 트루

    for neig in tree[node]: # 트리의 노드를 순찰
        if not vis[neig]: # 1,3 처럼 자식이 없으면
            is_leaf = False # 뻘스
            dfs(neig, dep+1) # dep+1씩
    if is_leaf:
        total_de += dep
dfs(1,0)
print(total_de)


'''2번 문제 (유형 연습: 트리에서 가장 먼 노드 찾기)

문제: 트리 지름 구하기 (가장 긴 경로)

루트 노드가 아니라 어떤 두 정점 사이의 가장 긴 경로의 길이를 구하세요.

입력 형식은 위와 동일합니다.
'''

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

mostm = 0
max_d = 0
def dfs(node,depth,visited):
    global mostm,max_d
    visited[node] = True
    if depth > max_d:
        max_d = depth
        mostm = node
    for nei in tree[node]:
        if not visited[nei]:
            dfs(nei, depth +1, visited)
visited = [False] * (n+1)
dfs(1,0, visited)

visited = [False] * (n+1)
max_d = 0
dfs(mostm,0, visited)
print(max_d)
'''추천 3번 문제: “모든 노드에서 가장 먼 노드까지의 거리 구하기”

🔍 문제 설명

트리가 주어질 때, 각 노드마다 가장 먼 노드까지의 거리를 모두 구하세요'''
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
print(tree)
def dfs(node, depth, visited, dist):
    visited[node] = True
    dist[node] = depth
    for x in tree[node]:
        if not visited[x]:
            dfs(x, depth+1, visited, dist)

visited = [False] * (n+1)
print(visited)
dist = [0] * (n+1)
dfs(1,0,visited,dist)
print(dist)
A = dist.index(max(dist))

visited = [False] * (n+1)
dist_A = [0] * (n+1)
dfs(A, 0, visited,dist_A)
B = dist_A.index(max(dist_A))

visited = [False] * (n+1)
dist_B = [0] * (n+1)
dfs(B, 0, visited,dist_B)

for i in range(1, n+1):
    print(max(dist_A[i], dist_B[i]), end=' ')


'''문제 4. 가장 가까운 1 찾기 (BFS 기초)

📌 문제 설명

0과 1로 이루어진 2차원 행렬이 주어집니다.
당신은 각 0에 대해, 가장 가까운 1까지의 맨해튼 거리(상하좌우)를 구해야 합니다.

모든 0에 대해, 가장 가까운 1까지의 거리를 출력하는 행렬을 만들어주세요.
단, 1인 칸은 거리 0으로 처리합니다.'''
from collections import deque
n,m = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
q= deque()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append((i,j))
            dist[i][j] = 0
while q:
    x,y = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx <n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
for r in dist:
    print(r)

'''문제 5. 미로 탈출 (BFS 기초 응용)

📌 문제 설명

0은 벽이고 1은 이동할 수 있는 길입니다.
(0, 0)에서 출발해 (n-1, m-1)까지 최단 거리로 이동할 수 있는 칸 수를 출력하세요.
맨해튼 거리가 아닌, 실제로 이동한 칸 수를 구해야 합니다.

단, 상하좌우로만 움직일 수 있고, 같은 칸을 두 번 방문할 수 없습니다.'''

from collections import deque
n, m = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]
q= deque()
q.append((0,0))
directions = [(-1,0),(1,0), (0,-1),(0,1)]
while q:
    x,y = q.popleft()
    for dx,dy in directions:
        nx,ny = x + dx, y+ dy
        if nx <0 or nx >= n or ny <0 or ny >= m:
            continue
        if matrix[nx][ny] !=1:
            continue
        matrix[nx][ny] = matrix[x][y] +1
        q.append((nx,ny))
print(matrix[n-1][m-1])