# Ex4_Pokemons

#Requirements

In order to run the game properly your python have to include the following libraries:
1. pygame. to install it go to python console and type "pip install pygame"

# Ex3_DWG - Directed Weighted Graph in Python

This OOP project deals with the realization of weighted and directed graphs. It includes a few calculations on the graph via well-known algorithms such as Floyd-Warshall algorithm and Dijkstra algorithm and also it includes the GUI (graphical user interface) to show the graph itself and it's calculations to the user. 
As part of implementing the graphs we implemented classes:


* class GraphAlgoInterface.py
* class GraphInterface.py
* class GraphAlgo.py
* class DiGraph.py
* class aco.py
* class main.py
* class test_DiGraph.py
* class test_GraphAlgo.py

<br>
- GraphAlgoInterface.py and GraphInterface.py are interfaces to GraphAlgo.py and DiGraph.py. There are functions and explinations about implements.
<br>
- In DiGraph.py we have 3 classes: Node, Edge, DiGraph itself and some basic functions on graph such as getters, setters, add Node, remove Node, remove Edge etc.
<br>
- In GraphAlgo.py we have algorithms on grpah such as find shortest path, find center on graph, tsp. GraphAlgo.py uses DiGraph. 
<br>
- In aco.py we have three classes: ACO, Graph, Aunt we use them to implement ACO algorithm for solving TSP.
<br>
- In main.py we have three check functions that checks if our algorithms work corectly. main.py uses GraphAlgo.py
<br>
- test_DiGraph.py and test_GraphAlgo.py are tests for our program.
<br>
<br>

link to the wiki: <br>
https://github.com/JosefSo/Ex3_DWG/wiki

## Pre-Work

We already implemented these algorithms in Java you can have a look at this: <br>
https://github.com/SaliSharfman/Ex2_DirectedWeightedGraph.git


## Algorithms 

🔹Center: Finds the node that has the shortest distance to it's farthest node. Our algorithm for finding center is based on Dijkstra.

![rneVg](https://user-images.githubusercontent.com/77780368/147604052-001066c4-5886-42ce-a6e5-82257c2b40b3.png)

🔹Shortest path: finding the shortest path between two nodes and its length. Our algorithm for finding shortest path is based on Dijkstra algorithm.
<br> 
More about Dijkstra: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

![Dijkstra_Animation](https://user-images.githubusercontent.com/77780368/147604706-c57dd14a-ded5-4160-b734-5bd6ad4947a5.gif) <br>
Dijkstra's algorithm to find the shortest path between a and b. It picks the unvisited vertex with the lowest distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. Mark visited (set to red) when done with neighbors.  <br>
![DijkstraDemo](https://user-images.githubusercontent.com/77780368/147604870-42dbf28e-91ad-42cf-a164-fb0861655a9c.gif) <br>
A demo of Dijkstra's algorithm based on Euclidean distance. Red lines are the shortest path covering, i.e., connecting u and prev[u]. Blue lines indicate where relaxing happens, i.e., connecting v with a node u in Q, which gives a shorter path from the source to v.
<br>



🔹TSP (travelling salesman problem): tsp - asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research. <br>
More about tsp:  https://en.wikipedia.org/wiki/Travelling_salesman_problem <br>
Our tsp function finds the shortest path between all given nodes on the graph. We've used ACO (Ant colony optimization) algorithm to solve this problem. ACO is a probabilistic technique for solving computational problems which can be reduced to finding good paths through graphs. Our ACO algorithm depends on a randomaly desicions so it may give a different results on the same input data. <br>
More about ACO:  https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms <br>

![AntColony](https://user-images.githubusercontent.com/77780368/147604381-28079434-1390-4ce9-b86f-a7d2bdecb753.gif)

A little bit more about the algorithm (you can skip it):<br> Artificial ants stand for multi-agent methods inspired by the behavior of real ants. The pheromone-based communication of biological ants is often the predominant paradigm used. Combinations of artificial ants and local search algorithms have become a method of choice for numerous optimization tasks involving some sort of graph, e.g., vehicle routing and internet routing.

As an example, ant colony optimization is a class of optimization algorithms modeled on the actions of an ant colony. Artificial 'ants' (e.g. simulation agents) locate optimal solutions by moving through a parameter space representing all possible solutions. Real ants lay down pheromones directing each other to resources while exploring their environment. The simulated 'ants' similarly record their positions and the quality of their solutions, so that in later simulation iterations more ants locate better solutions. One variation on this approach is the bees algorithm, which is more analogous to the foraging patterns of the honey bee, another social insect.

![Artificial_ants](https://user-images.githubusercontent.com/77780368/147603511-8f003663-f8eb-4efd-8e02-6df8dd9dc5cd.jpg)


## matplotlib

We used matplotlib to draw the graphs, here some screenshots of the results:

check 0, no pos so the pos is random between 0-100:  <br>

![image](https://user-images.githubusercontent.com/75334138/147599233-29f5bc5d-db32-4950-8639-035549e3ece8.png)
 
check1 (T0), no pos so the pos is random between 0-100: <br>

![image](https://user-images.githubusercontent.com/75334138/147599314-738e8289-4336-40bd-8cad-fcabe8dce715.png)

check2 (A5 after removing an edge) with pos: <br>

![image](https://user-images.githubusercontent.com/75334138/147599385-7693df7b-9a2d-41de-bee5-ff0d9931cb25.png)

check3 no pos so the pos is random between 0-100: <br>

![image](https://user-images.githubusercontent.com/75334138/147599517-3d353ebe-de48-4327-9046-38e8b4ba79a5.png)



## UML

link to UML: [UML_Ex3_DWG.pdf](https://github.com/JosefSo/Ex3_DWG/files/7786355/UML_Ex3_DWG.pdf)


![UML_Ex3_DWG](https://user-images.githubusercontent.com/86108478/147605870-3a01f9dc-d4bb-41c3-9543-7843e4ad8584.jpg)



## How To Run

🔹In order to run the program you will have to install matplotlib library. to install it in the terminal pip install matplotlib. <br>

![image](https://user-images.githubusercontent.com/75334138/147597429-72bb6735-c163-43cb-9165-899a96286178.png)</br>
🔹Download the zip of the project code. <br>
🔹Open cmd. <br>
🔹cd to src directory. <br>
🔹You have now 2 choices: <br>
1.Run the check() method that given with the task: write the next command "python main.py" (check0-check3 will be ran al plotted). <br>
![image](https://user-images.githubusercontent.com/86108478/147611164-ead346e7-d514-40bc-83f7-3e5abf09b559.png) <br>

2.Plot graph from json: write the next command "python main.py FileName.json" (FileName will be any direction for json file that you have).  <br>
![image](https://user-images.githubusercontent.com/86108478/147611237-23a90072-d790-4ed8-9df9-7497dba6ba2c.png) <br>


An exapmle of output like the required output of the main: <br>
![image](https://user-images.githubusercontent.com/75334138/147598653-ef875698-f9b2-4822-ab53-2d6fd3398ce5.png)






