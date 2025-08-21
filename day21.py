'''1번. 숨바꼭질 (실버 1, BFS 최단거리)
	•	문제
수빈이는 현재 점 N에 있고, 동생은 점 K에 있다.
수빈이는 1초마다 다음 세 가지 행동 중 하나를 할 수 있다.
	•	x-1, x+1, x*2
수빈이가 동생을 찾는 최소 시간을 출력하라.'''
from collections import deque
n,k = map(int,input().split())
maxxx= 100000
time = [-1] * (maxxx+1)
q = deque()
q.append(n)
time[n] = 0
while q:
    x = q.popleft()
    for nx in (x-1,x+1,x*2):
        if 0<=t<maxxx and time[nx] == -1:
            time[nx] = time[x]+1
            q.append(nx)
print(time[k])


'''2번. 트리의 부모 찾기 (실버 2, DFS/BFS)
	•	문제
루트가 1인 트리가 주어진다. 각 노드의 부모를 구해 출력하라.'''
k = int(input())
node = [[] for _ in range(k+1)]
for _ in range(k-1):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
visited = [False] * (k+1)
parent = [0]*(k+1)
def dfs(u):
    visited[u] = True
    
    for i in node[u]:
        if not visited[i]:
            parent[i]= u
            dfs(i)

    return parent
pp = dfs(1)
for i in range(2, k+1):
    print(parent[i])


'''Kruskal 대표 문제

문제명(유형): 최소 스패닝 트리 / MST (간선 중심, Union-Find)
설명: 정점 N(1~N), 간선 M이 주어질 때, 모든 정점을 연결하는 
최소 비용의 스패닝 트리의 가중치 합을 출력.
입력 형식
N M
u1 v1 w1
u2 v2 w2
...
uM vM wM
•	1 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000 정도(플랫폼마다 다를 수 있음)
•	간선은 무방향, (ui, vi, wi): 정점 ui—vi 사이 가중치 wi
출력 형식
	•	MST의 총 가중치

풀이 아이디어(요약)
	1.	간선을 가중치 오름차순 정렬
	2.	Union-Find로 사이클이 생기지 않으면 간선 채택
	3.	N-1개 간선이 선택되면 종료'''

class DSU:
    def __init__(self,n):
        self.p = list(range(n+1))
        self.r = [0]*(n+1)

    def find(self, x):
        if self.p[x] !=x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self,a,b):
        a,b = self.find(a), self.find(b)
        if a==b:
            return False
        if self.r[a] < self.r[b]:
            a,b = b,a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] +=1 
        return True

n,m = map(int, input().split())
edges = []
for _ in range(m):
    u,v,m = map(int,input().split())
    edges.append((w,u,v))

edges.sort()
dsu = DSU(n)
ans = 0
picked = 0

for w,u,v in edges:
    if dsu.union(u,v):
        ans += w
        picked += 1
        if picked == n-1:
            break
print(ans)


'''📌 21일차 3번 문제: 최소 스패닝 트리 (골드 4, MST 입문)

문제
	•	그래프가 주어진다. (정점 N, 간선 M)
	•	간선에는 가중치가 있음.
	•	그래프에서 모든 정점을 연결하는 최소 비용을 구하라.
	•	단, 그래프는 항상 연결되어 있음.
'''
class DSU:
    def __init__(self,n):
        self.p = list(range(n+1))
        self.r = [0] * (n+1)

    def find(self,x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, a,b):
        a,b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a,b = b,a 
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True
n,m = map(int,input().split())
edges = []
for _ in range(m):
    u,v,w = map(int,input().split())
    edges.append((u,v,w))
edges = sorted(edges, key=lambda x: x[2])
ans = 0
picked = 0
dsu = DSU(n)
for u,v,w in edges:
    if dsu.union(u,v):
        ans +=w
        picked +=1
    if picked == n-1:
        break
print(ans)


'''2) Prim 대표 문제

문제명(유형): 네트워크 연결 / MST (정점 중심, 우선순위 큐)
설명: N개의 컴퓨터(정점)와 M개의 연결(간선), 각 연결 비용이 주어진다.
모든 컴퓨터를 연결하는 최소 비용을 출력.
입력
N
M
u1 v1 w1
u2 v2 w2
...
uM vM wM
출력 형식
	•	MST의 총 가중치

풀이 아이디어(요약)
	1.	임의의 시작 정점에서 시작(보통 1)
	2.	방문 집합과 비방문 집합을 잇는 최소 비용 간선을 우선순위 큐로 유지
	3.	매번 가장 싼 간선으로 새로운 정점을 추가
    '''
import heapq
n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))
    graph[v].append((v,w))
visited = [False] * (n+1)
pq = []

start = 1
visited[start] = True
for w,v in graph[start]:
    heapq.heappush(pq,(w,start,v))
ans = 0
cnt = 0

while pq and cnt < n-1:
    w,u,v = heapq.heappop(pq)
    if visited[u]:
        continue
    visited[u] =True
    ans+=1
    cnt+=1
    for nw,nv in graph[v]:
        if not visited[nv]:
            heapq.heappush(pq,(nw,v,nv))
print(ans)