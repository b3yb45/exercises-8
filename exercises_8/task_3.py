A = 1
B = 200
C = 7
D = 7

out = list(map(lambda x: (x % C != 0) and (x % 10) == D, range(A, B)))
print(sum(out))
