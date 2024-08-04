N = int(input())
Max = 2 * N - 1
sweep = list(range(1,N+1,1)) +  list(range(N-1,0,-1))

for i in sweep:
    star = 2 * i - 1
    blank = int((Max - star) / 2)
    for j in range(blank):
        print(" ", end='')
    for j in range(star):
        print("*", end='')
    for j in range(blank):
        print(" ", end='')
    print('')
