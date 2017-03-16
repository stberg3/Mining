# AVLTree.py

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
                probe.weight -= 1
                probe_parent = probe
                probe = probe.left_child
            elif probe.data < new_node.data:
                probe.weight += 1
                probe_parent = probe
                probe = probe.right_child
            else:
                raise ValueError("Bad key: dups disallowed {0}".format(probe))

        if new_node.data < probe_parent.data:
            probe_parent.left_child = new_node
        elif new_node.data > probe_parent.data:
            probe_parent.right_child = new_node
        else:
            raise ValueError("Bad key: dups disallowed {0}".format(probe))

    def inOrder(self):
        self.inOrderHelper()
        return self.inOrderList

    def inOrderHelper(self, node=None):
        if node == None:
            node = self.root
            self.inOrderList = [node]

        if node.left_child:
            self.inOrderHelper(node.left_child)

        self.inOrderList.insert(0,node)

        if node.right_child:
            self.inOrderHelper(node.right_child)

tree = AVLTree()
tree.add(0)
tree.add(-10)
tree.add(10)
tree.add(7)
tree.add(11)

print(tree.inOrder())
