''' 
Tree: Inorder Transversal

This challenge, you are required to implement inorder traversal of a tree.
Complete the  function in your editor below, which has  parameter: a pointer to the root of a binary tree.
It must print the values in the tree's inorder traversal as a single line of space-separated values.

Input Format
Our hidden tester code passes the root node of a binary tree to your $inOrder* function.

Constraints
1 <= nodes in the tree <= 500
       
Output Format
Print the tree's inorder traversal as a single line of space-separated values.
'''

# Hacker Rank Code
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

#End of HackerRank Code

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root, end = " ")
        inOrder(root.right)



#More Hackerrank Code 
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

inOrder(tree.root)