# Ex4_Pokemons - Pokemons game on Directed Weighted Graph in Python

This project represents the game of pokemons on Directed Weighted Graph. The main goal of this game is to catch as many Pokemons as we can so that each catch of a Pokemon will update our grade and eventually will return the final grade score . In this project we built a directional weighted graph and the graph will be visualized by using GUI.

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

## Pre-Work

We already implemented these algorithms in Java you can have a look at this: <br>
https://github.com/SaliSharfman/Ex2_DirectedWeightedGraph.git
https://github.com/SaliSharfman/Ex3_DWG.git


## Algorithms 




## How To Run

#Requirements

In order to run the game properly your python have to include the following libraries:
1. pygame. to install it go to python console and type "pip install pygame"
