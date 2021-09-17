class LinkedList :  #Singly linked list with dummy
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.dummy = self.Node(None,None)
            self.size = 0
            
    def __str__(self):
        s = 'link list : '
        p = self.dummy.next
        while p != None :
            s += str(p.data)
            if p.next != None:
                s += '->'
            p = p.next
        return s
          
    def __len__(self) :
        return self.size
            
    def isEmpty(self) :
        return self.size == 0
        
    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    def sizeof(self) :
        siz = 0
        p = self.dummy.next
        while p != None :
            siz+=1
            p = p.next
        if self.isEmpty():
             siz=0
        return siz        
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    
    def append(self,data) :
        return self.insertAfter(len(self),data)
    
    def insertAfter(self,i,data) :
        p = self.nodeAt(i-1)
        p.next = self.Node(data,p.next)
        self.size += 1
    
    def deleteAfter(self,i) :
        if self.size > 0 :
          p = self.nodeAt(i)
          p.next = p.next.next
          self.size -= 1
        
    def delete(self,i) :            #ลบข้อมูลที่ index นั้นเลย
        self.deleteAfter(i-1)   

    def removeData(self,data) :
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)


lit =input("Enter Input : ").split(',')
linked=LinkedList()
set =False
for i in  range(len(lit)):
    if i == 0:
     if lit[0]=='':
         set=True
     else :
        for y in lit[i].split(' '):
            linked.append(y)
     if lit[0]=='':
         print('List is empty')
     else :
        print(linked)
     continue
    index,data =lit[i].split(':')
    index=index.replace(" ",'')
    if int(index)>=0 and int(data)<=linked.sizeof():
     #print(str(i))   
     index,data =lit[i].split(':')
     index=index.replace(" ",'')
     print("index ="+index+" and data = "+data)
     linked.insertAfter(int(index),int(data))
     if not linked.isEmpty():
         print(linked)
    else :
       print('Data cannot be added')
       if not linked.isEmpty():
            print(linked)
    if linked.isEmpty():
        print('List is empty') 

