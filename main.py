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
        self.oldheight = -1
        self.bf = 0


    def get_bf(self):
        return self.bf
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
        if self.key == None:
         return -1
        return self.height;

    def get_oldeight(self):
        if self.key == None:
         return -1
        return self.oldheight;

    """sets left child
    
    

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node;
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node;
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node;
        return None

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key;
        return None

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value;
        return None

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h
        return None
    def set_oldheight(self, oh):
        self.old_height = oh
    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        if (self.height == -1):
            return False
        return True


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None

    # add your fields here

    def CalcBF(self):
        return  self.left.get_height() - self.right.get_height()




    def Tree_position(self,x, k):
        while x is not None:
            y = x;
            if x.key == k:
                return x
            elif x.key > k:
                x = x.left
            elif x.key < k:
                x = x.right
            return y
    """searches for a AVLNode in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: the AVLNode corresponding to key or None if key is not found.
    """

    def search(self, key):
        curr = self.Tree_position(self.root, key)
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
    def update_height(self, node):
        if node is None:
            return 0
        node.height = 1 + max(node.left.height, node.right.height)

    def right_rotation(self, node):
        A = node.left


        node.left = A.right
        A.right.set_parent(node)
        A.right = node
        A.parent =  node.parent
        if A.key > A.parent.key:
            A.parent.right = A
        else:
            A.parent.left = A

        node.parent = A

        #update heights
        node.height = 1 + max(node.left.get_height, node.right.get_height)
        A.height =  1 + max(A.left.get_height(), A.right.get_height())

    def left_rotation(self, node):
        A = node.right

        node.right = A.left
        A.left.set_parent(node)
        A.left = node
        A.parent = node.parent
        if A.key > A.parent.key:
            A.parent.right = A
        else:
            A.parent.left = A

        node.parent = A

        # update heights
        node.height = 1 + max(node.left.get_height, node.right.get_height)
        A.height = 1 + max(A.left.get_height(), A.right.get_height())

    def insert(self, key, val):
        cnt = 0
        leaf  = self.insert_rec(self.root, key, val, None)
        parent = leaf.parent
        while parent is not None:
            bf = parent.CalcBF()
            if abs(bf) < 2 and parent.get_height() == parent.get_oldheight():
                return cnt
            elif abs(bf) < 2 and parent.get_height() != parent.get_oldheight():
                cnt += 1
                parent = parent.get_parent()
            elif abs(bf) == 2:
                cnt += self.rotations_insert(parent)
                return cnt
        return cnt
    def insert_rec(self, node, key, val, parent):
        if node is None:
            node = AVLNode(key, val)
            node.set_parent(parent)
            return node
        if key < node.key:
            node.left = self.insert_rec(node.left, key, val, node)
        elif key > node.key:
            node.right = self.insert_rec(node.right, key, val,node)

        node.set_oldheight(node, node.get_height())
        self.update_height(node)
        node.height = 1 + max(node.left.get_height(), node.right.get_height())

    def rotations_insert(self, node):
        if node.bf == -2:
            if node.get_right().get_bf() == -1: #case 1
                self.left_rotation(node)
                return 1
            if node.get_right().get_bf() == 1:
                self.right_rotation(node)
                self.left_rotation(node)
                return 2
        if node.bf == 2:
            if node.get_left().get_bf() == -1: #case 2
                self.left_rotation(node)
                self.right_rotation(node)
                return 2
            if node.get_left().get_bf() == 1:
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
            bf = parent.CalcBF()
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
        if node.bf == -2:
            if node.get_right().get_bf() == -1 or node.get_right().get_bf() == 0 : #case 1
                self.left_rotation(node)
                return 1
            if node.get_right().get_bf() == 1:
                self.right_rotation(node)
                self.left_rotation(node)
                return 2
        if node.bf == 2:
            if node.get_left().get_bf() == -1: #case 2
                self.left_rotation(node)
                self.right_rotation(node)
                return 2
            if node.get_left().get_bf() == 1 or node.get_right().get_bf() == 0:
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
