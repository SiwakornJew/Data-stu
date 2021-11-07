
class Node:

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    
    def __init__(self):
        self.root = None

    def insert(self,data):
        s = ""
        if self.root == None:
            self.root = Node(data)
            print(s+'*')
            return self.root
        node =self.root
        while True:
            if int(data) <int(node.data):
                s+='L'
                if node.left == None:
                    node.left = Node(data)
                    break
                node = node.left
            else:
                s+='R'
                if node.right == None:
                    node.right = Node(data)
                    break
                node =node.right
        print(s+'*')
        return self.root



T = BST()
inp = input('Enter Input : ').split()
for i in inp:
    T.insert(i)
    
