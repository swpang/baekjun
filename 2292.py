# 1  
# 2 ~ 7 (6 = 2 + 2 + 2 + 0 + 0 + 0) 
# 8 ~ 19 (12 = 3 + 3 + 3 + 1 + 1 + 1) 
# 20 ~ 37 (18 = 4 + 4 + 4 + 2 + 2 + 2)
# 38 ~ 61 (24 = 5 + 5 + 5 + 3 + 3 + 3)
# 62 ~ 91 (30 = 6 + 6 + 6 + 4 + 4 + 4)

n = int(input())

min = 1
last = 1
while (last < n):
    last += (min + 1) * 3 + (min - 1) * 3
    min += 1
print(min)