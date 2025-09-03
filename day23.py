class DSU:
    def __init__(self, n):
        self.p = list(range(n+1))
        self.r = [0]*(n+1)
    def find(self,x):
        if self.p[x]!= x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a,b = self.find(a),self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a,b = b,a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] +=1
        return True
n,m = map(int, input().split())
edge = []
for _ in range(m):
    u,v,w = map(int,input().split())
    edge.append((w,u,v))
edge.sort()
ans = 0
bb = 0
ddd = DSU(n)
for w,u,v in edge:
    if ddd.union(u,v):
        ans += w
        bb +=1 
    if bb == (n-1):
        break
print(ans)

import heapq
INF = 10**18
n,m,t,s,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
dist[s] = 0
pq = [(0,s)]
for _ in range(m):
    u,v,w,c = map(int,input().split())
    graph[u].append((w,v,c))

while pq:
    cost,k = heapq.heappop(pq)
    if cost > dist[k]:
        continue
    for w,v,c in graph[k]:
        nco = cost + w + (t if c==1 else 0)
        if nco < dist[v]:
            dist[v] = nco
            heapq.heappush(pq,(nco,v))
print(dist[e] if dist[e] != INF else -1)


'''23일차 3번 문제: K번째 최단 경로 (골드4 · 다익스트라 응용)

문제 설명
	•	N개의 도시와 M개의 도로가 있다. (도로는 방향)
	•	각 도로는 (u → v, w) 형식으로 주어지며, 가중치는 양의 정수다.
	•	1번 도시에서 N번 도시로 가는 최단 경로들 중 K번째로 짧은 경로의 길이를 구하라.
	•	만약 K번째 경로가 존재하지 않으면 -1을 출력한다.'''
import heapq
n,m,k = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist =  [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
pq = [(0,1)]
heapq.heappush(dist[0],0)
while pq:
    cost, l = heapq.heappop(pq)
    for v,w in graph[l]:
        nco = cost+w
        if len(dist[v])<k:
            heapq.heappush(dist[v], -nco)
            heapq.heappush(pq,(nco, v))
        elif -dist[v][0] > nco:
            heapq.heappop(dist[v])
            heapq.heappush(dist[v],-nco)
            heapq.heappush(pq,(nco, v))

if len(dist[n]) < k:
    print(-1)
else:
    print(-dist[n][0])


''' 문제: K번째 작은 수 경로 찾기 (골드 2 ~ 3 난이도)

문제 설명
	•	N×N 격자가 있음.
	•	각 칸에는 자연수가 적혀 있음.
	•	(1,1) → (N,N) 까지 이동하려고 한다.
	•	이동은 오른쪽, 아래쪽만 가능하다.
	•	경로에 적힌 숫자들을 더했을 때의 경로 합을 고려한다.
	•	이때, (1,1)에서 (N,N)까지 가능한 경로 합 중 K번째로 작은 값을 구하라.'''
import heapq
n,k = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[[] for _ in range(n)] for __ in range(n)]
dirs = [(1,0),(0,1)]
pq = [(graph[0][0],0,0)]
dist[0][0].append(-graph[0][0])

while pq:
    cost,x,y = heapq.heappop(pq)
    for dx,dy in dirs:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0 <= ny <n:
			nco = cost + graph[nx][ny]
			if len(dist[nx][ny]) < k:
				heapq.heappush(dist[nx][ny],-nco)
				heapq.heappush(pq,(nco,nx,ny))
			elif -dist[nx][ny][0]>nco:
				heapq.heappop(dist[nx][ny])
				heapq.heappush(dist[nx][ny],-nco)
				heapq.heappush(pq,(nco,nx,ny))
