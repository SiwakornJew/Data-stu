class Stack:
    def __init__(self,list = None) :
        if list== None :
            self.items = []
        else :
            self.items = list
    def push(self,i):
            self.items.append(i)
    def pop(self) :  
            return self.items.pop(len(self.items)-1)  
    def isEmpty(self) :
            return self.items==[]
    def size(self) :
            return len(self.items)

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
stack=list(s.split(','))

m,n = int(m),int(n)
#print(str(m) +"||"+str(stack)+"||"+str(o)+"||"+str(n))
if o == 'arrive':
    if  len(stack) < m :
        if str(n) in stack:
            print("car "+str(n)+" already in soi")
        else:
            print("car "+str(n)+" arrive! : Add Car "+str(n))
            stack.append(n)
    else :
         print("car "+str(n)+" cannot arrive : Soi Full ")
else :
    if '0' in stack  :
        print("car "+str(n)+" cannot depart : Soi Empty")
    elif str(n) not in stack:
        print("car "+str(n)+" cannot depart : Dont Have Car "+str(n))
    else:
        print("car "+str(n)+" depart ! : Car "+str(n)+" was remove")
        stack.remove(str(n))
        

stackTemp=[]
for i in  stack: 
    stackTemp.append(int(i))
    if int(i)==0:
        stackTemp.remove(0)
print(stackTemp)

