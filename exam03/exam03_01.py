def TowerofHanoi(round, source, dest, aux):
    if round>0:
        TowerofHanoi(round-1, source, aux, dest)
        pole_lst[aux-1].append(pole_lst[source-1].pop())
        print("move",round,"from ",chr(ord('A')+source-1), "to" ,chr(ord('A')+aux-1))
        print('|  |  |')
        printPole(n,pole_lst[0],pole_lst[1],pole_lst[2])
        TowerofHanoi(round-1, dest, source, aux)

def printPole(n, p1, p2 ,p3):
    if n!=0:
      if len(p1) >= n:
         print(p1[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if len(p2) >= n:
         print(p2[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      if len(p3) >= n:
         print(p3[n-1],end = '  ')
      else:
         print('| ',   end = ' ')
      print()
      printPole(n-1,p1,p2,p3)
    else:
        return

def init(n):
    if n == 0:
        return []
    return [n] + init(n-1)

n= int(input("Enter Input : "))
pole_lst = [[],[],[]]
pole_lst[0] = init(n)
print('|  |  |')
printPole(n,pole_lst[0],pole_lst[1],pole_lst[2])
TowerofHanoi(n,1,2,3)