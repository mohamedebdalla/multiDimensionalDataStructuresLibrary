# # from BST import BST

# # # test the BST class
# # print()
# # print('Testing BST:')
# # print()
# # # create a BST object
# # bst = BST()

# # # insert some values
# # print('Inserting values into tree...')
# # bst.insert(50)
# # bst.insert(30)
# # bst.insert(70)
# # bst.insert(20)
# # bst.insert(40)
# # bst.insert(60)
# # bst.insert(80)

# # print('Values added :', bst.values)

# # # search for a node
# # print('Searching for node with value 30...')
# # node = bst.search(30)
# # print("Node found:", node)

# # # delete a node
# # bst.delete(20)

# # # print the tree in order
# # print("In-order traversal:")
# # bst.printInOrder()

# # # print the tree breadth-first
# # print("Breadth-first traversal:")
# # bst.printBF()

# from BST import BST
# from AVL import AVL, TNode
# # from TNode import TNode

# # Test BST
# print("Testing BST:")
# bst = BST()
# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(2)
# bst.insert(4)
# bst.insert(6)
# bst.insert(8)

# # Test searching
# print("Searching for 2:", bst.search(2))
# print("Searching for 10:", bst.search(10))

# # Test deletion
# bst.delete(5)
# print("After deleting 5:")
# bst.print_bf()

# # Test AVL
# print("\nTesting AVL:")
# avl = AVL()
# avl.insert(5)
# avl.insert(3)
# avl.insert(7)
# avl.insert(2)
# avl.insert(4)
# avl.insert(6)
# avl.insert(8)

# # Test searching
# print("Searching for 2:", avl.search(2))
# print("Searching for 10:", avl.search(10))

# # Test deletion
# avl.delete(5)
# print("After deleting 5:")
# avl.printBF()

# # Test creation from object
# obj = TNode(5, TNode(3, TNode(2), TNode(4)), TNode(7, TNode(6), TNode(8)))
# bst = BST(obj)
# avl = AVL(obj)

# print("BST from object:")
# bst.print_bf()

# print("AVL from object:")
# avl.print_bf()

from BST import BST

print()
print('Testing BST')
print()

# create a BST object
bst = BST()

# insert some nodes
bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(9)

# print the tree in order
print("In order traversal:")
bst.print_in_order()

# print the tree breadth-first
print("Breadth-first traversal:")
bst.print_bf()

# search for a node
node = bst.search(6)
print(f"Node found: {node.data}" if node else "Node not found")

# delete some nodes
bst.delete(2)
bst.delete(8)

# print the tree in order again
print("In order traversal after deleting 2 and 8:")
bst.print_in_order()

# print the tree breadth-first again
print("Breadth-first traversal after deleting 2 and 8:")
bst.print_bf()

# search for a deleted node
node = bst.search(8)
print(f"Node found: {node.data}" if node else "Node not found")


from AVL import AVL

print()
print('Testing AVL')
print()

# create an empty AVL tree
avl = AVL()

# insert values into the AVL tree
avl.insert(10)
avl.insert(5)
avl.insert(20)
avl.insert(3)
avl.insert(8)
avl.insert(15)
avl.insert(25)
avl.insert(1)
avl.insert(4)
avl.insert(6)
avl.insert(9)
avl.insert(13)
avl.insert(17)
avl.insert(22)
avl.insert(27)

# print the AVL tree in-order and breadth-first
print("In-order traversal:")
avl.print_in_order()
print("Breadth-first traversal:")
avl.print_bf()

# search for values in the AVL tree
print("Searching for values:")
print(avl.search(10).data)
print(avl.search(5).data)
print(avl.search(20).data)
print(avl.search(30))

# delete values from the AVL tree
avl.delete(8)
avl.delete(13)
avl.delete(22)

# print the AVL tree in-order and breadth-first
print("In-order traversal:")
avl.print_in_order()
print("Breadth-first traversal:")
avl.print_bf()