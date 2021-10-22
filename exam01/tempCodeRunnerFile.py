import time 
def placable(row, col):
    for prevCol in sol:
        if col == prevCol:
            return False
    for prevRow, prevCol in enumerate(sol):
        if abs(row - prevRow) == abs(col - prevCol):
            return False
    return True
startTime = time.time()
for n in range(2,17):
    sol = []
    row = 0
    col = 0
    count = 0
    first = True
    while True:
        while col < n:
            if placable(row, col):
                sol.append(col)
                col = 0
                row += 1
            else:   
                col += 1
        if row == n or col == n:
            if col == n and row != 0:
                col = sol[-1] + 1
                sol.pop()
                row -= 1
            if row == 0 and col == n:
                break
            if row == n - 1:
                sol.append(col - 1)
                count+=1
                sol.pop()
    print(f"\nBoard {n} x {n}")
    print("Number of Solutions = " + str(count))
    print("Time to Complete = ", 1000*(time.time() - startTime), "ms")
    startTime = time.time()