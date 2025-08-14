# 대표 다익스트라
'''
deque(double-ended queue)
목적 : 양쪽 끝에서 빠르게 넣고 빼는 fifo큐 구현
주용도 : 
- BFS(너비 우선 탐색), 순서대로 처리하는 작업 대기열, 슬라이딩 윈도우, 회전

heapq(우선순위 큐, 최소 힙)
목적 : 가장 작은값(또는 큰값)을 빠르게 꺼내는 구조
구조 : 완전 이진트리 기반의 힙 구조
시간 복잡도 : 삽입/ 삭제O (log N)
주 용도:
- 다익스트라, 프림 알고리즘(최단 경로, MST), 작업스케줄링(가장 우선순위 높은/낮은
항목 먼저 처리), K번째 최소값/최대값 구하기'''
import sys
import heapq
input = sys.stdin.readline
INF = 10**18

# 입력
V, E = map(int, input().split())
S = int(input())

graph = [[] for _ in range(V + 1)]  # 1-indexed
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # 방향 그래프. 무방향이면 graph[v].append((u, w))도 추가

# 다익스트라
dist = [INF] * (V + 1)
dist[S] = 0
pq = [(0, S)]  # (현재까지의 최단거리, 노드)

while pq:
    d, u = heapq.heappop(pq)
    # 이미 더 좋은 경로로 처리된 적 있으면 스킵
    if d > dist[u]:
        continue
    # 인접 간선 완화(Relaxation)
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

# 출력 (도달 불가면 INF)
for i in range(1, V + 1):
    print(dist[i] if dist[i] != INF else "INF")


''' 1 (실버1~골드5): 단일 시작 최단경로 (Dijkstra)

문제
정점 수 V, 간선 수 E, 시작 정점 S가 주어진다.
모든 간선의 가중치는 양의 정수. S에서 각 정점까지의 최단거리를 구하라.
도달 불가면 INF.'''
import heapq
INF = 10**5
v,e = map(int, input().split())
s = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

dist = [INF] * (v+1)
dist[s] = 0
pq = [(0,s)]

while pq:
    d,u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v,w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] =nd
            heapq.heappush(pq,(nd,v))
for i in range(1, v+1):
    print(dist[i] if dist[i] != INF else "INF")
    

import heapq
INF = 10 ** 18
v,e = map(int, input().split())
s= int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
dist = [INF]*(v+1)
dist[s] = 0
pq = [(0,s)]
q = int(input())
while pq:
    d,u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v2,w in graph[u]:
        nd = d+ w
        if nd < dist[v2]:
            dist[v2] = nd
            heapq.heappush(pq,(nd,v2))

for _ in range(q):
    t = int(input())
    print(dist[t] if dist[t] != INF else "INF")     


'''BFS 응용 (골드5~4)

문제:
	•	N×M 격자, 0은 빈칸, 1은 벽, S는 시작점, E는 도착점.
	•	이동은 상하좌우 한 칸씩.
	•	단, 최대 1번만 벽을 부술 수 있음.
	•	시작점에서 도착점까지의 최소 이동 횟수를 구하라.
	•	도달 불가면 -1.'''
from collections import deque
n,m = map(int,input().split())
q = deque()

dir = [(-1,0),(1,0),(0,-1),(0,1)]
graph = [input().strip() for _ in range(n)]
dist = [[[-1]*2 for _ in range(m)] for __ in range(n)]
sx = sy = ex = ey = -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            sx, sy = i, j
        elif grid[i][j] == 'E':
            ex, ey = i, j
q.append((sx,sy,0))
while q:
    x,y, hit = q.popleft()
    if (x,y) == (ex,ey):
        print(dist[x][y][hit])
        break
    for dx,dy in dir:
        nx, ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] != '1':
            if dist[nx][ny][hit] == '-1':
                dist[nx][ny][hit] = dist[x][y][hit]+1
                q.append((nx,ny,hit))
                
        elif 0<=nx<n and 0<=ny<m and graph[nx][ny] == '1' and hit == 0:
            if dist[nx][ny][hit] == '-1':
                dist[nx][ny][1] = dist[x][y][0]+1
                q.append((nx,ny,hit))
    

'''3번 — 다익스트라 변형 (골드4)

문제:
	•	도시 개수 N, 도로 개수 M.
	•	각 도로는 양방향, 가중치 있음.
	•	도로마다 통행 제한 시간 L이 있어서, 출발 시간이 L보다 빠르면 통과 불가.
	•	1번 도시에서 N번 도시까지의 최소 도착 시간을 구하라.
	•	도달 불가면 -1.

포인트:
	•	다익스트라에서 if current_time < L이면 그 도로는 못 탐색
	•	우선순위 큐에 (time, node)로 저장, time은 현재까지 걸린 총 시간'''
import heapq
INF = 10 **18
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w,l = map(int,input().split())
    graph[u].append(v,w,l)
    graph[v].append((u,w,l))
dist = [INF] * (n+1)
dist[1] =  0
pq = [(0,1)]
while pq:
    t,u = heapq.heappop(pq)
    if t<= dist[u]:
        continue
    for v,w,l in graph[u]:
        depart = max(t,l)
        nt = depart + w
        if nt < dist[v]:
            dist[v] = nt
            heapq.heappush(pq,(nt,v))
print(dist[n] if dist[n] != INF else -1)
