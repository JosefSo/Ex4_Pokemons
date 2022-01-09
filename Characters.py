import json
import operator

from DiGraph import DiGraph


class Agent:
    def __init__(self, id:int,value:float,src:int,dest:int,speed:float,pos:tuple=None,isBussy:bool=False):
        self.id=id
        self.value=value
        self.src=src
        self.dest=dest
        self.speed=speed
        if pos is not None:
            x, y, z = pos
            self.pos = float(x), float(y), float(z)
        else:
            self.pos = None
        self.isBussy=isBussy
    def getId(self) ->int:
        return self.id
    def setId(self,id:int):
        self.id=id
    def getLocation(self) ->tuple:
        return self.pos
    def setLocation(self,x:float,y:float,z:float):
        self.pos=(x,y,z)
    def __lt__(self, other):
        return self.speed > other.speed

class Pokemon:
    def __init__(self, value:float,type:int,pos:tuple=None):
        self.value= value
        self.type=type
        if pos is not None:
            x, y, z = pos
            self.pos = float(x), float(y), float(z)
        else:
            self.pos = None

    def getLocation(self) -> tuple:
        return self.pos

    def setLocation(self, x: float, y: float, z: float):
        self.pos = (x, y, z)
    def getEdge(self,graph:DiGraph):
        EPS=0.00001
        x,y,z=self.pos
        for v1 in graph.get_all_v().keys():
            dv1 = graph.distNodeToPoint(v1,(x,y,z))
            for v2 in graph.all_out_edges_of_node(v1).keys():
                dv2 = graph.distNodeToPoint(v2, (x, y, z))
                tup=graph.equationAndDist(v1,v2)
                m,n,d=tup
                if y+EPS>(m*x)+n and y-EPS<(m*x)+n:
                    if d+EPS>dv1+dv2 and d-EPS<dv1+dv2:
                        if self.type<0 and v1>v2:
                            return (v1,v2)
                        return (v2,v1)
        return None



    def __lt__(self, other):
        return self.value > other.value
    def __repr__(self):
        return f"value: {self.value}, type:{self.type}"
    def __str__(self):
        return f"value: {self.value}, type:{self.type}"


class Characters:
    def __init__(self):
        self.agents = []
        self.pokemons = []
        self.agentspaths = {}
        #self.agentsvalues={}
        self.edegesValues=[]
    def load_Agents_from_json(self, jsonStr: str) -> bool:
        self.agents = []
        dict = json.loads(jsonStr)
        elements = dict["Agents"]
        for ag in elements:
            id = int(ag.get("Agent")["id"])
            value=float(ag.get("Agent")["value"])
            src = int(ag.get("Agent")["src"])
            dest = int(ag.get("Agent")["dest"])
            speed = float(ag.get("Agent")["speed"])
            location = ag.get("Agent")["pos"].split(",")
            pos=(location[0], location[1], location[2])
            agent=Agent(id,value,src,dest,speed,pos)
            self.agents.append(agent)

        self.agents.sort()
        self.agents.reverse()
        return True

    def load_Pokemons_from_json(self, jsonStr: str,graph:DiGraph) -> bool:
        edegesValuesDic = {}
        self.pokemons = []
        dict = json.loads(jsonStr)
        elements = dict["Pokemons"]
        for ag in elements:
            value = float(ag.get("Pokemon")["value"])
            type = int(ag.get("Pokemon")["type"])
            location = ag.get("Pokemon")["pos"].split(",")
            pos = (location[0], location[1], location[2])
            pokemon = Pokemon(value,type, pos)
            self.pokemons.append(pokemon)
            edge= pokemon.getEdge(graph)
            if edge not in edegesValuesDic.keys():
                edegesValuesDic[edge]= pokemon.value
            else:
                edegesValuesDic[edge] = edegesValuesDic[edge]+pokemon.value
        self.edegesValues = sorted(edegesValuesDic.items(), key=operator.itemgetter(1))
        self.edegesValues.reverse()
        self.pokemons.sort()


        return True