import random


class Graph(object):
    def __init__(self, cost_matrix: dict, size: int):
        """
        :param cost_matrix: matrix with all shortest paths of a given list of nodes
        :param matrix_size: size of the cost matrix
        """
        self.matrix_size = size
        self.matrix = cost_matrix
        self.pheromone = {}
        for i in self.matrix.keys():
            self.pheromone[i] = {}
            for j in self.matrix.get(i).keys():
                self.pheromone[i][j] = 1 / (size * size)


class ACO(object):
    def __init__(self, ant_count: int, generations: int, alpha: float, beta: float, rho: float, q: int, strategy: int):
        """
        :param ant_count: count of ant
        :param generations: number of generations
        :param alpha: relative importance of pheromone
        :param beta: relative importance of heuristic information
        :param rho: pheromone residual coefficient
        :param q: pheromone intensity
        :param strategy: pheromone update strategy. 0 - ant-cycle, 1 - ant-quality, 2 - ant-density
        """
        self.Q = q
        self.rho = rho
        self.beta = beta
        self.alpha = alpha
        self.ant_count = ant_count
        self.generations = generations
        self.update_strategy = strategy

    def _update_pheromone(self, graph: Graph, ants: list):
        for i in graph.pheromone.keys():
            for j in graph.pheromone.get(i).keys():
                graph.pheromone[i][j] *= self.rho
                for ant in ants:
                    graph.pheromone[i][j] += ant.pheromone_delta[i][j]


    def solve(self, graph: Graph):
        """
        Sloves the TSP: find the shortest path as near as possible between all the given nodes
        :param graph: graph with matrix of all shortest path between a given nodes
        :return: A list of the nodes id's in the path, and the overall distance
        """
        best_cost = float('inf')
        best_solution = []
        for gen in range(self.generations):
            # noinspection PyUnusedLocal
            ants = [_Ant(self, graph) for i in range(self.ant_count)]

            for ant in ants:
                for i in graph.matrix.keys():
                    ant._select_next()
                if graph.matrix[ant.tabu[-1]][ant.tabu[0]] != float('inf'):
                    ant.total_cost += graph.matrix[ant.tabu[-1]][ant.tabu[0]]
                if ant.total_cost < best_cost:
                    best_cost = ant.total_cost
                    best_solution = [] + ant.tabu
                # update pheromone
                ant._update_pheromone_delta()

            self._update_pheromone(graph, ants)
        return best_solution, best_cost


class _Ant(object):
    """ Ant class """
    def __init__(self, aco: ACO, graph: Graph):
        self.colony = aco
        self.graph = graph
        self.total_cost = 0.0
        self.tabu = []  # tabu list
        self.pheromone_delta = []  # the local increase of pheromone

        self.allowed = [key for key in graph.matrix.keys()]  # nodes which are allowed for the next selection

        self.eta = {}
        for i in self.graph.matrix.keys():
            self.eta[i] = {}
            for j in self.graph.matrix.get(i).keys():
                if i == j:
                    self.eta[i][j] = 0
                else:
                    self.eta[i][j] = 1 / graph.matrix[i][j]

        # manipulations for find random
        n = random.randint(0, len(self.allowed)-1)
        start = self.allowed[n]   # start from any node

        self.tabu.append(start)
        self.current = start
        self.allowed.remove(start)

    def _select_next(self) -> None:
        """ selects next node by probability roulette """
        denominator = 0
        for i in self.allowed:
            denominator += \
                (self.graph.pheromone[self.current][i] ** self.colony.alpha) * \
                (self.eta[self.current][i] ** self.colony.beta)

        probabilities = {}
        for key in self.graph.matrix.keys():
            probabilities[key] = 0
        for i in self.graph.matrix.keys():
            try:
                self.allowed.index(i)  # test if allowed list contains i
                if denominator != 0:
                    probabilities[i] = self.graph.pheromone[self.current][i] ** self.colony.alpha * \
                        self.eta[self.current][i] ** self.colony.beta / denominator
            except ValueError:
                pass  # do nothing

        if len(self.allowed) != 0:
            selected = self.allowed[0]
            rand = random.random()

            for key in probabilities.keys():
                rand -= probabilities[key]
                if rand <= 0:
                    selected = key
                    break

            self.allowed.remove(selected)
            self.tabu.append(selected)
            self.total_cost += self.graph.matrix[self.current][selected]
            self.current = selected

    def _update_pheromone_delta(self):
        """ updates pheromone on the path """
        self.pheromone_delta = {}
        for i in self.graph.matrix.keys():
            self.pheromone_delta[i] = {}
            for j in self.graph.matrix.get(i).keys():
                self.pheromone_delta[i][j] = 0

        for _ in range(1, len(self.tabu)):
            i = self.tabu[_ - 1]
            j = self.tabu[_]
            if self.colony.update_strategy == 1:  # ant-quality system
                self.pheromone_delta[i][j] = self.colony.Q
            elif self.colony.update_strategy == 2:  # ant-density system
                self.pheromone_delta[i][j] = self.colony.Q / self.graph.matrix[i][j]
            else:  # ant-cycle system
                self.pheromone_delta[i][j] = self.colony.Q / self.total_cost