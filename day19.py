'''1번. 미로 탐색 (실버 1 난이도, BFS 기본기)
	•	N×M 크기의 미로가 주어진다.
	•	0은 벽, 1은 길.
	•	(1,1)에서 출발해 (N,M)까지 이동할 때, 최소 칸 수를 구하라.
	•	상하좌우 이동 가능.
	•	BFS로 풀어야 한다.'''
from collections import deque
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dist = [[-1]*n for _ in range(m)]
q = deque()
q.append((0,0))
dist[0][0] = 1
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
while q:
    x,y = q.popleft()
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]== 1 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))
print(dist[n-1][m-1])

'''2번. 연결 요소의 개수 (실버 2 난이도, DFS/BFS 둘 다 가능)
	•	N개의 정점과 M개의 간선이 있는 무방향 그래프가 주어진다.
	•	연결 요소의 개수를 출력하라.
	•	즉, 떨어져 있는 그래프 덩어리의 개수를 구하는 문제.
	•	DFS(재귀) 또는 BFS(큐) 아무 방식으로 풀어도 됨.'''

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
vis = [False] * (n+1)
def dfs(u):
    vis[u] = True
    for v in graph[u]:
        if not vis[v]:
            dfs(v)
com= 0
for node in range(1, n+1):
    if not vis[node]:
        com+=1
        dfs(node)


print(com)

'''3번. 바이러스 (실버 3 난이도, DFS 연습)
	•	N개의 컴퓨터 (1~N), M개의 연결 관계가 주어진다.
	•	1번 컴퓨터가 웜 바이러스에 걸림.
	•	네트워크를 통해 전염될 때, 감염되는 컴퓨터의 수를 구하라.
	•	(1번 제외한 감염된 컴퓨터 수를 출력).
	•	DFS로 풀면 딱 좋음.'''
n =int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
vis = [False] * (n+1)
def dfs(u):
    vis[u] = True
    for v in graph[u]:
        if not vis[v]:
            dfs(v)
dfs(1)
print(sum(vis)-1)


'''정점 수 N, 간선 수 M, 시작 정점 S가 주어진다.
모든 간선은 방향이 있으며, 가중치는 양의 정수다.
시작점 S에서 각 정점까지의 최단거리를 구하라. 도달 불가능한 정점은 INF를 출력한다.

입력
	•	첫 줄: N M S  (1 \le N \le 100000,\ 0 \le M \le 300000,\ 1 \le S \le N)
	•	다음 M줄: u v w  (정점 u \rightarrow v, 가중치 w, 1 \le w \le 10^9)

출력
	•	1번 정점부터 N번 정점까지, 각 줄에 S에서의 최단거리를 출력
	•	도달할 수 없으면 INF'''
import heapq
INF = 10**18
n,m,s = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

dis = [INF]*(n+1)
dis[s] = 0
pq = [(0,s)]
while pq:
    weight,n = heapq.heappop(pq)
    if dis[n] < weight:
        continue
    for v,w in graph[n]:
        nco = w+weight
        if nco < dis[v]:
            dis[v] = nco
            heapq.heappush(pq,(nco,v))
for i in range(1,n+1):
    print(dis[i] if dis[i]!=INF else 'INF')
