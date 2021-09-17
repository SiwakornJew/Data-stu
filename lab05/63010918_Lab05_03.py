class DoublyLinkedList : #Circular Doubly linked list with dummy
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.dummy = self.Node(None,None,None)
            self.dummy.next = self.dummy.prev = self.dummy
            self.size = 0
            
    def __str__(self):
        s = ''
        p = self.dummy.next
        for i in range(len(self)-1) :
            s += str(p.data) + ' '
            p = p.next
        if str(p.data) != "None":
            s += str(p.data)    
        return s  

    def __len__(self) :
        return self.size
        
    def isEmpty(self) :
        return self.size == 0
    
    def indexOf(self,data) :
        q = self.dummy.next
       
        for i in range(len(self)) :
            if int(q.data) == int(data) :
                return i
            q = q.next
        return -1
    
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    def str_reverse(self):
        s = ''
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)-1) :
            s += str(p.data) + ' '
            p = p.prev
        if str(p.data) != "None":
            s += str(p.data)
        return s 
    def add_before(self,q,data) :
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1
        
    def append(self,data) :
        self.add_before(self.nodeAt(len(self)),data)
    def mergeLists(self,p,q):
        q = self.nodeAt(len(self)-1)
        for i in range(len(q)-1) :
            print(q.data)
            q = q.prev
  
    def removeNode(self,q) :   
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1
    def delete(self,i) :
        self.removeNode(self.nodeAt(i))
 

lit =input("Enter Input (L1,L2) : ").split()
s1 =str(lit[0]).split("->")
s2 =str(lit[1]).split("->")
linkA=DoublyLinkedList()
linkB=DoublyLinkedList()
for i in s1:linkA.append(i)
for i in s2:linkB.append(i)
print(f"L1    : {linkA}")
print(f"L2    : {linkB}")
print("Merge : "+str(linkA)+" "+linkB.str_reverse())

