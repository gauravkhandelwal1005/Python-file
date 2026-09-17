def fact(n):
  if(fact n == 0 or n == 1):
    return 1
return n * fact(n-1)

print(fact(5))

def num_val(n):
  if(n == 0):
    return 0
  return fact(n-1) + 1

sum = num_val(10)
print(sum)
