from collections import deque
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dist = [-1] * (n+1)
dist[1] = 0
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in graph[x]:
        if dist[i] == -1:
            dist[i] = dist[x] +1
            q.append(i)
max_dist = max(dist[1:])
target = [i for i,d in enumerate(dist) if d == max_dist]
print(max_dist, target[0], len(target) )


from collections import deque
n = int(input())
wall = [list(map(int,input().split())) for _ in range(n)]
max_mul = max(max(wall))
def safe_land(wall,mul,n):
    visited = [[False]*n for _ in range(n)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    areas = 0
    q = deque()
    def bfs(sx,sy):
        q.append([sx,sy])
        
        visited[sx][sy] = True
        q.append((sx,sy))
        while q:
            x,y = q.popleft()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx < n and 0<=ny<n:
                    if wall[nx][ny] > mul and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
    for i in range(n):
            for j in range(n):
                if not visited[i][j] and wall[i][j] >mul:
                    bfs(i,j)
                    areas +=1 
    return areas
ans = 0
for i in range(max_mul+1):

    ans = max(ans,safe_land(wall,i,n))
print(ans)


'''20일차 3번 문제: 유기농 배추 (실버2, BFS/DFS 연습)
	•	N×M 밭에 배추가 심어져 있다.
	•	배추는 상하좌우로 연결되어 있으면 하나의 배추흰지렁이가 관리할 수 있다.
	•	밭 전체에 최소 몇 마리의 지렁이가 필요한지 출력하라.
	•	즉, 연결된 배추 덩어리 개수를 구하는 문제다.'''
from collections import deque
t = int(input())
ji = 0
def find_ji(graph):
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque()
    global ji
 
    def bfs(sx,sy):
        visited[sx][sy] = True
        deque((sx,sy))
        while q:
            x,y = q.popleft()
            for dx, dy in dirs:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    if graph[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] =True
                        q.append((nx,ny))
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and graph[i][j] ==1:
                bfs(i,j)
                ji +=1
    return ji
for _ in range(t):
	
    m,n,k = map(int,input().split())
    visited = [[False] *m for _ in range(n)]
    graph = [[-1] * m for _ in range(n)] 
    for _ in range(k):
        a,b = map(int, input().split())
        graph[b][a]= 1
    print(find_ji(graph))


    import heapq
INF = 10 ** 18
n,m,s,t = map(int,input().split())
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
dist[s] =0
for _ in range(m):
    u,v,m = map(int,input().split())
    graph[u].append((v,m))
prev = [-1]*(n+1)
pq = [(0,s)]
while pq:
    cost, n = heapq.heappop(pq)
    if dist[n] < cost:
        continue
    for v,m in graph[n]:
        nco = m+cost
        if nco < dist[v]:
            dist[v] = nco
            prev[v] = n
            heapq.heappush(pq,(nco,v))
if dist[t] == INF:
    print('INF')
else:
    path = []
    cur = t
    while cur != -1:
        path.append(cur)
        cur=prev[cur]
    path.reverse()
    print(dist[t])
    print(len(path))
    print(*path)