'''창고에 토마토가 저장돼 있다.
	•	1: 익은 토마토
	•	0: 익지 않은 토마토
	•	-1: 빈 칸
하루가 지나면 익은 토마토의 상하좌우에 있는 익지 않은 토마토가 익는다.
모든 토마토가 다 익는 데 걸리는 최소 일수를 출력하라.
처음부터 전부 익어 있으면 0, 끝까지 못 익으면 -1.'''
from collections import deque
m,n = map(int, input().split())
q = deque()
tomato = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i,j))
directions = [(-1,0),(1,0),(0,-1),(0,1)]
while q:
    x,y = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
            tomato[nx][ny]  =  tomato[x][y] +1
            q.append((nx,ny))

an = 1
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            an = -1
            exit()
        an = max(an, tomato[i][j])
print(an-1)

        
'''문제
	•	크기: 세로 M, 가로 N인 격자(좌표는 0 ≤ x < N, 0 ≤ y < M)
	•	K개의 직사각형이 주어지고, 해당 영역은 칠해져 있음(막힘)
	•	칠해지지 않은 칸들끼리 상하좌우로 연결된 덩어리(영역)의 개수와, 각 영역의 넓이를 오름차순으로 출력'''
from collections import deque
q = deque()
m,n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            board[y][x] = 1

directions = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(yy,xx):
    q= deque()
    q.append((yy,xx))
    board[yy][xx] = 1
    area = 1
    while q:
        y,x = q.popleft()
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and board[ny][nx] == 0:
                board[ny][nx] =1
                area +=1
                q.append((ny,nx))
    return area
areas = []
for y in range(m):
    for x in range(n):
        if board[y][x] == 0:
            areas.append(bfs(y,x))
print(areas)

# dfs
from collections import deque
q = deque()
m,n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            board[y][x] = 1
directions = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(y,x):
    area = 1
    board[y][x] = 1
    for dx, dy  in directions:
        nx, ny = x + dx, y+ dy
        if 0 <= nx < n and 0<=ny <m and board[nx][ny]==0:
            area += dfs(ny,ny)
    return area

areas = []
for y in range(m):
    for x in range(n):
        if board[y][x] == 0:
            areas.append(dfs(y,x))
print(len(areas))

from collections import deque
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def bfs(x,y, board, h,w, visited):
    q = deque()
    q.append((x,y))

    while q:
        y,x = q.popleft()
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            if 0<= ny<h and 0<=nx<w:
                if not visited[ny][nx] and board[ny][nx]==1:
                    visited[ny][nx]=0
                    q.append((ny,nx))
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    count = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] == 1 and not visited[y][x]:
                bfs(y, x, board, h, w, visited)
                count += 1
    print(count)

    from collections import deque
n,m = map(int, input().split())
miro = [list(map(int,input().split())) for _ in range(n)]
gil = [[[0]*2 for _ in range(m)]for __ in range(n)]
directions = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs():
    q = deque()
    q.append((0,0,0))
    gil[0][0][0]=1
    while q:
        y,x,used = q.popleft()
        if y == n-1 and x == m-1:
            return gil[y][x][used]
        for dy, dx in directions:
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx <m:
                if miro[ny][nx]==0 and gil[ny][nx][used] == 0:
                    gil[ny][nx][used] = gil[y][x][used] +1
                    q.append((ny,nx,used))
                elif miro[ny][nx]==1 and used ==0 and gil[ny][nx][1]==0:
                    gil[ny][nx][1] = gil[y][x][used] +1
                    q.append((ny,nx,1))
    return -1
print(bfs())


'''예시 문제: 불! (Fire Escape)
	•	미로에 불이 번지고 있음.
	•	지훈이가 탈출해야 함.
	•	불은 매 초 4방향으로 번짐.
	•	지훈이는 불이 번진 칸으로 갈 수 없음.
	•	가장자리에 도달하면 탈출 성공.'''
from collections import deque
r,c = map(int, input().split())
grid = [list(input().strip)for _ in range(r)]

fire = [[-1]*c for _ in range(r)]
dis = [[-1]*c for _ in range(r)]

df = deque()
dd = deque()

for y in range(r):
    for x in range(c):
        if grid[y][x] =='F':
            df.append((y,x))
            fire[y][x] =0
        elif grid[y][x]=='J':
            sy,sx = y,x

directions = [(-1,0),(1,0),(0,-1),(0,1)]
while df:
    y,x = df.popleft()
    for dy, dx in directions:
        ny, nx = y+dy, x+dx
        if 0<=ny<r and 0<= nx<c:
            if grid[ny][nx] != '#' and fire[ny][nx] == -1:
                fire[ny][nx] = fire[y][x] + 1
                df.append((ny, nx))

dd.append((sy, sx))
dist[sy][sx] = 0


if sy == 0 or sy == r-1 or sx == 0 or sx == c-1:
    print(1)
    exit()

while dd:
    y, x = dd.popleft()
    t = dis[y][x]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        nt = t + 1
        if not (0 <= ny < r and 0 <= nx < c):
            print(nt)
            exit()

        if grid[ny][nx] == '#' or dis[ny][nx] != -1:
            continue
        if fire[ny][nx] != -1 and nt >= fire[ny][nx]:
            continue

        dis[ny][nx] = nt
        dd.append((ny, nx))

print("IMPOSSIBLE")
            
