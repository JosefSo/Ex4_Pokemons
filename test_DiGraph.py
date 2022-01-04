from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
"""
this is the test class for DiGraph, we are also using GraphAlgo for convenience.
every test should work if running it alone. every test checks out unique bugs that could occur
"""
class TestDiGraph(TestCase):

    def test_v_size(self):
        a_algo = GraphAlgo()
        file = "../data/G1.json"
        a_algo.load_from_json(file)
        a = a_algo.get_graph().v_size()
        self.assertEqual(17,a)


    def test_e_size(self):
        b_algo = GraphAlgo()
        file = "../data/G1.json"
        b_algo.load_from_json(file)
        self.assertEqual(36,b_algo.get_graph().e_size())

    def test_get_all_v(self):
        c_algo = GraphAlgo()
        file = "../data/G1.json"
        c_algo.load_from_json(file)
        a = c_algo.get_graph().get_all_v()
        i=0
        for k,v in a.items():
            self.assertEqual(i,v.getId())
            self.assertEqual(i,k)
            i=i+1

    def test_all_in_edges_of_node(self):
        d_algo = GraphAlgo()
        file = "../data/G1.json"
        d_algo.load_from_json(file)
        a = d_algo.get_graph().all_in_edges_of_node(1).keys()
        self.assertEqual({0,2},a)


    def test_all_out_edges_of_node(self):
        e_algo = GraphAlgo()
        file = "../data/G1.json"
        e_algo.load_from_json(file)
        v = e_algo.get_graph().all_out_edges_of_node(1).keys()
        self.assertEqual(v,e_algo.get_graph().all_out_edges_of_node(1).keys())

    def test_get_mc(self):
        g_algo = GraphAlgo()
        file = "../data/G2.json"
        g_algo.load_from_json(file)
        self.assertEqual(111, g_algo.graph.get_mc())
        a = g_algo.get_graph().remove_edge(1,2)
        b=g_algo.get_graph().get_mc()
        self.assertEqual(b, 112)
        g_algo.graph.remove_node(0)
        self.assertEqual(119,g_algo.graph.get_mc())

    def test_add_edge(self):
        f_algo = GraphAlgo()
        file = "../data/G1.json"
        f_algo.load_from_json(file)
        f_algo.get_graph().add_edge(1, 7, 3.3)
        self.assertEqual(f_algo.graph.e_size(),37)

    def test_add_node(self):
        g_algo = GraphAlgo()
        file = "../data/G1.json"
        g_algo.load_from_json(file)
        g_algo.get_graph().add_node(18)
        self.assertEqual(18,g_algo.graph.v_size())
        g_algo.get_graph().add_node(19,(2,2,2))
        self.assertEqual(19, g_algo.graph.v_size())

    def test_remove_node(self):
        h_algo = GraphAlgo()
        file = "../data/G1.json"
        h_algo.load_from_json(file)
        h_algo.graph.remove_node(0)
        self.assertEqual(16, h_algo.graph.v_size())

    def test_remove_edge(self):
        i_algo = GraphAlgo()
        file = "../data/G1.json"
        i_algo.load_from_json(file)
        i_algo.graph.remove_edge(1,2)
        self.assertEqual(35, i_algo.graph.e_size())
