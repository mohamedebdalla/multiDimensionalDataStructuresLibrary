from  mylib.datastructures.Linear.DLL import DLL
from  mylib.datastructures.Linear.SLL import SLL
from  mylib.datastructures.Linear.CSLL import CSLL
from  mylib.datastructures.Linear.CDLL import CDLL
from  mylib.datastructures.Linear.QueueLL import QueueLL
from  mylib.datastructures.Linear.StackLL import StackLL
from  mylib.datastructures.nodes.DNode import DNode
from  mylib.datastructures.nodes.SNode import SNode
from  mylib.datastructures.nodes.TNode import TNode
from  mylib.datastructures.trees.BST import BST
from  mylib.datastructures.trees.AVL import AVL

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

print("================================================== Trees Datastructure testing complete.  ============================================")
print("\n")
print("======================================= Use 'pytest' to test the Linear Datastructure implementation.  ===============================")
print("\n")
"""
 LINEAR TESTS
"""

ssl = AVL()


# Testing SLL
def test_SLL_InsertHead():
    sll = SLL()
    sll.InsertHead(SNode(1))
    assert sll.head.data == 1

def test_SLL_InsertTail():
    sll = SLL()
    sll.InsertTail(SNode(1))
    assert sll.tail.data == 1


def test_SLL_Insert():
    sll = SLL()
    node = SNode(1)
    sll.Insert(node, 1)
    assert sll.head.data == 1

def test_SLL_SortedInsert():
    sll = SLL()
    sll.SortedInsert(SNode(3))
    sll.SortedInsert(SNode(1))
    sll.SortedInsert(SNode(2))
    assert sll.head.data == 1
    assert sll.tail.data == 3

def test_SLL_DeleteHead():
    sll = SLL()
    sll.InsertHead(SNode(1))
    sll.InsertHead(SNode(2))
    sll.DeleteHead()
    assert sll.head.data == 1

def test_SLL_DeleteTail():
    sll = SLL()
    sll.InsertHead(SNode(1))
    sll.InsertHead(SNode(2))
    sll.DeleteTail()
    assert sll.tail.data == 2

def test_SLL_Delete():
    sll = SLL()
    node1 = SNode(1)
    sll.InsertHead(node1)
    sll.InsertHead(SNode(2))
    sll.Delete(node1)
    assert sll.head.data == 2


# Testing DLL
def test_DLL_InsertHead():
    dll = DLL()
    dll.InsertHead(DNode(1))
    assert dll.head.data == 1

def test_DLL_InsertTail():
    dll = DLL()
    dll.InsertTail(DNode(1))
    assert dll.tail.data == 1

def test_DLL_Insert():
    dll = DLL()
    dll.Insert(DNode(1), 0)
    assert dll.head.data == 1

def test_DLL_SortedInsert():
    dll = DLL()
    dll.SortedInsert(DNode(3))
    dll.SortedInsert(DNode(1))
    dll.SortedInsert(DNode(2))
    assert dll.head.data == 1
    assert dll.tail.data == 3

def test_DLL_DeleteHead():
    dll = DLL()
    dll.InsertHead(DNode(1))
    dll.InsertHead(DNode(2))
    dll.DeleteHead()
    assert dll.head.data == 1

def test_DLL_DeleteTail():
    dll = DLL()
    dll.InsertHead(DNode(1))
    dll.InsertHead(DNode(2))
    dll.DeleteTail()
    assert dll.tail.data == 2

def test_DLL_Delete():
    dll = DLL()
    node1 = DNode(1)
    dll.InsertHead(node1)
    dll.InsertHead(DNode(2))
    dll.Delete(node1)
    assert dll.head.data == 2


# Testing CSLL
def test_CSLL_InsertHead():
    csll = CSLL()
    csll.InsertHead(SNode(1))
    assert csll.head.data == 1

def test_CSLL_InsertTail():
    csll = CSLL()
    csll.InsertTail(SNode(1))
    assert csll.tail.data == 1

def test_CSLL_Insert():
    csll = CSLL()
    csll.Insert(SNode(1), 0)
    assert csll.head.data == 1

def test_CSLL_SortedInsert():
    csll = CSLL()
    csll.SortedInsert(SNode(3))
    csll.SortedInsert(SNode(1))
    csll.SortedInsert(SNode(2))
    assert csll.head.data == 1
    assert csll.tail.data == 3

def test_CSLL_DeleteHead():
    csll = CSLL()
    csll.InsertHead(SNode(1))
    csll.InsertHead(SNode(2))
    csll.DeleteHead()
    assert csll.head.data == 1

def test_CSLL_DeleteTail():
    csll = CSLL()
    csll.InsertHead(SNode(1))
    csll.InsertHead(SNode(2))
    csll.DeleteTail()
    assert csll.tail.data == 2

def test_CSLL_Delete():
    csll = CSLL()
    node1 = SNode(1)
    csll.InsertHead(node1)
    csll.InsertHead(SNode(2))
    csll.Delete(node1)
    assert csll.head.data == 2

# Testing QueueLL

def test_QueueLL_Enqueue():
    q = QueueLL()
    q.enqueue(SNode(1))
    assert q.head.data == 1

def test_QueueLL_Dequeue():
    q = QueueLL()
    q.enqueue(SNode(1))
    q.enqueue(SNode(2))
    q.dequeue()
    assert q.head.data == 2


# Testing StackLL

def test_StackLL_push():
    stack = StackLL()
    stack.push(SNode(1))
    assert stack.peek() == 1

def test_StackLL_pop():
    stack = StackLL()
    stack.push(SNode(1))
    stack.push(SNode(2))
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_StackLL_peek():
    stack = StackLL()
    stack.push(SNode(1))
    assert stack.peek() == 1

def test_StackLL_isEmpty():
    stack = StackLL()
    assert stack.isEmpty() == True
    stack.push(SNode(1))
    assert stack.isEmpty() == False

# Testing CDLL
def test_CDLL_InsertHead():
    cdll = CDLL()
    cdll.InsertHead(DNode(1))
    assert cdll.head.data == 1

def test_CDLL_InsertTail():
    cdll = CDLL()
    cdll.InsertTail(DNode(1))
    assert cdll.tail.data == 1

def test_CDLL_Insert():
    cdll = CDLL()
    cdll.Insert(DNode(1), 0)
    assert cdll.head.data == 1

def test_CDLL_SortedInsert():
    cdll = CDLL()
    cdll.SortedInsert(DNode(3))
    cdll.SortedInsert(DNode(1))
    cdll.SortedInsert(DNode(2))
    assert cdll.head.data == 1
    assert cdll.tail.data == 3

def test_CDLL_DeleteHead():
    cdll = CDLL()
    cdll.InsertHead(DNode(1))
    cdll.InsertHead(DNode(2))
    cdll.DeleteHead()
    assert cdll.head.data == 1

def test_CDLL_DeleteTail():
    cdll = CDLL()
    cdll.InsertHead(DNode(1))
    cdll.InsertHead(DNode(2))
    cdll.DeleteTail()
    assert cdll.tail.data == 2

def test_CDLL_Delete():
    cdll = CDLL()
    node1 = DNode(1)
    cdll.InsertHead(node1)
    cdll.InsertHead(DNode(2))
    cdll.Delete(node1)
    assert cdll.head.data == 2
