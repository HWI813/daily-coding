'''15일차 예제 문제

문제: 숨바꼭질

수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동할 수 있다.
	•	걷기: X-1 또는 X+1로 1초 후 이동
	•	순간이동: 2*X로 1초 후 이동

수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 출력하세요.'''
from collections import deque

n = int(input())
k = int(input())
max  = 100001
matrix = [-1]*max
matrix[n] =0
q = deque()
q.append(n)

while q:
    x = q.popleft()
    for dx in (x - 1, x + 1, x * 2): 
        if 0<=dx < max and matrix[dx] == -1:
            matrix[dx] = matrix[x] +1
            q.append(dx)
print(matrix[k])


'''15일차 응용 2번 문제: 숨바꼭질 3

수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 다음 세 가지 방법으로 이동할 수 있다.
	1.	걷기: X-1 또는 X+1 (1초 걸림)
	2.	순간이동: 2*X (0초 걸림)

⸻

❗목표:

수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 출력하시오.'''
from collections import deque

n = int(input())
k = int(input())
max  = 100001
matrix = [-1]*max
matrix[n] =0
q = deque()
q.append(n)

while q:
    x = q.popleft()
    for dx in (x - 1, x + 1, x * 2): 
        if 0<=dx < max and matrix[dx] == -1:
            if dx == x * 2:
                matrix[dx] = matrix[x]
                q.appendleft(dx)
            else:
            
                matrix[dx] = matrix[x] +1
                q.append(dx)
print(matrix[k])

''' 15일차 응용 3번 문제: 미로 탈출

수빈이는 미로의 (0, 0) 위치에서 탈출구 (n-1, m-1)로 이동해야 합니다.
미로는 0과 1로 이루어진 n × m 크기의 2차원 배열입니다.
	•	1은 이동할 수 있는 길이고
	•	0은 벽(이동 불가)입니다.

수빈이는 상, 하, 좌, 우로 한 칸씩 이동할 수 있습니다.
한 칸 이동하는 데 1초가 걸립니다.

⸻

✏ 입력
	•	첫째 줄에 n, m (2 ≤ n, m ≤ 100)
	•	둘째 줄부터 n개의 줄에 m개의 숫자 (0 또는 1)

⸻

🎯 출력
	•	(0, 0)에서 (n-1, m-1)까지 최단 이동 시간을 출력하시오.
	•	탈출이 불가능한 경우 -1 출력'''
from collections import deque
n, m = map(int, input().split())
matrix  = [list(map(int,input().strip()) )for _ in range(n)]
q = deque()
q.append((0,0))
directions = [(0,-1),(0,1),(-1,0),(1,0)]
while q:
    x,y = q.popleft()
    for dx, dy in directions:
        nx,ny = x+dx, y+dy
        if nx<0 or nx >=n or ny <0 or ny >=m:
            continue
        if matrix[nx][ny] != 1:
            continue
        matrix[nx][ny] = matrix[x][y] + 1
        q.append((nx,ny))
print(matrix[n-1][m-1])

'''15일차 응용 4번: 점프 점프

수빈이는 숫자가 적힌 직선 위 칸에 서 있습니다.
각 칸에는 점프할 수 있는 최대 거리가 적혀 있습니다.
수빈이는 0번 칸에서 출발하여 n-1번 칸까지 최소 점프 횟수로 도달하려고 합니다.

수빈이는 한 번 점프할 때 1칸 이상, 해당 칸의 숫자만큼 이하 거리로만 이동할 수 있습니다.

⸻

✏ 입력
	•	첫 줄에 정수 n (1 ≤ n ≤ 1,000)
	•	둘째 줄에 n개의 정수 a₀, a₁, …, aₙ₋₁ (0 ≤ aᵢ ≤ 100)

⸻

🎯 출력
	•	n-1번 칸에 최소 몇 번 점프로 도달할 수 있는지 출력
	•	도달할 수 없으면 -1 출력'''
from collections import deque
n = int(input())
l = list(map(int, input().split()))

q = deque()
q.append(0)
dis = [-1] * n
dis[0] = 0
cnt = 0
while q:
    x = q.popleft()
    for i in range(1, l[x]+1):
        nx = x+ i
        if nx >= n:
            continue
        if  dis[nx] == -1:
            dis[nx] = dis[x] +1
            q.append(nx)

        
print(dis[n-1])
'''15일차 응용 5번 문제: 탈출

문제 설명
	•	미로의 크기는 R×C이며, 각 칸은 다음 중 하나로 이루어져 있습니다:
	•	'.': 비어 있는 곳
	•	'*': 물이 차 있는 곳
	•	'X': 돌
	•	'D': 비버의 굴 (목표 지점)
	•	'S': 고슴도치의 시작 위치
	•	매 초마다 고슴도치는 인접한 네 칸(상하좌우) 중 하나로 이동 가능
단, 물이 차 있는 칸과 돌, 그리고 이미 물이 찬 칸은 이동할 수 없습니다.
	•	물은 고슴도치보다 먼저 인접한 빈 칸으로 퍼져나갑니다.
	•	고슴도치가 **비버의 굴(D)**에 도착하는 최소 시간을 구하세요.'''
from collections import deque
r,c = map(int, input().split())
miro = [list(input()) for _ in range(r)]

water = [[-1]*c for _ in range(r)]
dist = [[-1]* c for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()

# 물먼저
for i in range(r):
    for j in range(c):
        if miro[i][j] == '*':
            q.append((i,j))
            water[i][j]=0

while q:
    x,y = q.popleft()
    for dir in range(4):
        nx = x+ dx[dir]
        ny = y + dy[dir]
        if 0<= nx < r and 0 <=ny < c:
            if miro[nx][ny] == '.' and water[nx][ny] == -1:
                water[nx][ny] = water[x][y] +1
                q.append((nx,ny))

q= deque()
for i in range(r):
    for j in range(c):
        if miro[i][j] == 'S':
            q.append((i,j))
            dist[i][j]=0

while q:
    x,y = q.popleft()
    for dir in range(4):
        nx = x+ dx[dir]
        ny = y + dy[dir]
        if 0<= nx < r and 0 <=ny < c:
            if miro[nx][ny] == 'D':
                print(dist[x][y]+1)
                exit()
            if miro[nx][ny] == '.' and dist[nx][ny] == -1:
                if water[nx][ny] ==-1 or water[nx][ny] > dist[x][y]+1:
                    dist[nx][ny] = dist[x][y] +1
                    q.append((nx,ny))
print('KAKTUS')