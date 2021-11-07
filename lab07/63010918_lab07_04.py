
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
    def insert(self, data):
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
    def delete(self, node, data):
        if node is None:    # base case
            print("Error! Not Found DATA")
            return
        if node.data != data:   # not found
            if node.data > data:
                node.left = self.delete(node.left, data)  # not found left
            elif node.data < data:
                node.right = self.delete(node.right, data)  # not found right
        else:   # found !!!!

            if node.left is None:   # left None
                node = node.right
                return node
            elif node.right is None:  # right None
                node = node.left
                return node
            else:
                current = node.right
                while current.left is not None:
                    current = current.left

                node.data = current.data    # replace delete
                node.right = self.delete(node.right, current.data)  # permanent delete recursive.....

        return node
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


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
T = BST()
inp = input('Enter Input : ').split(',')
#print(inp[1][2].split())
#print(inp[0][1:].split())
for i in range (len(inp)):
    if inp[i][0] == 'i':
        print("insert " + (inp[i][2:]))
        T.root=T.insert(int(inp[i][2:]))
        T.printTree(T.root)
    if inp[i][0] == 'd':
        print("delete " + (inp[i][2:]))
        T.root=T.delete(T.root,int(inp[i][2:]))
        T.printTree(T.root)
#for i in inp:
    #root = T.insert(i)
#T.printTree(root)
