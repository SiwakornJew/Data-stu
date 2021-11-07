class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
      
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.min =0
        self.max=0
        self.equal=[]
        self.count=0
    def insert(self, data,k):
        if data <= k:
            self.count+=1
        if self.root == None:
            self.root=Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left =Node(data)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right
    def getMax(self):
        node =self.root
        while node.right != None:
            node =node.right
        return node.data
    def getMin(self):
        node =self.root
        while node.left != None:
            node = node.left
        return node.data

    def returnCount(self):
        return self.count

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = input('Enter Input : ').split('/')
k=int(inp[1])
for i in inp[0].split():
    T.root = T.insert(int(i),k)
T.printTree(T.root)
print("--------------------------------------------------")
print(T.returnCount())
