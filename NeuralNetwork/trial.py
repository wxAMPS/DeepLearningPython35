import numpy as np

# float_formatter = lambda x: "%.2f" % x
# np.set_printoptions(formatter={'float_kind': float_formatter})
input = [2, 3, 1]
str = [np.random.randn(y, 1).tolist() for y in input]
print(str)
# print([y for y in input])
# print(list(zip(input[:-1], input[1:])))
# print([np.random.randn(y, x).tolist() for x, y in zip(input[:-1], input[1:])])
# print(input[:-1])
# print(input[1:])
