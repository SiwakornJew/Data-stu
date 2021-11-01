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
        
    def contentEquivalence(self,lst):
        if self.size != len(lst): return False
        temp1=[]
        temp2=[]
        for i in range(self.size):
            temp1.append(self.nodeAt(i).data)
            temp2.append(lst.nodeAt(i).data)
        temp1=self.sort(temp1)
        temp2=self.sort(temp2)
        for i in range(self.size):
                if temp1[i]!=temp2[i]:
                    return False
        return True
       

    def sort(self,lst):
        if not lst:
         return []
        return (self.sort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            self.sort([x for x in lst[1:] if x >= lst[0]]))
     


inputlist = input('List1,List2 : ').split(',')
list1 = LinkedList()
list2 = LinkedList()

for i in inputlist[0].split():
    list1.append(i)
for i in inputlist[1].split():
    list2.append(i)

print('List1 content Equivalence List2 :',list1.contentEquivalence(list2))
       



