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
        s = 'linked list : '
        p = self.dummy.next
        for i in range(len(self)-1) :
            s += str(p.data) + '->'
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
        s = 'reverse : '
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)-1) :
            s += str(p.data) + '->'
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
  
    def removeNode(self,q) :   
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1
     
        
    def delete(self,i) :
        self.removeNode(self.nodeAt(i))


lit =input("Enter Input : ")
lit=lit.replace(", ",",")
lit=lit.split(',')
dLinked=DoublyLinkedList()

for i in lit:
     a=i.split()
     if 'A' == a[0]:
      dLinked.append(a[1])
     elif 'Ab' == a[0]:
      dLinked.add_before(dLinked.nodeAt(0),a[1])
     elif 'I' == a[0]:
        index,data=a[1].split(':')
        if int(index)>=0 and int(index)<=len(dLinked):
            print("index = "+index+" and data = "+data)
            dLinked.add_before(dLinked.nodeAt(int(index)),int(data))
        else :
            print('Data cannot be added')
     else :
        if dLinked.isIn(a[1]):
            for i in range(len(dLinked)): 
                if int(dLinked.nodeAt(i).data) == int(a[1]):
                    print(f"removed : {dLinked.nodeAt(i).data} from index : {i}")
                    dLinked.delete(int(i))

                    break
            
        else :
            print("Not Found!")

     print(dLinked)
     print(dLinked.str_reverse())


