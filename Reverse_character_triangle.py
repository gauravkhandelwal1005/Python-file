from string import ascii_uppercase

n = 5
for i in range(1, n + 1):
  print(*ascii_uppercase[n - i:n])
