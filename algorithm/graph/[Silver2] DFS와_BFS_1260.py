import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().strip().split())
graph = [[False] * (N+1) for _ in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = True

visited1 = [False] * (N+1) #dfs
visited2 = [False] * (N+1) #bfs

def bfs(V):
  q = deque([V])
  visited2[V] = True
  while q:
    V = q.popleft()
    print(V, end=" ")
    for i in range(1, N + 1):
      if not visited2[i] and graph[V][i]:
        q.append(i)
        visited2[i] = True

def dfs(V):
  visited1[V] = True
  print(V, end=" ")
  for i in range(1, N+1):
    if not visited1[i] and graph[V][i]:
      dfs(i)

dfs(V)
print()
bfs(V)
