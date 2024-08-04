num_inputs = int(input())

input_coords = []
for i in range(num_inputs):
    input_coords.append(list(map(int, input().split(' '))))

area = 0
for x in range(1, 101, 1):
    for y in range(1, 101, 1):
        in_paper = 0
        for j in input_coords:
            if (x > j[0]) and (x <= j[0] + 10) and (y > j[1]) and (y <= j[1] + 10):
                in_paper = 1
                break
        if in_paper:
            area += 1
print(area)