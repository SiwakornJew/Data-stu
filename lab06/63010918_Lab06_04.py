a = []
b = []
c = []
def move(n, start, filler, dest, maxn):
    return
def pop(start, dest):
    if start == 'A':
        x = a.pop(0)
    elif start == 'B':
        x = b.pop(0)
    else:
        x = c.pop(0)
    if dest == 'A':
        a.insert(0,x)
    elif dest == 'B':
        b.insert(0,x)
    else :
        c.insert(0,x)
def showTower(maxn, row):
    global a
    global b
    global c
    acp = a[::-1]
    bcp = a[::-1]
    ccp = a[::-1]
    if row == maxn:
        print('| | |')
    if len(a) >= row:
        print(f"{acp[row-1]}  ",end="")
    else:
        print('|  ',end='')
    if len(a) >= row:
        print(f"{bcp[row-1]}  ",end="")
    else:
        print('|  ',end='')
    if row !=0:
        print()
    showTower(maxn, row-1)

def move(n, start, filler, dest, maxn):
    if n == 1:
        print(f"move {n} from {start} to {dest}")
        pop(start, dest)
        showTower(maxn, maxn)
    else:
        move(n-1, start, dest, filler, maxn)
        print(f"move {n} from {start} to {dest}") 
        pop(start, dest)
        showTower(maxn, maxn)
        move(n-1, filler, start, dest, maxn)

def rec_init_a(num, target):
    global a
    if num <= target:
        a.append(num)
        rec_init_a(num+1, target)  

n = int(input("Enter Input : "))
rec_init_a(1, n)
showTower(n, n)
move(n, 'A', 'B', 'C', n)
