class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
      
    def __str__(self):
        return str(self.data)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

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

    def pre_order(self, node):
        if node == None:
            return ''
        s = str(node.data)\
            + self.pre_order(node.left)\
                + self.pre_order(node.right)
        return s

    def in_order(self, node):
        if node == None:
            return ''
        s = self.in_order(node.left)\
             + str(node.data)\
                 + self.in_order(node.right)
        if node.left is not None and node.right is not None:
            s = '(' + s + ')'
        return s

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
inp = list(input("Enter Postfix : "))
T =BST()
S =Stack()
for chr in inp:
    if chr in'+-*/':
        op1 = S.pop()
        op2 = S.pop()
        S.push(Node(chr,op2,op1))
    else:
        S.push(Node(chr))
    
print("Tree :")
T_root = S.pop()
T.printTree(T_root)
print("--------------------------------------------------")
print("Infix :",T.in_order(T_root))
print("Prefix :",T.pre_order(T_root))

