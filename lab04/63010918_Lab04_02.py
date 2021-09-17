from typing import List
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

main=Queue()
cashier1=Queue()
cashier2=Queue()
cout1=0
cout2=0
lit =(input("Enter people : "))
for i in lit:main.enQueue(i)

for i in range(1,main.size()+1):
        d=main.deQueue()
        if i % 3 == 1 and i!= 1:
                cashier1.deQueue()
                cout1-=1
        if i % 2 == 0 and not cashier2.isEmpty() :
                cashier2.deQueue()
        if  cashier1.isFull and cout1 != 5:
                
                cashier1.enQueue(d)
                cout1+=1
        else:
                cashier2.enQueue(d)
                cout2+=1
        
        print(str(i)+' '+str(main)+' '+str(cashier1)+' '+str(cashier2))

