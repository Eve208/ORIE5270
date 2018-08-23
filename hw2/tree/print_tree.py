class Tree(object):

    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        """
        :return: (int) value of the root
        """
        if self.root is not None:
            return self.root.value
        else:
            return None

    def getDepth(self, root):
        """
        :param root: (Node)
        :return: (int) the depth of the tree
        """
        if root is None or not(isinstance(root,Node)) or (root.left is None and root.right is None):
            return 1
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1


    def nodePos(self, root, tree_struc, row, col):
        """
        :param root: (Node)
        :param tree_struc: (list of lists)
        :param row: (int)
        :param col: (int)
        :return: (list of lists) contains all the nodes
        """
        if isinstance(root, Node):
            tree_struc[-(row+1)][col] = root.value
            if root.left:
                self.nodePos(root.left, tree_struc, row - 1, col - 2 ** (row - 1))
            if root.right:
                self.nodePos(root.right, tree_struc, row - 1, col + 2 ** (row - 1))
        else:
            tree_struc[-(row+1)][col] = root
           
        return tree_struc

    def printTree(self):
        """
        :return: (list of list) tree with empty spaces represented by '|'
        """
        d = self.getDepth(self.root)
        if d ==1:
            tree_struc = ['|', self.get_value_root(), '|' ]
            return tree_struc
        else:   
            w = 2**d - 1
            tree_struc = [['|' for i in range(w)] for j in range(d)]
            tree_struc = self.nodePos(self.root, tree_struc, d - 1, 2**(d - 1)-1)
            return tree_struc

class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
