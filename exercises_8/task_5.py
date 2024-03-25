from functools import reduce
A = 1
B = 20
C = 2

out = reduce(lambda x, y: x * y, filter(lambda x: (x % C == 0) and (x ** 0.5 == int(x ** 0.5)), range(A, B)))
print(out)
