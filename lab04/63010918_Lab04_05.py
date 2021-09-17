from queue import Queue

class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items =Queue
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return int(len(self.items))
    def __str__(self) :
        return str(self.items)
    def getvalue(self,i):
        return self.items[i]
    def isFull(self) :
        return self.items.full()
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
    def __str__(self) :
        return str(self.items)

inp = input('Enter Input (Normal, Mirror) : ').split(" ")
normalList=Stack()
mirrorList=Stack()
iteamM=Queue()
x=''
comboM=0
comboN=0
fbome=0
inp[1]=''.join(reversed(inp[1]))
#print(inp[1])
for i in inp[1]: 
    mirrorList.push(i)
    if i == x :
        count+=1
    else :
        x=i
        count=1
    if count==3 :
        count=0
        mirrorList.pop() 
        mirrorList.pop()
        iteamM.enQueue(mirrorList.pop()) 
        comboM+=1
        if mirrorList.size()>1:
            if mirrorList.items[-2] == mirrorList.items[-1] :
                x=mirrorList.items[-1]
                count = 2
            else :
                x=mirrorList.items[-1]
                count = 1
        elif mirrorList.size()==1:
                x=mirrorList.items[-1]
                count = 1
x=''
for i in inp[0]: 
    normalList.push(i)
    if i == x:
        count+=1
    else :
        x=i
        count=1
    if count==3:
        count=0
        if not iteamM.isEmpty():
            p=iteamM.deQueue()
            if i==p:
                normalList.push(p)
                normalList.pop()
                normalList.pop()
                normalList.pop()
                fbome+=1
            else:
                normalList.pop()
                normalList.push(str(p))
                normalList.push(i)
            
        else :
            normalList.pop()
            normalList.pop()
            normalList.pop()
            comboN+=1
        if normalList.size()>1:
            if normalList.items[-2] == normalList.items[-1]:
                x=normalList.items [-1]
                count=2
            else:
                x=normalList.items[-1]
                count=1
        elif normalList.size()==1:
            x=normalList.items[-1]
            count=1

print("NORMAL :")
print(normalList.size())
if normalList.isEmpty():
    print("Empty")
else:
    S=''.join([str(i) for i in normalList.items])
    S=''.join(reversed(S))
    print(S)
print(str(comboN)+" Explosive(s) ! ! ! (NORMAL)")
if fbome != 0:
    print("Failed Interrupted "+str(fbome)+" Bomb(s) ")
print("------------MIRROR------------")
print(": RORRIM")
print(mirrorList.size())
if mirrorList.isEmpty():
    print("ytpmE")
else:
    S=''.join([str(i) for i in mirrorList.items])
    S=''.join(reversed(S))
    print(S)
S = ("(RORRIM) ! ! ! (s)evisolpxE "+str(comboM))
print(S)