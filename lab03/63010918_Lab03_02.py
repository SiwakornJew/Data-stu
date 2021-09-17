def ManageStack(lst1):
  stack=[]
  counta=0
  for x in range(len(lst1)) :
   if 'A' == str(lst1[x])[0:1]:
       counta+=1
       print("Add = "+str(lst1[x][2:]))
       stack.append(lst1[x][2:])
   elif 'P' == str(lst1[x])[0:1] and stack:
        p=stack.pop()
        counta-=1
        print("Pop = "+str(p))  
   elif 'LD' == str(lst1[x])[0:2] and stack:
        a=len(stack)
        countAD=0
        for i in range(a) : 
             if stack[i] < lst1[x][3:]:countAD+=1
        if a-countAD==0:
           continue
        for i in range(a-countAD-1,-1,-1) :
          if int(stack[i]) < int(lst1[x][3:]):
           print("Delete = "+stack[i] +" Because "+stack[i]+" is less than "+lst1[x][3:])
           stack.remove(stack[i])
          elif int(stack[0]) < int(lst1[x][3:]) and i ==0:
           print("Delete = "+str(int(stack[0])) +" Because "+stack[0]+" is less than "+str(int(lst1[x][3:]))+str(i))
           stack.remove(stack[0])

   elif 'MD' == str(lst1[x])[0:2] and stack:
        a=len(stack)
        countMD=0
        for i in range(a) : 
             if stack[i] > lst1[x][3:]:countMD+=1
        for i in range(a-countMD) :
          if stack[i] > lst1[x][3:]:
           print("Delete = "+stack[i] +" Because "+stack[i]+" is more than "+lst1[x][3:])
           stack.remove(stack[i])
          if stack[0] > lst1[x][3:]:
           print("Delete = "+stack[0] +" Because "+stack[0]+" is more than "+lst1[x][3:])
           stack.remove(stack[0])
           

   elif 'D' == str(lst1[x])[0:1] and stack:
      
        a=len(stack)
        countD=0
        for i in range(a) : 
             if stack[i] == lst1[x][2:]:countD+=1
        if a-countD==0:
             d=1
        else:
            d=a-countD
        for i in range(d) :
          if int(stack[i]) == int(lst1[x][2:]):
           print("Delete = "+stack[i])
           stack.remove(stack[i])
          if int(stack[0]) == int(lst1[x][2:]):
           print("Delete = "+stack[0])
           stack.remove(stack[0])

   else :
        print("-1")

  if(not stack):
     print("Value in Stack = ",end="")
     print(stack)
  else:
     print("Value in Stack = ",end="")
     print(str(stack).replace('\'',''))

lst1=[]
lst1 = list(map(str,input("Enter Input : ").split(",")))

ManageStack(lst1)

