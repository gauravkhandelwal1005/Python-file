def fact(n):
  if(fact n == 0 or n == 1):
    return 1
return n * fact(n-1)

print(fact(5))
