from itertools import permutations
import time
start_time = time.time()


def print_table(N):
    for row in range(N):
        print(table[row])

def put_queen(x,y,N):
    if table[y][x] == 0:
        for m in range(N):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= N-1 and x+m <= N-1:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= N-1:
                table[y-m][x+m] = 1
            if y+m <= N-1 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False
for N in range(2,17):
    table = [[0]*N for _ in range(N)]
    plist=[]
    for n in range(N):
        plist.append(n)
    perms = permutations(plist)
    num_comb = 0
    for perm in perms:
        cout = 0
        for i in range(N):
            if put_queen(perm[i],i,N) == True:
                cout+=1
        if cout == N :
            num_comb += 1
        table =[[0] * N for _ in range(N)]
    print(f"solution{num_comb}")
    print(" Bord %s x %s --- %s milliseconds ---" % (N,N,(time.time() - start_time)*1000))
    start_time=time.time()
