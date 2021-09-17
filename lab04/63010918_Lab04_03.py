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

lit,hint =(input("Enter code,hint : ")).split(',')
Q=Queue()
decoad=ord(hint)-ord(lit[0])
for i in lit:
    Q.enQueue(chr(ord(i)+decoad))
    print(Q)
