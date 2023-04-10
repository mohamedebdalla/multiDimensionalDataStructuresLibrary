# from BST import BST

# # test the BST class
# print()
# print('Testing BST:')
# print()
# # create a BST object
# bst = BST()

# # insert some values
# print('Inserting values into tree...')
# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# bst.insert(20)
# bst.insert(40)
# bst.insert(60)
# bst.insert(80)

# print('Values added :', bst.values)

# # search for a node
# print('Searching for node with value 30...')
# node = bst.search(30)
# print("Node found:", node)

# # delete a node
# bst.delete(20)

# # print the tree in order
# print("In-order traversal:")
# bst.printInOrder()

# # print the tree breadth-first
# print("Breadth-first traversal:")
# bst.printBF()

from BST import BST
from AVL import AVL
from myLib.datastructures.nodes.TNode import TNode




# Test BST
print("Testing BST:")
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Test searching
print("Searching for 2:", bst.search(2))
print("Searching for 10:", bst.search(10))

# Test deletion
bst.delete(5)
print("After deleting 5:")
bst.print_tree()

# Test AVL
print("\nTesting AVL:")
avl = AVL()
avl.insert(5)
avl.insert(3)
avl.insert(7)
avl.insert(2)
avl.insert(4)
avl.insert(6)
avl.insert(8)

# Test searching
print("Searching for 2:", avl.search(2))
print("Searching for 10:", avl.search(10))

# Test deletion
avl.delete(5)
print("After deleting 5:")
avl.print_tree()

# Test creation from object
obj = TNode(5, TNode(3, TNode(2), TNode(4)), TNode(7, TNode(6), TNode(8)))
bst = BST(obj)
avl = AVL(obj)

print("BST from object:")
bst.print_tree()

print("AVL from object:")
avl.print_tree()
