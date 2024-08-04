lines = []
for i in range(5):
    lines.append(input())

for j in range(15):
    for i in lines:
        if j < len(i):
            print(i[j], end = '')
        else:
            continue