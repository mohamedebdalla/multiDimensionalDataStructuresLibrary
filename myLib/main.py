import pytest
import sys
sys.path.append('C:/Users/Moe/338_finalProject')
# from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.Linear.SLL import SLL
from myLib.datastructures.Linear.DLL import DLL
from myLib.datastructures.Linear.CSLL import CSLL
from myLib.datastructures.Linear.CDLL import CDLL
from myLib.datastructures.Linear.QueueLL import QueueLL
from myLib.datastructures.Linear.StackLL import StackLL
from myLib.datastructures.nodes.DNode import DNode
from myLib.datastructures.nodes.SNode import SNode

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
    sll.Insert(SNode(1), 0)
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


def test_QueueLL_Enqueue():
    q = QueueLL()
    q.Enqueue(SNode(1))
    assert q.head.data == 1

def test_QueueLL_Dequeue():
    q = QueueLL()
    q.Enqueue(SNode(1))
    q.Enqueue(SNode(2))
    q.Dequeue()
    assert q.head.data == 2


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

