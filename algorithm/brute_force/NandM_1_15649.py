import sys

def backtracking():
  if len(array) == m:
    print(' '.join(map(str, array)))
    return

  for i in range(1, n+1):
    if i not in array:
      array.append(i)
      backtracking()
      array.pop()


n, m = map(int, sys.stdin.readline().strip().split())
array = []

backtracking()