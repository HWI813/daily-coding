'''1️⃣ DFS 복습 — 영역의 개수 구하기 (실버 2)
	•	입력: M, N, K (격자 크기와 직사각형 개수)
	•	K개의 직사각형 좌표가 주어짐.
	•	출력: 칠해지지 않은 영역의 개수와, 각 영역의 넓이(오름차순).'''
from collections import deque
m,n,k = map(int,input().split())
kk = [[0] * n for _ in range(m)]
kkk = [[-1] * n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            kk[y][x] = -1

            


def bfs(sx,sy):
	q = deque()
	q.append((sx,sy))
	kkk[sx][sy] = 1
	dirs = [(-1,0),(1,0),(0,-1),(0,1)]
	for i in range(m):
		for j in range(n):
			if kk[j][i] == 0:
				
				sx,sy = kk[j][i] 
	q.append((sx,sy))
	
	land_cnt = 1
	while q:
		x,y = q.popleft()
		for dx,dy in dirs:
			nx,ny = x+dx,y+dy
			if 0<=nx<m and 0<=ny<n:
				if kk[nx][ny] == 0 and kkk[nx][ny] == -1:
					land_cnt +=1
					q.append((nx,ny))

	return land_cnt
areas = []
for i in range(m):
    for j in range(n):
        if kk[i][j] == 0 and not visited[i][j]:
            areas.append(bfs(i,j))
areas.sort()
print(len(areas))
print(*areas)				



      
            
    

m,n,k = map(int,input().split())
kk = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(x1,x2):
        for x in range(x1,x2):
            kk[y][x] = -1
def dfs(x,y):
    visited[x][y] = 1
    area = 1
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if  0 <= nx < m and 0 <= ny < n:
            if kk[nx][ny] ==0 and not visited[nx][ny]:
                area += dfs(nx,ny)
    return area
areas = []
for i in range(m):
    for j in range(n):
        if kk[i][j] == 0 and not visited[i][j]:
            areas.append(dfs(i,j))

areas.sort()
print(len(areas))
print(*areas)


''' 2번. 미로 탈출 (실버 1, BFS 최단거리)

문제 설명
	•	N×M 크기의 미로가 주어진다.
	•	0은 벽, 1은 길이다.
	•	(0,0)에서 시작해서 (N-1,M-1)까지 이동해야 한다.
	•	상하좌우로만 이동할 수 있다.
	•	최소 이동 칸 수를 출력하라. (시작 칸, 도착 칸도 포함)
	•	만약 이동할 수 없다면 -1을 출력한다.'''
n,m = map(int,input().split())
from collections import deque
q = deque()
miro = [list(map(int,input().strip())) for _ in range(n)] 
dist = [[-1]* (m) for _ in range(n)]
dist[0][0] = 1
q.append((0,0))
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
while q:
    x,y = q.popleft()
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m:
        	if dist[nx][ny] == -1 and miro[nx][ny]== 1:
                  
                  dist[nx][ny]=dist[x][y]+1
                  q.append((nx,ny)) 
print(dist[n-1][m-1])
            

'''24일차 3번: 특정 거리의 도시 찾기 (실버 2, 다익스트라/BFS 응용)

문제 설명
	•	N개의 도시(정점)와 M개의 도로(간선)가 있다.
	•	모든 도로의 거리는 1이다. (즉, BFS로 풀어도 되고 다익스트라로 풀어도 됨)
	•	시작 도시 X에서 출발해서 최단거리가 정확히 K인 모든 도시 번호를 출력하라.
	•	만약 그런 도시가 없다면 -1을 출력한다.'''

import heapq
INF = 10**18
n,m,k,x = map(int,input().split())
city= []*(n+1)
dist=[INF]*(n+1)
dist[x] = 0
graph = [[] for _ in range(n+1)]
pq = [(0,x)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
while pq:
    w,n = heapq.heappop(pq)
    if w > dist[u]:
        continue
    
    for x in graph[n]:
        nco = w+1
        if nco < dist[x]:
            dist[x] = nco
            heapq.heappush(pq,(nco,x))
ans = [i for i in range(1,n+1) if dist[i]==k]
if ans:
    for a in ans:
        print(a)
else:
    print(-1)


class DSU:
    def __init__(self,n):
        self.p = list(range(n+1))
        self.r = [0]*(n+1)
    def find(self,x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a,b = self.find(a), self.find(b)
        if a==b:
            return False
        if self.r[a] < self.r[b]:
            a,b = b,a
        self.p[x] = a
        if self.r[a] ==self.r[b]:
            self.r[a] +=1

        return True
n,m = map(int,input().split())
edge =[]
for _ in range(m):
    u,v,w = map(int,input().split())
    edge.append((w,u,v))
edge.sort()
ans = 0
bb = 0
d = DSU(n)
for w,u,v in edge:
    if d.union(u,v):
        ans +=1
        bb+=1
    if bb==(n-1):
        break
print(ans)