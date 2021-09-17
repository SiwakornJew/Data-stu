from collections import deque
from typing import List

class Queue:

    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items =List
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

inp = input('Enter Input : ').split(',')
Q= Queue()
L=[]
dequelist=[]
for i in inp :
    L =i.split()
    if L[0] =='E':
        Q.enQueue(L[1])
        print(str(Q).replace("\'",'').replace("[",'').replace("]",''))
    else :
        if Q.isEmpty():
            print("Empty")
        else:
            temp =str(Q).split(",")
            for i in range(len(temp)):
                if i == 0:
                    print(str(Q.getvalue(i))+" <- ",end="")
                    dequelist.append(Q.deQueue())
                    if Q.isEmpty():
                        print("Empty")
                    else:
                        print(str(Q).replace("\'",'').replace("[",'').replace("]",''))

if not dequelist:
    print("Empty : ",end='')
else:
    print(str(dequelist).replace("\'",'').replace("[",'').replace("]",'')+" : ",end='')
if Q.isEmpty():
    print("Empty")
else:
    print(str(Q).replace("\'",'').replace("[",'').replace("]",''))
