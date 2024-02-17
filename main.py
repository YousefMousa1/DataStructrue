# username - Yousefmousa1
# id1      - 323993543
# name1    - yousef
# id2      - 323033134
# name2    - Miral
"""A class represnting a node in an AVL tree"""
import unittest

class AVLNode(object):
    """Constructor, you are allowed to add more fields.
    @type key: int or None
    @type value: any
    @param value: data of your node
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0



    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        if self.height is None:
            return -1
        return self.height

    """sets left child
    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node
        return None

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key
        return None

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value
        return None

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h
        return None
    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.height != -1


    def calcbf(self):
        return self.left.get_height() - self.right.get_height()

"""
A class implementing the ADT Dictionary, using an AVL tree.
"""





class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = AVLNode(None, None)

    # add your fields here
    def create_real_node(self, key, value):
        Node = AVLNode(key, value)
        Node.set_height(0)
        Node.set_left(AVLNode(None, None))  # stands for Virtual Node
        Node.set_right(AVLNode(None, None))  # stands for Virtual Node
        Node.set_parent(None)
        return Node

    def update_height(self, node):
        if node is not None and node.is_real_node():
            left_height = node.get_left().get_height()
            right_height = node.get_right().get_height()
            node.set_height(max(left_height, right_height) + 1)


    """searches for a AVLNode in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: the AVLNode corresponding to key or None if key is not found.
    """

    def search(self, key):
        if self.root is None or self.root.get_height() == -1: #root is a virtual node or not existent
            return None
        curr = self.root
        while curr is not None and curr.get_height() != -1: #if curr is not a virtual node nor None
            if curr.key == key:
                return curr
            elif curr.key < key:
                curr = curr.left
            elif curr.key > key:
                curr = curr.right
        return curr

    def tree_position(self, key):
        if not self.root.is_real_node():
            return None
        curr = self.root
        while not curr.is_real_node():
            if key < curr.get_key():
                if curr.get_left().is_real_node():
                    self.update_height(curr)
                    curr = curr.get_left()
                else:
                    break
            elif key > curr.get_key():
                if curr.get_right().is_real_node():
                    self.update_height(curr)
                    curr = curr.get_right()
                else:
                    break
        return curr



    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def right_rotation(self, z):
        sub_root = z.get_parent()
        y = z.get_left()
        t3 = y.get_right()
        y.right = z
        z.parent = y
        z.left = t3
        if t3 is not None: t3.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(z.get_left().get_height(), z.get_right().get_height())
        y.height = 1 + max(y.get_left().get_height(), y.get_right().get_height())



    def left_rotation(self,z):
        sub_root = z.get_parent()
        y = z.get_right()
        t2 = y.get_left()
        y.left = z
        z.parent = y
        z.right = t2
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(z.get_left().get_height(), z.get_right().get_height())
        y.height = 1 + max(y.get_left().get_height(), y.get_right().get_height())

    def insert_BST(self, key, val):
        inserted = self.create_real_node(key, val)
        curr = self.root
        if curr is None or not curr.is_real_node():
            self.root = inserted
            return inserted

        while curr.get_key() is not None:
            if inserted.get_key() < curr.get_key():
                if curr.get_left().is_real_node():
                    curr = curr.get_left()
                else:
                    break
            elif inserted.get_key() > curr.get_key():
                if curr.get_right().is_real_node():
                    curr = curr.get_right()
                else:
                    break

        if curr.get_key() > inserted.get_key():
            curr.set_left(inserted)

        if curr.get_key() < inserted.get_key():
            curr.set_right(inserted)
        inserted.set_parent(curr)
        self.update_height(curr)
        self.height_fix(inserted)



        return inserted


    def height_fix(self, node):
        while node is not None:
            self.update_height(node)
            node = node.get_parent()




    def insert(self, key, val):
        if not self.root.is_real_node():
            self.insert_BST(key, val)
            h_changed = False
            parent = None

        else:
            old_height = self.tree_position(key).get_height()
            parent = self.insert_BST(key, val).get_parent()
            new_height = self.tree_position(key).get_height()
            h_changed = (new_height != old_height)
        cnt = 0
        while parent is not None:
            bf = parent.calcbf()
            if abs(bf) < 2 and not h_changed:
                return cnt
            elif abs(bf) < 2 and h_changed:
                cnt += 1
                parent = parent.get_parent()
            elif abs(bf) == 2:
                cnt += self.rotations_insert(parent)
                return cnt
        return cnt


    def rotations_insert(self, node):
        if node.calcbf() == -2:
            if node.get_right().calcbf() == -1: #case 1
                self.left_rotation(node)
                return 1
            if node.get_right().calcbf() == 1:
                self.right_rotation(node)
                self.left_rotation(node)
                return 2
        if node.calcbf() == 2:
            if node.get_left().calcbf() == -1: #case 2
                self.left_rotation(node)
                self.right_rotation(node)
                return 2
            if node.get_left().calcbf() == 1:
                self.right_rotation(node)
                return 1


    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


    def successor(self, node):
        current = node.right
        while current.left is not None:
            current = current.left
        return current



    def delete_BST(self, node):
        if node.left is None and node.right is None:
            if(node.parent.key > node.key):
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left is not None and node.right is None:
            node.left.parent = node.parent
            node.parent.left = node.left
        elif node.right is not None and node.left is None:
            node.right.parent = node.parent
            node.parent.right = node.right
        else:
            successor = self.successor(node)
            node.key = successor.key
            self.delete(successor)
    def delete(self, node):
        cnt =0
        self.delete_BST(node)
        parent = node.parent
        while parent is not None:
            bf = parent.calcbf()
            if abs(bf) < 2 and parent.get_height() == parent.get_oldheight():
                return cnt
            elif abs(bf) < 2 and parent.get_height() != parent.get_oldheight():
                cnt += 1
                parent = parent.get_parent()
            elif abs(bf) == 2:
                cnt += self.rotations_delete(parent)
                return cnt
        return cnt

    def rotations_delete(self, node):
        node_bf = node.calcbf
        node_right_bf = node.get_right_bf()
        node_left_bf = node.get_left_bf()
        if node_bf == -2:
            if node.get_right().calcbf() == -1 or node_right_bf == 0 : #case 1
                self.left_rotation(node)
                return 1
            if node_right_bf == 1:
                self.right_rotation(node)
                self.left_rotation(node)
                return 2
        if node.bf == 2:
            if node_left_bf == -1: #case 2
                self.left_rotation(node)
                self.right_rotation(node)
                return 2
            if node_left_bf == 1 or node_right_bf == 0:
                self.right_rotation(node)
                return 1
    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return -1

    """splits the dictionary at the i'th index

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        return None

    """joins self with key and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree2, key, val):
        return None

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root

def print_avl_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left or root.right:
            if root.left:

                print_avl_tree(root.left, level + 1, "L--- ")
            if root.right:

                print_avl_tree(root.right, level + 1, "R--- " )
def insert_and_print(avl_tree, key, value):
    print(f"Inserting node ({key}, {value}) into the AVL tree:")
    avl_tree.insert_BST(key, value)

    print("\n")

def main():
    avl_tree = AVLTree()

    # Insert nodes
    insert_and_print(avl_tree, 50, 'A')
    insert_and_print(avl_tree, 30, 'B')
    insert_and_print(avl_tree, 90, 'C')
    insert_and_print(avl_tree, 15, 'D')
    insert_and_print(avl_tree, 10, 'E')
    insert_and_print(avl_tree, 3, 'F')
    insert_and_print(avl_tree, 2, 'H')




   

    # Inorder traversal after insertion
    print_avl_tree(avl_tree.get_root())
    print(avl_tree.get_root().get_height())

if __name__ == "__main__":
    main()
