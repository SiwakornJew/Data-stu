lst1=[]
stack=[]
countp=0
counta=0
lst1 = list(map(str,input("Enter Input : ").split(",")))
for x in range(len(lst1)) :
   if 'A' in lst1[x]:
       counta+=1
       print("Add = "+str(lst1[x][2:])+" and Size = "+str(counta))
       stack.append(lst1[x][2:])
   else:
     if 'P' in lst1[x] and stack:
        p=stack.pop()
        counta-=1
        print("Pop = "+str(p)+" and Index = "+str(counta))
     else:
        print("-1")
if(not stack):
    print("Value in Stack = Empty")
else:
    print("Value in Stack = "+str(stack)[1:-1].replace('\'','').replace(' ','').replace(',',' '))

