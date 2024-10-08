import sys

def dfs(start, depth):
  global min
  if depth == n//2:
    start = 0
    link = 0
    for i in range(n):
      for j in range(n):
        if visited[i] and visited[j]:
          start += S[i][j]
        elif not visited[i] and not visited[j]:
          link += S[i][j]
    if min > abs(start - link):
      min = abs(start-link)
    return


  for i in range(start, n):
    if not visited[i]:
      visited[i] = 1
      dfs(i+1, depth+1)
      visited[i] = 0



n = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
min = float('inf')
visited = [0] * n
dfs(0, 0)
print(min)
