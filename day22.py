'''문제 요약
	•	정점 N(1~N), 간선 M.
	•	각 간선: u v w (u–v를 비용 w로 연결, 양방향)
	•	모든 정점을 연결하는 최소 비용을 구하라. 
    (항상 연결 가능하다고 가정하지 않는다면, 연결 불가 시 처리 필요)
'''
class dsu:
    def __init__(self,n):
        self.p = list(range(n+1))
        self.r = [0]*(n+1)
    def find(self,x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a,b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a,b = b,a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] +=1
        return True

n,m = map(int,input().split())
edges = []

for _ in range(m):
    u,v,w = map(int,input().split())
    edges.append((w,u,v))
ds = dsu(n)
edges.sort()
ans = 0
picked = 0
for w,u,v in edges:
    if ds.union(u,v):
        ans +=w
        picked +=1
    if picked == n-1:
        break
print(ans)

'''22일차 2번: 도시 분할 계획 (MST 응용 · 실버1~골드5)

문제

N개의 집(정점)과 M개의 도로(간선, 양방향, 비용)가 있다.
모든 집을 연결하는 마을 네트워크를 만들고 싶지만, 마을을 두 개로 분할하려 한다.
즉, 모든 집은 두 마을 중 하나에 속하고, 각 마을 내부는 연결되어야 하며(사이클 없어도 됨), 두 마을을 잇는 도로는 없도록 하려고 한다.

이때 각 마을 내부 도로 비용의 합을 최소로 하려면, 선택해야 할 도로들의 총 비용의 최소값을 구하라.

아이디어 힌트
	•	전체를 하나의 MST로 만든 뒤, 가장 비용이 큰 간선 1개를 제거하면 두 개의 연결 요소로 나뉘고, 그 합이 최소가 된다.

입력
	•	첫 줄: N M (2 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000)
	•	다음 M줄: A B C (1 ≤ A, B ≤ N, A ≠ B, 1 ≤ C ≤ 10^6)
	•	A–B를 비용 C로 연결하는 양방향 도로

출력
	•	두 마을로 분할했을 때 선택된 도로 비용의 합의 최소값을 출력'''
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
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a,b = b,a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] +=1
        return True
n,m = map(int,input().split())
edge = []
for _ in range(m):
    u,v,w = map(int,input().split())
    edge.append((w,u,v))
edge.sort()
ds = DSU(n)
ens = 0
pi = 0
max_e = 0
for w,u,v in edge:
    if ds.union(u,v):
        ens += w
        pi += 1
        if w > max_e:
            max_e = w
    if pi == n-1:
        break
print(ens - max_e)


import heapq
INF = 10 ** 18
n,m = map(int,input().split())
graph = [] * (n+1)
dist = [INF] *(n+1)
par = [-1] * (n+1)
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
dist[1] = 0
pq = [(0,1)]
while pq:
    cost,start = heapq.heappop(pq)
    if cost > dist[start]:
        continue
    for v,w in graph[start]:
        nco = w+ cost
        if nco < dist[v]:
            dist[v] = nco
            par[v] = start
            heapq.heappush(pq,(nco,v))
if dist[n] == INF:
    print(-1)
else:
    print(dist[n])
    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = par[cur]
    path.reverse()
    print(len(path))
    print(*path)