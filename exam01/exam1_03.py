lst =[int(i) for i in input("Enter number end with (-1) : ").split()]
if -1 not in lst:
    print("Invalid INPUT !!!")
    exit()
max =None
numMax=None
counter=0
di=dict()
for n in lst:
    if n==-1:
        break
    di[n] =di.get(n,0) +1
    if max ==None or max < di[n]:
        max =di[n]
        numMax = n
print(di)
for v in di.values():
    if v == max:
        counter +=1
if len(di) == 0 or counter > 1 or max < sum(x for x in di.values())/2:
    print("Not found")
    exit()
print(numMax)