print(" Fun with countdown ")
x = list(map(int, input("Enter List : ").split()))
x.append(-1)
ans = []
ans1 = []
checkAns = []
checkAns0 = []
check = 0 
count = 0
for i in range(0,len(x)-1,1):
    if x[i] == 1:
        count += 1
ans.append(count)
ans.append(ans1)
for i in range(0,len(x)-1,1):

    if x[i] == 1:
        checkAns.append(x[i])
        checkAns0 = checkAns.copy()
        ans1.append(checkAns0)
        checkAns.clear()
    elif x[i] == x[i+1] + 1:
        checkAns.append(x[i])

print(ans)