import unittest
from graph.graph import find_shortest_path, find_negative_cycles,getGraph,getEdges

class TestGraphs(unittest.TestCase):
    def test_shortest1(self):
        self.path1 = find_shortest_path("graph.txt", 1, 8)
        self.answer1 = (8.0, [1.0, 3.0, 5.0, 7.0, 8.0])
        assert self.path1 == self.answer1
        
    def test_shortest2(self):
        self.path2 = find_shortest_path("graph.txt", 1, 1)
        self.answer2 = (0, [1.0])
        assert self.path2 == self.answer2
        
    def test_shortest3(self):
        self.path3 = find_shortest_path("graph.txt", 2,7)
        self.answer3 = None
        assert self.path3 == self.answer3
    
    def test_negCycle1(self):
        self.cycle1 = find_negative_cycles("graph2.txt")
        self.answer4 = None
        assert self.cycle1 == self.answer4
        
    def test_negCycle2(self):
        self.cycle2 = find_negative_cycles("graph.txt")
        self.answer5 = [5.0, 7.0, 8.0, 5.0]
        assert self.cycle2 == self.answer5
