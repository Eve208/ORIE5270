
import unittest

from print_tree import Tree,Node

class TestPrintTree(unittest.TestCase):
    def setUp(self):
        node1 = Node(1, None, None)
        node2 = Node(2, None, None)
        node3 = Node(3, None, None)
        node4 = Node(4, None, None)
        node5 = Node(5, None, None)
        node6 = Node(6, None, None)
        node7 = Node(7, None, None)
        
        # tree with only one node
        self.tree1 = Tree(node1)
        self.print1 = self.tree1.printTree()
        self.answer1 = ["|",1,"|"]
        
        # tree with only left nodes
        node3.left = node4
        node2.left = node3
        node1.left = node2
        self.tree2 = Tree(node1)
        self.print2 = self.tree2.printTree()
        self.answer2 = [['|', '|', '|', '|', '|', '|', '|', 1, '|', '|', '|', '|', '|', '|', '|'],
                        ['|', '|', '|', 2, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                        ['|', 3, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                        [4, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        
        # full tree
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        node1.left = node2
        node1.right = node3
        self.tree3 = Tree(node1)
        self.print3 = self.tree3.printTree()
        self.answer3 = [["|", "|", "|", 1, "|", "|", "|"],
                        ["|", 2, "|", "|", "|", 3, "|"],
                        [4, "|", 5, "|", 6, "|", 7]]
        
        # other case
        node2.left = None
        node2.right = node5
        node3.left = node6
        node3.right = None
        node1.left = node2
        node1.right = node3
        self.tree4 = Tree(node1)
        self.print4 = self.tree4.printTree()
        self.answer4 = [["|", "|", "|", 1, "|", "|", "|"],
                        ["|", 2, "|", "|", "|", 3, "|"],
                        ["|", "|", 5, "|", 6, "|", "|"]]
        
        
    # test tree with only one node 
    def test1(self):
        self.assertEqual(self.print1,self.answer1)
        
    # test tree with only left nodes
    def test2(self):
        self.assertEqual(self.print2,self.answer2)
        
    # test full tree
    def test3(self):
        self.assertEqual(self.print3,self.answer3)
    
    # other case
    def test4(self):
        self.assertEqual(self.print4,self.answer4)
    

