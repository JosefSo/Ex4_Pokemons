import json


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
        return True

    def load_Pokemons_from_json(self, jsonStr: str) -> bool:
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
        self.pokemons.sort()
        return True