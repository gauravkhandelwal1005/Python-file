n = 5
for i in range(1, n + 1):
  s = '123456789'[:i]
  mid = s + s[-2::-1]
  print(mid.center(2 * n - 1))
