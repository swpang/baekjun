inputs = input().split(' ')
inputs = list(map(int, inputs))
ideal = [1, 1, 2, 2, 2, 8]
results = [x - y for x, y in zip(ideal, inputs)]
for idx, item in enumerate(results):
    print(item)
    if idx != 5:
        print(' ')
