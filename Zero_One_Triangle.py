rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()
