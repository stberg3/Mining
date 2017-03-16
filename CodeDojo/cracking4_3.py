# cracking4-3.py
# Given a non-decreasing array create a binary search tree of minimum height.

from math import ceil
from random import randrange

array = [randrange(100) for i in range(10)]
array.sort()
# print(array)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.weight = 0
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.data) + " (" + str(self.weight) + ")"

    def __repr__(self):
        return str(self)

class AVLTree(object):
    def __init__(self, array=None):
        self.root = None
        if array != None:
            for el in array:
                self.add(el)

    def left_rotate(self, node):
        node.right_child.left_child = node
        node.right_child = None
        node.weight -= 1
        print("   ",node)
        print(node.left_child,"\t", node.right_child)

    def right_rotate(self, node):
        node.left_child.right_child = node
        node.left_child = None
        node.weight += 1
        print("   ",node)
        print(node.left_child,"\t", node.right_child)

    def add(self, data):
        # spec. case
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            return

        probe_parent = None
        probe = self.root

        while probe != None:
            if new_node.data < probe.data:
                probe.weight += 1
                probe_parent = probe
                probe = probe.right_child
            elif probe.data < new_node.data:
                probe.weight -= 1
                probe_parent = probe
                probe = probe.left_child
            else:
                raise ValueError("Bad key: dups disallowed {0}".format(probe))

        if new_node.data < probe_parent.data:
            probe_parent.left_child = new_node
        elif new_node.data > probe_parent.data:
            probe_parent.right_child = new_node
        else:
            raise ValueError("Bad key: dups disallowed {0}".format(probe))

        # if probe_parent.weight > 1:
        #     print("left rotate on {0}".format(probe.data))
        #     left_rotate(probe_parent)
        # elif probe_parent.weight < -1:
        #     print("right rotate on {0}".format(probe.data))
        #     right_rotate(probe_parent)

        if probe_parent.data < new_node.data:
            print("Setting {0}'s right_child to {1}".format(
                probe_parent.data, new_node.data))
            probe_parent.right_child = new_node
        else:
            print("Setting {0}'s left to {1}".format(
                probe_parent.data, new_node.data))
            probe_parent.left_child = new_node

        # if probe_parent.weight > 1:
        #     print("left rotate on {0}".format(probe_parent.data))
        #     self.left_rotate(probe_parent)
        # elif probe_parent.weight < -1:
        #     print("right rotate on {0}".format(probe_parent.data))
        #     self.right_rotate(probe_parent)


    inOrderList = None

    def inOrder(self):
        self.inOrderHelper()
        return self.inOrderList

    def inOrderHelper(self, node=None):
        if node == None:
            node = self.root
            self.inOrderList = [node]

        if node.left_child:
            self.inOrderHelper(node.left_child)

        # print(node)
        self.inOrderList.insert(0,node)

        if node.right_child:
            self.inOrderHelper(node.right_child)

from random import randint

def load_tree(n=10):
    return AVLTree([randint(0,200) for i in range(n)])

tree = load_tree()
print(tree.inOrder())
