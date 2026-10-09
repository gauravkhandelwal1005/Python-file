n = 5
for i in range(1 - n, n):
  s = '*' * (2 * (n - abs(i)) - 1)
  print(s.center(2 * n - 1))
