import random
import sys
import heapq as heap
from collections import defaultdict

import pygame
from matplotlib import pyplot as plt
from pygame import gfxdraw

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import json
from aco import Graph, ACO


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""
    radius=15
    def __init__(self, graph:GraphInterface= DiGraph()):
        self.graph=DiGraph()
        self.graph=graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_jsonSring(self, jsonStr: str) -> bool:
        self.graph=DiGraph()
        dict = json.loads(jsonStr)
        nodes = dict["Nodes"]
        for n in nodes:
            if "pos" in n.keys():
                s = n["pos"].split(",")
                self.graph.add_node((int)(n["id"]), (s[0], s[1], s[2]))
            else:
                self.graph.add_node((int)(n["id"]))
        edges = dict["Edges"]
        for n in edges:
            self.graph.add_edge((int)(n["src"]), (int)(n["dest"]), (float)(n["w"]))
        return True

    def load_from_json(self, file_name: str) -> bool:
        self.graph = DiGraph()
        with open(file_name, 'r') as f:
            dict = json.load(f)
        nodes = dict.get("Nodes")
        for n in nodes:
            if "pos" in n.keys():
                s = n["pos"].split(",")
                self.graph.add_node((int)(n["id"]), (s[0], s[1], s[2]))
            else:
                self.graph.add_node((int)(n["id"]))
        edges = dict.get("Edges")
        for n in edges:
            self.graph.add_edge((int)(n["src"]), (int)(n["dest"]), (float)(n["w"]))
        return True

    def save_to_json(self, file_name: str) -> bool:
        class JsonGraph():
            def __init__(self,g:DiGraph):
                self.Edges = []
                for n in g.nodes.values():
                    for d,w in g.all_out_edges_of_node(n.getId()).items():
                        edge = {}
                        edge["src"] = n.getId()
                        edge["w"] = w
                        edge["dest"] = d
                        self.Edges.append(edge)
                self.Nodes = []
                for n in g.nodes.values():
                    node = {}
                    if (n.getLocation() is not None):
                        x, y, z = n.getLocation()
                        node["pos"] = f"{x},{y},{z}"
                    node["id"] = n.getId()
                    self.Nodes.append(node)

        toSave = JsonGraph(self.graph)
        with open(file_name+".json","w") as f:
            json.dump(toSave,fp=f,indent=4,default=lambda o:o.__dict__)
        return True

    # based on code from https://levelup.gitconnected.com/dijkstra-algorithm-in-python-8f0e75e3f16e
    def dijkstra(self, startingNode):
        """
        Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph
        :param startingNode: A node from which we start the algorithm
        :return: parentsMap - paths (which node was before), nodeCosts - distances from startingNode
        """
        visited = set()
        parentsMap = {}
        pq = []
        nodeCosts = defaultdict(lambda: float('inf'))
        nodeCosts[startingNode] = 0
        heap.heappush(pq, (0, startingNode))

        while pq:
            # go greedily by always extending the shorter cost nodes first
            _, node = heap.heappop(pq)
            visited.add(node)

            for adjNode, weight in self.graph.all_out_edges_of_node(node).items():
                if adjNode in visited:
                    continue

                newCost = nodeCosts[node] + weight
                if nodeCosts[adjNode] > newCost:
                    parentsMap[adjNode] = node
                    nodeCosts[adjNode] = newCost
                    heap.heappush(pq, (newCost, adjNode))

        return parentsMap, nodeCosts


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        """
        stack=[]
        curr=id2
        if id1 not in self.graph.nodes.keys()or id1 not in self.graph.nodes.keys():
           return (float('inf'), [])
        stack.append(self.graph.nodes[curr].getId())
        if id1 == id2:
            return (0,stack)
        parentsMap, nodeCosts =self.dijkstra(id1)
        dist = -1
        if str(nodeCosts[id2]) != "inf":
            dist = nodeCosts[id2]
        if dist == -1:
            return (float('inf'), [])
        while curr != id1:
            curr = parentsMap[curr]
            stack.append(self.graph.nodes[curr].getId())
        #NodeList=[]
        # while(stack):
        #     NodeList.append(stack.pop().getId())
        return (dist,stack)

    def floyd(self, G, node_lst: list[int]):
        """
        Finds all shortest paths that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :param G: graph
        :return: A dist of the shortest paths between a given nodes
        """
        dist = {}  # {} - create a dictionary
        for i in node_lst:
            dist[i] = {}  # {} - create a dict
            for j in node_lst:
                d, l = self.shortest_path(i, j)
                dist[i][j] = d  # () - create a tuple
        return dist

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        dist = self.floyd(self.graph, node_lst)

        # matrix_size - a size with all nodes for TSP
        rank = len(node_lst)

        # init the ACO class
        aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
        # init the Graph class
        graph = Graph(dist, rank)
        # call solve
        path, cost = aco.solve(graph)

        ans = []
        cost = 0
        for idx in range(len(path) - 1):
            c, tmp = self.shortest_path(path[idx], path[idx + 1])
            cost += c
            for t in tmp:
                ans.append(t)
            if (idx != len(path) - 2):
                ans.pop()
        return ans, cost


    def maxPathOfNode(self,node:int):
        max =sys.float_info.min
        parentsMap, nodeCosts = self.dijkstra(node)
        if len(nodeCosts) !=len(self.graph.nodes):
            return None
        for i in self.graph.nodes.keys():
            if i !=node:
                temp= nodeCosts[i]
                if temp>max:
                    max=temp
        return max


    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        min =sys.float_info.max
        for i in self.graph.nodes.keys():
            center = self.maxPathOfNode(i)
            if center is None:
                return None, float('inf')
            if center<min:
                min =center
                ans=i
        return ans,min
    def plot_graph(self) -> None:
        """ Draws the graph with pyplot library """
        plt.title("Directed Weighted Graph")
        plt.xlabel("x")
        plt.ylabel("y")
        locations = {}
        for node in self.graph.nodes.values():
            if node.getId() in locations.keys():
                x, y, z = locations[node.getId()]
            elif node.getLocation() is None:
                x, y, z = random.uniform(0, 100), random.uniform(0, 100),random.uniform(0, 100)
                locations[node.getId()]=(x,y,z)
            else:
                x, y, z = node.getLocation()
                locations[node.getId()] = (x, y, z)
            plt.plot(x, y, markersize=10, marker='.', color='blue')
            plt.text(x, y, str(node.getId()), color="red", fontsize=10)

            for dest in self.graph.all_out_edges_of_node(node.getId()).items():
                d, w = dest
                if d in locations.keys():
                    his_x, his_y, his_z = locations[d]
                elif self.graph.nodes[d].getLocation() is None:
                    his_x, his_y, his_z = random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)
                    locations[d] = (his_x, his_y, his_z)
                else:
                    his_x, his_y, his_z = self.graph.nodes[d].getLocation()
                    locations[d] = (his_x, his_y, his_z)

                plt.annotate("", xy=(x, y), xytext=(his_x, his_y), arrowprops=dict(arrowstyle="<-"))
                plt.text((x+his_x)/2, (y+his_y)/2, w, color="red", fontsize=5)
        plt.show()
