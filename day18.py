'''18일차 문제: 불길 탈출 (골드5 난이도)

문제 설명
	•	N×M 격자가 주어짐.
	•	빈 칸(.), 벽(#), 불(F), 사람(J)이 있음.
	•	불은 매 분마다 인접한 4방향(상하좌우)으로 번짐.
	•	사람은 매 분마다 인접한 4방향(상하좌우)으로 이동할 수 있음.
	•	단, 불이 번진 칸이나 벽은 갈 수 없음.
	•	사람이 격자 밖으로 나가면 탈출 성공.
	•	최소 탈출 시간을 구하고, 탈출이 불가능하면 IMPOSSIBLE 출력.'''
from collections import deque
n,m = map(int, input().split())
miro = [list( input().strip()) for _ in range(n)]
dist = [[-1] *(m) for _ in range(n)]
fire = [[-1]*m for _ in range(n)]

qf = deque()
qj = deque()
jx=jy=-1
dir = [(-1,0),(1,0),(0,1),(0,-1)]
for i in range(n):
    for j in range(m):
        if miro[i][j] == 'F':
            qf.append((i,j))
            fire[i][j] = 0
        elif miro[i][j] == 'J':
            jx,jy = i,j
while qf:
    x,y = qf.popleft()
    for dx,dy in dir:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if miro[nx][ny] != '#' and fire[nx][ny] == -1:
                fire[nx][ny]  = fire[x][y] +1
                qf.append((nx,ny))
dist[jx][jy]=0
qj.append((jx,jy))
if jx == 0 or jy == 0 or jx == n-1 or jy == m-1:
    print(1)
    exit()
else:
    esca = False
    while qj:
        x,y = qj.popleft()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            ntime = dist[x][y]+1
            if not (0<= nx < n and 0 <= ny < m ):
                print(ntime)
                esca = True
                exit()
            if miro[nx][ny] == '#' or dist[nx][ny] != -1:
                continue
            if fire[nx][ny] != -1 and ntime >= fire[nx][ny]:
                continue
            dist[nx][ny] = ntime
            qj.append((nx,ny))
    if not esca:
        print('IMPOSSIBLE')


'''18일차 2번 문제 (다익스트라 쉬운 버전)

문제: 최소 비용 이동 (실버 1 난이도)
	•	N×M 격자가 주어짐.
	•	각 칸에는 0 이상 9 이하의 숫자가 있음 → 해당 칸으로 이동할 때 드는 비용.
	•	사람은 (0,0)에서 시작해 (N-1,M-1)까지 도착해야 함.
	•	상하좌우로만 이동 가능.
	•	최소 이동 비용을 구하라.
	•	시작 칸의 비용도 포함해야 함..'''
import heapq
n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
INF = 10 ** 18
dist = [[INF]*m for _ in range(n)]
dist[0][0] = grid[0][0]
pq = [(grid[0][0],0,0)]
dirs = [(-1,0),(1,0),(0,1),(0,-1)]
while pq:
    cost, x, y = heapq.heappop(pq)
    if dist[x][y] < cost:
        continue
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <=nx < n and 0<=ny<m:
            ncost = cost+grid[nx][ny]
            if ncost < dist[nx][ny]:
                dist[nx][ny] = ncost
                heapq.heappush(pq,(ncost,nx,ny))
print(dist[n-1][m-1])

'''18일차 3번 문제 (다익스트라 연습용)

문제: 최소 비용 환승 (실버 1 난이도)
	•	N개의 도시와 M개의 버스 노선이 있다.
	•	각 노선은 (출발, 도착, 비용)으로 주어지며, 양방향이 아닐 수도 있음 (즉, 단방향).
	•	사람은 1번 도시에서 출발하여 N번 도시로 가려 한다.
	•	최소 비용을 구하라.
	•	만약 도착할 수 없다면 -1을 출력하라.
'''
import heapq
n,m = map(int, input().split())
grid = [[]  for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    grid[u].append((v,w))
INF = 10 ** 18
dist = [INF]*(n+1)
dist[1] = 0
pq = [(0,1)]
while pq:
    cost,u = heapq.heappop(pq)
    if dist[u] < cost:
        continue
    for v, w in grid[u]:
        nv = cost+ w
        if dist[v] > nv:
            dist[v] = nv
            heapq.heappush(pq,(nv,v))
print(dist[n] if dist[n] != INF else -1)


'''18일차 4번 문제 (다익스트라 응용)

문제: 최소 비용 도로 건설 (실버 1 ~ 골드 5 난이도)
	•	N개의 도시와 M개의 도로가 있다.
	•	각 도로는 (출발, 도착, 비용)으로 주어지며 양방향이다.
	•	도로 비용은 통행료라고 생각하면 된다.
	•	사람은 1번 도시에서 출발해 모든 도시로 가는 최소 비용을 구하려 한다.
	•	즉, 1번 도시에서 다른 모든 도시까지의 최단 비용을 각각 출력하라.
	•	만약 도달할 수 없는 도시가 있으면 INF를 출력하라.'''
import heapq
INF = 10 ** 18
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
dist = [INF]*(n+1)
dist[1] =0
pq = [(0,1)]
while pq:
    cost, u = heapq.heappop(pq)
    if cost > dist[u]:
        continue
    for v,w in graph[u]:
        nco = w+cost
        if nco < dist[v]:
            dist[v] = nco
            heapq.heappush(pq,(nco,v))
for i in range(1, n + 1):
    print(dist[i] if dist[i] != INF else "INF")


'''18일차 5번 문제 (다익스트라 응용)

문제: 특정 도시를 반드시 거쳐가는 최소 비용 (골드5 난이도)
	•	N개의 도시와 M개의 도로가 있다.
	•	각 도로는 (출발, 도착, 비용) 형태이며 양방향이다.
	•	사람은 1번 도시에서 N번 도시로 이동하려 한다.
	•	단, 반드시 두 도시 v1, v2를 모두 거쳐야 한다. (순서는 상관 없음: 1 → v1 → v2 → N 또는 1 → v2 → v1 → N)
	•	최소 비용을 출력하라.
	•	만약 도달할 수 없다면 -1을 출력하라.

⸻
'''
import heapq
INF = 10**18

def daex(start,graph,n):
    cost = [INF] * (n+1)
    cost[start] = 0
    pq = [(0,start)]
    while pq:
        cost,n = heapq.heappop(pq)
        if cost > cost[n]:
            continue
        for u,w in graph[n]:
            nco = cost +w
            if nco < cost[n]:
                cost[n] = nco
                heapq.heappush(pq,(nco,u))

    return cost
print(cost[n] if cost[n] != INF else -1)
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int, input().split())
    graph[s].append((e,c))
    graph[e].append((s,c))
v1,v2 = map(int, input().split())
d1= daex[1,graph,n]
dv1 = daex[v1,graph,n]
dv2 = daex[v2,graph,n]

path1 = d1[v1] + dv1[v2] + dv2[n]
path2 = d1[v2] + dv2[v1] + dv1[n]
answ = min(path1,path2)
print(answ if answ < INF else -1)