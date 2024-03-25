A = 1
B = 175
C = 5
D = 7

nums_sum = sum(set(filter(lambda x: (x % C == 0) and (x % D == 0), range(A, B+1))))
print(nums_sum)
