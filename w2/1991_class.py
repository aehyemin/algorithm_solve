import sys
input = sys.stdin.readline()

class Node:
    def __init__(self,root,left,right):
        self.root = root
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.nodes = {}
        self.root = 'A'

    def add_node(self, root, left, right):
        self.nodes[root] = Node(root, left, right)

    def preorder(self, node):
        if node == '.':
            return
        print(node, end='')
        self.preorder(self.nodes[node].left)
        self.preorder(self.nodes[node].right)
        
    def inorder(self, node):
       if node == '.':
            return
       self.inorder(self.nodes[node].left)
       print(node, end='')
       self.inorder(self.nodes[node].right)
        

    def postorder(self, node):
       if node == '.':
            return
       self.postorder(self.nodes[node].left)
       self.postorder(self.nodes[node].right)
       print(node, end='')

tree = Tree()
N = int(input())

for _ in range(N):
    root, left, right = input().split()
    tree.add_node(root, left, right)

tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)
print()
