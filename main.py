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

        curr = self.root
        if curr is None or not curr.is_real_node():  # root is a virtual node or not existent
            return None
        while curr.is_real_node():  # if curr is not a virtual node nor None
            if curr.key == key:
                return curr
            elif curr.key < key:
                curr = curr.right
            elif curr.key > key:
                curr = curr.left
        if not curr.is_real_node():
            return None
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
        if z.right is None:
            z.right = AVLNode(None, None)
        if not t3.is_real_node:
            t3.parent = z
        y.parent = sub_root

        if not y.parent is None:
            if y.parent.key < y.key:
                y.parent.right = y
            elif y.parent.key > y.key:
                y.parent.left = y
        else:
            self.root = y
            sub_root = y

        self.update_height(z)
        self.update_height(y)
        while (sub_root is not None):
            self.update_height(sub_root)
            sub_root = sub_root.get_parent()

    def left_rotation(self, z):
        sub_root = z.get_parent()
        y = z.get_right()
        t2 = y.get_left()
        y.left = z
        z.parent = y
        z.right = t2
        if z.left is None:
            z.left = AVLNode(None, None)
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
            sub_root = y
        elif y.key > y.parent.key:
            y.parent.right = y
        elif y.key < y.parent.key:
            y.parent.left = y
        self.update_height(z)
        self.update_height(y)

        while(sub_root is not None):
            self.update_height(sub_root)
            sub_root = sub_root.get_parent()



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

        print("the insert cnt is: " , cnt)
        return cnt

    def rotations_insert(self, node):
        if node.calcbf() == -2:
            if node.get_right().calcbf() == -1:  # case 1
                self.left_rotation(node)
                return 1
            if node.get_right().calcbf() == 1:
                self.right_rotation(node.get_right())
                self.left_rotation(node)
                return 2
        if node.calcbf() == 2:
            if node.get_left().calcbf() == -1:  # case 2
                self.left_rotation(node.get_left())
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
        current = node
        while current.get_right().is_real_node():
            current = current.right
            while current.get_left().is_real_node():
                current = current.left
            break

        return current
    def delete_BST(self, node):
        parent = node.get_parent()
        if not node.get_left().is_real_node() and not node.get_right().is_real_node():
            if node.parent is None:
                self.root = None
                return
            if (node.parent.key > node.key):
                node.parent.left = AVLNode(None, None)
            else:
                node.parent.right = AVLNode(None, None)
            self.height_fix(node.parent)

        elif node.get_left().is_real_node() and not node.get_right().is_real_node():
            if node.parent is None:
                self.root = node.get_left()
                self.root.parent = None
            else:
                node.left.parent = node.parent
                if node.parent.key < node.key:
                    node.parent.right = node.left
                else:
                    node.parent.left = node.left

            self.height_fix(node.parent)

        elif node.get_right().is_real_node() and  not node.get_left().is_real_node():
            if node.parent is None:
                self.root = node.get_right()
                self.root.parent = None
            else:
                node.right.parent = node.parent
                if node.parent.key > node.key:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            self.height_fix(node.parent)

        else:
            prev_succ = self.successor(node).get_parent()
            succ = self.successor(node)
            if prev_succ is not node:
                self.swap(node, self.successor(node))
                self.height_fix(prev_succ)
            else:
                self.swap(node, self.successor(node))
                self.height_fix(succ)
        return parent


    def swap(self, node, succesor):
        #succesor.parent.left = AVLNode(None, None)
        if node.get_right() is succesor:
            succesor.parent = node.parent
            succesor.parent.right = succesor
            succesor.left = node.left
            succesor.left.parent = succesor.parent
        else:
            succesor.parent.left = succesor.right
            succesor.right.parent = succesor.parent
            succesor.parent = node.parent
            succesor.left = node.left
            succesor.right = node.right
            succesor.left.parent = succesor
            succesor.right.parent = succesor
            if self.root is node:
                self.root = succesor



    def delete(self, node):

        key = node.get_key()
        old_height = self.tree_position(key).get_height()
        parent = self.delete_BST(node)
        new_height = self.tree_position(key).get_height()
        h_changed = (new_height != old_height)
        cnt = 0
        parent_lst = []
        while parent is not None:
            bf = parent.calcbf()
            parent_lst.append(parent.get_parent())
            if abs(bf) < 2 and not h_changed:
                return cnt
            elif abs(bf) < 2 and h_changed:
                cnt += 1
                parent = parent.get_parent()
            elif abs(bf) == 2:

                cnt += self.rotations_delete(parent)
                parent = parent_lst[len(parent_lst) - 1]

        print("the delete cnt is: " , cnt)
        return cnt

    def rotations_delete(self, node):
        node_bf = node.calcbf()
        if node.get_right().is_real_node():
            node_right_bf = node.get_right().calcbf()
        node_left_bf = node.get_left().calcbf()
        if node_bf == -2:
            if node.get_right().calcbf() == -1 or node_right_bf == 0:  # case 1
                self.left_rotation(node)
                return 1
            if node_right_bf == 1:
                self.right_rotation(node.get_right())
                self.left_rotation(node)
                return 2
        if node.calcbf() == 2:
            if node_left_bf == -1:  # case 2
                self.left_rotation(node.get_left())
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
                print_avl_tree(root.right, level + 1, "R--- ")


def insert_and_print(avl_tree, key, value):
    print(f"Inserting node ({key}, {value}) into the AVL tree:")
    avl_tree.insert(key, value)

    print("\n")

def main():
    avl_tree = AVLTree()

    avl_tree.insert(15, "15")
    avl_tree.insert(8, "8")
    avl_tree.insert(22, "22")
    avl_tree.insert(4, "4")
    avl_tree.insert(20, "20")
    avl_tree.insert(11, "11")
    avl_tree.insert(24, "24")
    avl_tree.insert(2, "2")
    avl_tree.insert(18, "18")
    avl_tree.insert(12, "12")
    avl_tree.insert(9, "9")
    avl_tree.insert(13, "13")
    print_avl_tree(avl_tree.get_root())
    ans = avl_tree.delete(avl_tree.search(11))
    print_avl_tree(avl_tree.get_root())



if __name__ == "__main__":
    main()

        # Check that the node has been deleted and the successor node has taken its place
#self.assertIsNone(avl_tree.search(24))
        #self.assertEqual(avl_tree.root.get_value(), "11")
        #self.assertEqual(avl_tree.root.get_left().get_value(), "8")
        #self.assertEqual(avl_tree.root.get_right().get_right().get_value(), "20")
class TestAVLTree(unittest.TestCase):
    def test_avl_delete_leaf_node(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(5, "five")
        avl_tree.insert(3, "three")
        avl_tree.insert(7, "seven")

        # Delete a leaf node
        avl_tree.delete(avl_tree.search(3))

        # Check that the node has been deleted
        self.assertIsNone(avl_tree.search(3))

    def test_avl_delete_node_with_one_child(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(5, "five")
        avl_tree.insert(3, "three")
        avl_tree.insert(7, "seven")
        avl_tree.insert(6, "six")

        # Delete a node with one child
        avl_tree.delete(avl_tree.search(7))

        # Check that the node has been deleted and the child node is connected to the parent
        self.assertIsNone(avl_tree.search(7))
        self.assertEqual(avl_tree.root.get_right().get_value(), "six")

    def test_avl_delete_node_with_two_children(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(5, "five")
        avl_tree.insert(3, "three")
        avl_tree.insert(7, "seven")
        avl_tree.insert(6, "six")
        avl_tree.insert(8, "eight")

        # Delete a node with two children
        avl_tree.delete(avl_tree.search(7))

        # Check that the node has been deleted and the successor node has taken its place
        self.assertIsNone(avl_tree.search(7))
        self.assertEqual(avl_tree.root.get_right().get_value(), "eight")
        self.assertEqual(avl_tree.root.get_right().get_left().get_value(), "six")

    def test_avl_delete_leaf_node_ten(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        nodes = [(i, str(i)) for i in range(1, 11)]  # Inserting numbers 1 to 10
        for key, value in nodes:
            avl_tree.insert(key, value)

        # Delete a leaf node
        avl_tree.delete(avl_tree.search(10))

        # Check that the node has been deleted
        self.assertIsNone(avl_tree.search(10))

    def test_avl_delete_node_with_one_child_ten(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        nodes = [(i, str(i)) for i in range(1, 11)]  # Inserting numbers 1 to 10
        for key, value in nodes:
            avl_tree.insert(key, value)

        # Delete a node with one child
        avl_tree.delete(avl_tree.search(9))

        # Check that the node has been deleted and the child node is connected to the parent
        self.assertIsNone(avl_tree.search(9))
        self.assertEqual(avl_tree.root.get_value(), "4")
        self.assertEqual(avl_tree.root.right.right.get_value(), "10")
        self.assertEqual(avl_tree.root.right.get_value(), "8")

    def test_avl_delete_node_with_two_children_ten(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(15, "15")
        avl_tree.insert(8, "8")
        avl_tree.insert(22, "22")
        avl_tree.insert(4, "4")
        avl_tree.insert(20, "20")
        avl_tree.insert(11, "11")
        avl_tree.insert(24, "24")
        avl_tree.insert(2, "2")
        avl_tree.insert(18, "18")
        avl_tree.insert(12, "12")
        avl_tree.insert(9, "9")
        avl_tree.insert(13, "13")

        # Delete a node with two children
        ans = avl_tree.delete(avl_tree.search(11))

        # Check that the node has been deleted and the successor node has taken its place
        self.assertIsNone(avl_tree.search(11))
        self.assertEqual(avl_tree.root.get_value(), "15")
        self.assertEqual(avl_tree.root.get_left().get_value(), "8")
        self.assertEqual(avl_tree.root.get_left().get_right().get_value(), "12")
        self.assertEqual(avl_tree.root.get_right().get_right().get_value(), "24")
        self.assertEqual(avl_tree.root.get_left().get_right().get_right().get_value(), "13")
        self.assertEqual(ans, 3)

    def test_avl_delete_node_with_two_rotations(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(15, "15")
        avl_tree.insert(8, "8")
        avl_tree.insert(22, "22")
        avl_tree.insert(4, "4")
        avl_tree.insert(20, "20")
        avl_tree.insert(11, "11")
        avl_tree.insert(24, "24")
        avl_tree.insert(2, "2")
        avl_tree.insert(18, "18")
        avl_tree.insert(12, "12")
        avl_tree.insert(9, "9")
        avl_tree.insert(13, "13")

        # Delete a node with two children
        avl_tree.delete(avl_tree.search(24))

        # Check that the node has been deleted and the successor node has taken its place
        self.assertIsNone(avl_tree.search(24))
        self.assertEqual(avl_tree.root.get_value(), "11")
        self.assertEqual(avl_tree.root.get_left().get_value(), "8")
        self.assertEqual(avl_tree.root.get_right().get_right().get_value(), "20")