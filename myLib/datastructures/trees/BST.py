# import sys
# sys.path.append('/path/to/parent/folder') # replace with the actual path to the parent folder
# from data_structures.tnode import TNode

# from nodes.TNode import TNode 
# from sys import path
# path.append('myLib\datastructures\nodes\TNode.py')
# from datastructures.nodes.TNode import TNode


class BST:
    def __init__(self, root=None):
        self.root = root
        self.values = []
    
    def get_root(self):
        return self.root
    
    def set_root(self, root):
        self.root = root
   
    def insert(self, val):
        node = TNode(val, 0, None, None, None)  # create a new TNode instance with default values
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if val < current.get_data():
                    if current.get_left() is None:
                        current.set_left(node)
                        node.set_parent(current)
                        break
                    else:
                        current = current.get_left()
                else:
                    if current.get_right() is None:
                        current.set_right(node)
                        node.set_parent(current)
                        break
                    else:
                        current = current.get_right()
        self.values.append(val)
    
    def delete(self, val):
        if self.root is None:
            print("Value not found in tree")
            return
        current = self.root
        parent = None
        while current is not None:
            if val == current.get_data():
                if current.get_left() is None and current.get_right() is None:
                    if parent is None:
                        self.root = None
                    elif parent.get_left() == current:
                        parent.set_left(None)
                    else:
                        parent.set_right(None)
                elif current.get_left() is None:
                    if parent is None:
                        self.root = current.get_right()
                    elif parent.get_left() == current:
                        parent.set_left(current.get_right())
                    else:
                        parent.set_right(current.get_right())
                elif current.get_right() is None:
                    if parent is None:
                        self.root = current.get_left()
                    elif parent.get_left() == current:
                        parent.set_left(current.get_left())
                    else:
                        parent.set_right(current.get_left())
                else:
                    successor = current.get_right()
                    while successor.get_left() is not None:
                        successor = successor.get_left()
                    current.set_data(successor.get_data())
                    current = successor
                    continue
                print(f"Deleted {val} from tree")
                return
            elif val < current.get_data():
                parent = current
                current = current.get_left()
            else:
                parent = current
                current = current.get_right()
        print("Value not found in tree")


    def search(self, val):
        current = self.root
        while current is not None:
            if val == current.get_data():
                return current
            elif val < current.get_data():
                current = current.get_left()
            else:
                current = current.get_right()
        return None
    
    def _print_in_order(self, node):
        if node is not None:
            self._print_in_order(node.get_left())
            print(node.get_data(), end=' ')
            self._print_in_order(node.get_right())
    
    def printInOrder(self):
        self._print_in_order(self.root)
        print()
    
    def printBF(self):
        nodes = [self.root]
        while nodes:
            next_nodes = []
            for node in nodes:
                print(node.get_data(), end=' ')
                if node.get_left():
                    next_nodes.append(node.get_left())
                if node.get_right():
                    next_nodes.append(node.get_right())
            print()
            nodes = next_nodes

class TNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
        self.balance = 0
    
    def __init__(self, data, balance, parent, left, right):
        self.data = data
        self.balance = balance
        self.parent = parent
        self.left = left
        self.right = right
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_left(self, node):
        self.left = node
    
    def get_left(self):
        return self.left
    
    def set_right(self, node):
        self.right = node
    
    def get_right(self):
        return self.right
    
    def set_parent(self, node):
        self.parent = node
    
    def get_parent(self):
        return self.parent
    
    def set_balance(self, balance):
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def print_node(self):
        print(f"Data: {self.data}, Balance: {self.balance}")
    
    def __str__(self):
        return str(self.data)