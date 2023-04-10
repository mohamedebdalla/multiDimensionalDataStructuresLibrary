from BST import BST
from TNode import TNode

class AVL(BST):
    def __init__(self, root=None):
        super().__init__(root)

    def insert(self, val):
        super().insert(val)
        self._balance(self.root)

    def insert_node(self, node):
        super().insert_node(node)
        self._balance(self.root)

    def delete(self, val):
        super().delete(val)
        self._balance(self.root)

    def _height(self, node):
        if node is None:
            return -1
        else:
            return node.get_height()

    def _rotate_left(self, node):
        right_child = node.get_right()
        node.set_right(right_child.get_left())
        right_child.set_left(node)
        node.set_height(max(self._height(node.get_left()), self._height(node.get_right())) + 1)
        right_child.set_height(max(self._height(right_child.get_left()), self._height(right_child.get_right())) + 1)
        return right_child

    def _rotate_right(self, node):
        left_child = node.get_left()
        node.set_left(left_child.get_right())
        left_child.set_right(node)
        node.set_height(max(self._height(node.get_left()), self._height(node.get_right())) + 1)
        left_child.set_height(max(self._height(left_child.get_left()), self._height(left_child.get_right())) + 1)
        return left_child

    def _rotate_left_right(self, node):
        node.set_left(self._rotate_left(node.get_left()))
        return self._rotate_right(node)

    def _rotate_right_left(self, node):
        node.set_right(self._rotate_right(node.get_right()))
        return self._rotate_left(node)

    def _balance(self, node):
        if node is None:
            return
        if self._height(node.get_left()) - self._height(node.get_right()) > 1:
            if self._height(node.get_left().get_left()) >= self._height(node.get_left().get_right()):
                node = self._rotate_right(node)
            else:
                node = self._rotate_left_right(node)
        elif self._height(node.get_right()) - self._height(node.get_left()) > 1:
            if self._height(node.get_right().get_right()) >= self._height(node.get_right().get_left()):
                node = self._rotate_left(node)
            else:
                node = self._rotate_right_left(node)
        node.set_height(max(self._height(node.get_left()), self._height(node.get_right())) + 1)
        if node.get_parent() is not None:
            self._balance(node.get_parent())

    def set_root(self, root):
        super().set_root(root)
        self._balance(self.root)

    def __init__(self, val=None):
        if val is not None:
            super().__init__(TNode(val))
        else:
            super().__init__()

    def __init__(self, obj):
        if obj.get_left() is not None or obj.get_right() is not None:
            super().__init__()
            nodes = [obj]
            while nodes:
                next_nodes = []
                for node in nodes:
                    self.insert_node(node)
                    if node.get_left():
                        next_nodes.append(node.get_left())
                    if node.get_right():
                        next_nodes.append(node.get_right())
                nodes = next_nodes
        else:
            super().__init__(obj)

    def set_root(self, root):
        super().set_root(root)
        self._balance(self.root)
