square = lambda x: x * x
print(square(4))

add = lambda a, b: a + b
print(add(3, 5))

nums = [1, 2, 3]
print(list(map(
  lambda x: x * 2, nums)))

nums = [1, 2, 3, 4]
print(list(filter(
  lambda x: x % 2 == 0, nums)))

pairs = [(1, 3), (2, 1), (3, 2)]
print(sorted(pairs,
    key = lambda x: x[1]))
