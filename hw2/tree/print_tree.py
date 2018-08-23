class Tree(object):

    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None

# return the depth of tree
    def getDepth(self, root):
        if root is None or not(isinstance(root,Node)) or (root.left is None and root.right is None):
            return 1
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

# return the positions of nodes in list of lists
# param root: node
# param tree_struc: list of lists
# param row: int
# param col: int
    def nodePos(self, root, tree_struc, row, col):
        if isinstance(root, Node):
            tree_struc[-row -1][col] = root.value
            if root.left:
                self.nodePos(root.left, tree_struc, row - 1, col - 2 ** (row - 1))
            if root.right:
                self.nodePos(root.right, tree_struc, row - 1, col + 2 ** (row - 1))
        else:
            tree_struc[-row -1][col] = root
           
        return tree_struc

# print the tree
    def printTree(self):
        d = self.getDepth(self.root)
        if d ==1:
            tree_struc = ['|', self.get_value_root(), '|' ]
            for l in tree_struc:
                print(l, end = '')
            print()
        else:   
            w = 2**d - 1
            tree_struc = [['|' for i in range(w)] for j in range(d)]
            tree_struc = self.nodePos(self.root, tree_struc, d - 1, 2**(d - 1)-1)
            for l in tree_struc:
                for n in l:
                    print(n, end = '')
                print()

class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

