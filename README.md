# Ex4_Pokemons - pokemons game in Python


This OOP project deals with the realization of the pokemons game. We have server to which our client connects. Server gets masseges from client for examle: how to move Agent. Server knows change agent locations and spam pokemons on the graph.  The programm uses weighted and directed graphs.  It includes a few calculations on the graph via well-known algorithms such as Dijkstra algorithm and also it includes the GUI (graphical user interface) to show the graph itself and it's calculations to the user. 
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
https://github.com/JosefSo/Ex4_Pokemons/wiki

## Pre-Work

We already implemented these algorithms in Java you can have a look at this: <br>
https://github.com/SaliSharfman/Ex3_DWG.git


## Algorithms 




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

#Requirements

🔹In order to run the game properly your python have to include the following libraries:
1. pygame. to install it go to python console and type "pip install pygame"







