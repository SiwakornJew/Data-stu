print("*** Fun with countdown ***")
x = list(map(int, input("Enter List : ").split()))
x.append(-1)
a=[]
a1=[]
cheakA=[]
cheakA1=[]
cheak=[]
count=0
for i in range(0,len(x)-1,1):
    if x[i] == 1:
        count += 1
a.append(count)
a.append(a1)
for i in range(0,len(x)-1,1):

    if x[i] == 1:
        cheakA.append(x[i])
        cheakA1 = cheakA.copy()
        a1.append(cheakA1)
        cheakA.clear()
    elif x[i] == x[i+1] + 1:
        cheakA.append(x[i])

print(a)