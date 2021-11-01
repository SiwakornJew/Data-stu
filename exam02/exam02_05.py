class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p
    def cheakDup(self):
        temp= []
        if self.head == None : return
        p= self.head
        while p.next != None:
            temp.append(p.data)
            if p.next.data in temp:
                return True
            else:
                p =p.next
        return False
class Queue:
    def __init__(self):
        self.queue=LinkedList()

    def __str__(self):
        if self.isEmpty():
            return 'Empty Queue'
        s ='Queue data : '
        for i in range(len(self.queue)):
            s += str(self.queue.nodeAt(i).data)+' '
        return s

    def __len__(self):
        return len(self.queue)

    def enQueue(self,data):
        self.queue.append(data)

    def deQueue(self):
        return self.queue.removeHead()

    def isEmpty(self):
        return self.queue.isEmpty()
    def cheakDup(self):
        if self.queue.cheakDup() : return 'Duplicate'
        else : return 'NO Duplicate'
   
inputlst =input("Enter Input : ").split('/')
s=Queue()
for i in inputlst[0].split():
    s.enQueue(i)
for i in inputlst[1].split(','):
    #print(i[:1])
    if i[:1] == 'D' :
        s.deQueue()
    elif i[:1] =='E':
        s.enQueue(i[2:])
print(s.cheakDup())
    