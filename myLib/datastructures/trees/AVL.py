# from BST import BST


# class TNode:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.balance = 0
    
#     def __init__(self, data, balance, parent, left, right):
#         self.data = data
#         self.balance = balance
#         self.parent = parent
#         self.left = left
#         self.right = right
    
#     def set_data(self, data):
#         self.data = data
    
#     def get_data(self):
#         return self.data
    
#     def set_left(self, node):
#         self.left = node
    
#     def get_left(self):
#         return self.left
    
#     def set_right(self, node):
#         self.right = node
    
#     def get_right(self):
#         return self.right
    
#     def set_parent(self, node):
#         self.parent = node
    
#     def get_parent(self):
#         return self.parent
    
#     def set_balance(self, balance):
#         self.balance = balance
    
#     def get_balance(self):
#         return self.balance
    
#     def print_node(self):
#         print(f"Data: {self.data}, Balance: {self.balance}")
    
#     def __str__(self):
#         return str(self.data)

# class AVL(BST):
#     def __init__(self, root=None):
#         super().__init__(root)

#     def insert(self, val):
#         super().insert(val)
#         self._balance(self.root)

#     def insert_node(self, node):
#         super().insert_node(node)
#         self._balance(self.root)

#     def delete(self, val):
#         super().delete(val)
#         self._balance(self.root)

#     def _height(self, node):
#         if node is None:
#             return -1
#         else:
#             return node.get_height()

#     def _rotate_left(self, node):
#         right_child = node.get_right()
#         node.set_right(right_child.get_left())
#         right_child.set_left(node)
#         node.set_height(max(self._height(node.get_left()), self._height(node.get_right())) + 1)
#         right_child.set_height(max(self._height(right_child.get_left()), self._height(right_child.get_right())) + 1)
#         return right_child

#     def _rotate_right(self, node):
#         left_child = node.get_left()
#         node.set_left(left_child.get_right())
#         left_child.set_right(node)
#         node.set_height(max(self._height(node.get_left()), self._height(node.get_right())) + 1)
#         left_child.set_height(max(self._height(left_child.get_left()), self._height(left_child.get_right())) + 1)
#         return left_child

#     def _rotate_left_right(self, node):
#         node.set_left(self._rotate_left(node.get_left()))
#         return self._rotate_right(node)

#     def _rotate_right_left(self, node):
#         node.set_right(self._rotate_right(node.get_right()))
#         return self._rotate_left(node)

#     def _balance(self, node):
#         if node is None:
#             return
#         if self._height(node.get_left()) - self._height(node.get_right()) > 1:
#             if self._height(node.get_left().get_left()) >= self._height(node.get_left().get_right()):
#                 node = self._rotate_right(node)
#             else:
#                 node = self._rotate_left_right(node)
#         elif self._height(node.get_right()) - self._height(node.get_left()) > 1:
#             if self._height(node.get_right().get_right()) >= self._height(node.get_right().get_left()):
#                 node = self._rotate_left(node)
#             else:
#                 node = self._rotate_right_left(node)
#         node.set_height(max(self._height(node.get_left()), self._height(node.get_right())) + 1)
#         if node.get_parent() is not None:
#             self._balance(node.get_parent())

#     def set_root(self, root):
#         super().set_root(root)
#         self._balance(self.root)

#     def __init__(self, val=None):
#         if val is not None:
#             super().__init__(TNode(val))
#         else:
#             super().__init__()

#     def __init__(self, obj):
#         if obj.get_left() is not None or obj.get_right() is not None:
#             super().__init__()
#             nodes = [obj]
#             while nodes:
#                 next_nodes = []
#                 for node in nodes:
#                     self.insert_node(node)
#                     if node.get_left():
#                         next_nodes.append(node.get_left())
#                     if node.get_right():
#                         next_nodes.append(node.get_right())
#                 nodes = next_nodes
#         else:
#             super().__init__(obj)

#     def set_root(self, root):
#         super().set_root(root)
#         self._balance(self.root)

# from myLib.datastructures.nodes import TNode
# from myLib.datastructures.trees import BST
# from BST import BST

# class TNode:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.balance = 0
    
#     def __init__(self, data, balance, parent, left, right):
#         self.data = data
#         self.balance = balance
#         self.parent = parent
#         self.left = left
#         self.right = right
    
#     def set_data(self, data):
#         self.data = data
    
#     def get_data(self):
#         return self.data
    
#     def set_left(self, node):
#         self.left = node
    
#     def get_left(self):
#         return self.left
    
#     def set_right(self, node):
#         self.right = node
    
#     def get_right(self):
#         return self.right
    
#     def set_parent(self, node):
#         self.parent = node
    
#     def get_parent(self):
#         return self.parent
    
#     def set_balance(self, balance):
#         self.balance = balance
    
#     def get_balance(self):
#         return self.balance
    
#     def print_node(self):
#         print(f"Data: {self.data}, Balance: {self.balance}")
    
#     def __str__(self):
#         return str(self.data)
    
# # class AVL(BST):
# #     def __init__(self, data=None):
# #         super().__init__(data)
# #         self.root = None if data is None else TNode(data)

# #     def __init__(self, obj):
# #         self.root = obj
# #         if obj.left is not None or obj.right is not None:
# #             new_root = self.copy_tree(obj)
# #             self.root = new_root
# #             self.balance_tree(new_root)

# class AVL(BST):
#     def __init__(self, obj=None):
#         super().__init__()
#         if obj is None:
#             self.root = None
#         else:
#             self.root = obj
#             if obj.left is not None or obj.right is not None:
#                 new_root = self.copy_tree(obj)
#                 self.root = new_root
#                 self.balance_tree(new_root)


#     def copy_tree(self, node):
#         if node is None:
#             return None
#         new_node = TNode(node.data, None, None, None, 0)
#         new_node.left = self.copy_tree(node.left)
#         new_node.right = self.copy_tree(node.right)
#         return new_node

#     def balance_tree(self, node):
#         if node is None:
#             return
#         balance = self.get_balance(node)
#         if balance > 1:
#             if self.get_balance(node.left) >= 0:
#                 node = self.rotate_right(node)
#             else:
#                 node.left = self.rotate_left(node.left)
#                 node = self.rotate_right(node)
#         elif balance < -1:
#             if self.get_balance(node.right) <= 0:
#                 node = self.rotate_left(node)
#             else:
#                 node.right = self.rotate_right(node.right)
#                 node = self.rotate_left(node)
#         self.balance_tree(node.left)
#         self.balance_tree(node.right)

#     def get_balance(self, node):
#         if node is None:
#             return 0
#         return self.get_height(node.left) - self.get_height(node.right)

#     def get_height(self, node):
#         if node is None:
#             return -1
#         return 1 + max(self.get_height(node.left), self.get_height(node.right))

#     def rotate_right(self, node):
#         new_root = node.left
#         node.left = new_root.right
#         new_root.right = node
#         self.update_height(node)
#         self.update_height(new_root)
#         return new_root

#     def rotate_left(self, node):
#         new_root = node.right
#         node.right = new_root.left
#         new_root.left = node
#         self.update_height(node)
#         self.update_height(new_root)
#         return new_root

#     def update_height(self, node):
#         node.balance = self.get_height(node.left) - self.get_height(node.right)

#     def get_root(self):
#         return self.root

#     def set_root(self, node):
#         self.root = node
#         if node.left is not None or node.right is not None:
#             new_root = self.copy_tree(node)
#             self.root = new_root
#             self.balance_tree(new_root)

#     def insert(self, val):
#         if self.root is None:
#             self.root = TNode(val, None, None, None, 0)
#             return
#         super().insert(val)
#         self.balance_tree(self.root)

#     def insert(self, new_node):
#         if self.root is None:
#             self.root = new_node
#             return
#         super().insert(new_node)
#         self.balance_tree(self.root)

#     def delete(self, val):
#         super().delete(val)
#         self.balance_tree(self.root)

#     def search(self, val):
#         return super().search(val)

#     def print_in_order(self):
#         super().print_in_order()

#     def print_bf(self):
#         super().print_bf()


from BST import BST 
from myLib.datastructures.nodes.TNode import TNode

class AVL(BST):
    def __init__(self, obj=None):
        super().__init__()
        self.root = self._copy_tree(obj) if obj and (obj.left or obj.right) else None

    def _copy_tree(self, node):
        if not node:
            return None
        new_node = TNode(node.data, None, None, None, 0)
        new_node.left = self._copy_tree(node.left)
        new_node.right = self._copy_tree(node.right)
        return new_node

    def _balance_tree(self, node):
        if not node:
            return
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)
        elif balance < -1:
            if self._get_balance(node.right) <= 0:
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
        self._balance_tree(node.left)
        self._balance_tree(node.right)

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node):
        if not node:
            return -1
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _update_height(self, node):
        node.balance = self._get_height(node.left) - self._get_height(node.right)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node
        if node and (node.left or node.right):
            self._balance_tree(self._root)

    def insert(self, val):
        if not self.root:
            self.root = TNode(val, None, None, None, 0)
            return
        super().insert(val)
        self._balance_tree(self.root)

    def insert_node(self, new_node):
        if not self.root:
            self.root = new_node
            return
        super().insert_node(new_node)
        self._balance_tree(self.root)

    def delete(self, val):
        super().delete(val)
        self._balance_tree(self.root)

    def search(self, val):
        return super().search(val)

    def print_in_order(self):
        super().print_in_order()

    def print_bf(self):
        super().print_bf()