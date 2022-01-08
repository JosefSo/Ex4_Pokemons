# Ex4_Pokemons - Pokemons game on Directed Weighted Graph in Python

This project represents the game of pokemons on Directed Weighted Graph. The main idea of this game is to catch as many pokemons as we can so each catch of a pokemon will update our score and in the end will return the final grade score . In this project we did algorithm that sends agents to catch pokemons, connected a directed weighted graph to the algorithm and also we have used client that connects to the game's server. All the game is visualized by GUI with a different agents that run after different pokemons on the graph map. Also we have music on the background og the game.
<br> <br>
![pok](https://user-images.githubusercontent.com/77780368/148662389-3cc8bf19-a054-4114-badf-7dc8f28241a7.jpg)
<br>

## Implemented classes 
As part of implementing the graphs we implemented classes:

* class GraphAlgoInterface.py
* class GraphInterface.py
* class GraphAlgo.py
* class DiGraph.py
* class aco.py
* class main.py
* class test_DiGraph.py
* class test_GraphAlgo.py
* Characters.py
* client.py
* Ex4GUI.py
* GameAlgo.py
* ImagesManager.py


<br>
- In Characters.py we have three classes: 1.Class Agent, where is all data of our agents: speed, position and more 2.Class Pokemon: where is all data of our pokemons: value - how much pokemon costs, position on the graph and more 3.Class Characters: where is all data of our agents and pokemons, we used two list to save this data: agents = [], pokemons = [] and also class include two function that loads data of pokemons from json to our lists. Characters.py uses json library.
<br>
- client.py - it is client that connects to the server of the pokenons game
<br>
- Ex4GUI.py - visualization of the pokemons game on the screen by using GUI
<br>
- GameAlgo.py - where is the main algorithm of the game that sends agents to catch pokemons.
<br>
- ImagesManager.py - where is all pictures of the pokemons of game.
<br>
- In main.py we have three check functions that checks if our algorithms work corectly. main.py uses GraphAlgo.py
<br>
- GraphAlgoInterface.py and GraphInterface.py are interfaces to GraphAlgo.py and DiGraph.py. There are functions and explinations about implements.
<br>
- In DiGraph.py we have 3 classes: Node, Edge, DiGraph itself and some basic functions on graph such as getters, setters, add Node, remove Node, remove Edge etc.
<br>
- In GraphAlgo.py we have algorithms on grpah such as find shortest path, find center on graph, tsp. GraphAlgo.py uses DiGraph. 
<br>
- In aco.py we have three classes: ACO, Graph, Aunt we use them to implement ACO algorithm for solving TSP.
<br>
- test_DiGraph.py and test_GraphAlgo.py are tests for our program.
<br>
<br>
<br>

link to the wiki: <br>
https://github.com/JosefSo/Ex4_Pokemons/wiki

## The main algorithm of the game

The main algorithm of the game that sends agents to catch pokemons. Of a given agents with different speeds and pokemons with a different cost values, we faced a problem how to rich the most score as possible, how to catch the most pokemons on the given time. So we created list of agents and list of pokemons, both of them we're sorting from best to worst on each iteration of the game with the help of __lt__ function that we Implemented and it knows how to sort right our lists. Every time our algorithm sends the best agent to most cost value pokemon in order to rich as more score as possible. Also our algorithm knows to spam our agents at he beggining of the game in the best places to avoid extra steps that agents do to rich pokemons. This way our agents spam at the beggining and imediatly start to eat the pokemons.

## UML
<br>
Link to UML: [UML.pdf](https://github.com/JosefSo/Ex4_Pokemons/files/7834191/UML.pdf)

<br>
<br>

![UML](https://user-images.githubusercontent.com/77780368/148663417-635da90f-f97d-4a72-90a2-add245f5fe1a.jpeg)


<br>

## Pre-Work

We already implemented some of the algorithms on the graph that our game uses, you can have a look at this: <br>
https://github.com/JosefSo/Ex3_DWG <br>
https://github.com/SaliSharfman/Ex2_DirectedWeightedGraph
<br>



## How To Run

#Requirements

In order to run the game properly your python have to include the following libraries:
1. pygame. to install it go to python console and type "pip install pygame"
