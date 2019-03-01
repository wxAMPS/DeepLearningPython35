def output(n):
    print('lala %d' % n)


def addW(x):
    return x[0] * x[1]


input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
labels = [1, 0, 0, 0]
weights = [0, 0]
samples = zip(input_vecs, labels)
for (input_vec, label) in samples:
    vec = zip(input_vec, weights)
    print(input_vec, weights, list(vec))
    weights = list(map(addW, [[1, 2], [2, 3]]))
    print(list(weights))
