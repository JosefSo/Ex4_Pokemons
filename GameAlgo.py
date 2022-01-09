import json
import time as ti


class GameAlgo:

    def __init__(self,graph_algo):
        self.graph_algo=graph_algo
        self.isAgentSent = {}
        for s in graph_algo.get_graph().get_all_v().keys():
            for d in graph_algo.get_graph().all_out_edges_of_node(s):
                self.isAgentSent[(s, d)] = False
        self.sc=[0,0,0]
        self.gamelog=f""



    def syncValuesWithShorterPath(self,edegesValues:list,src:int,speed:float):
        newlist=[]
        for i in range(len(edegesValues)):
            e,v=edegesValues[i]
            d, l = self.graph_algo.shortest_path(src, e[0])
            # d = d + self.graph_algo.shortest_path(e[0], e[1])[0]
            val=9999+v
            if d>0 and len(l)>1:
                val=v/(d/speed)
            newlist.append((e,val))
        newlist.sort(key=lambda x:x[1])
        newlist.reverse()
        return newlist

    def sortByPaths(self,edegesValues:list,src:int,speed:float):
        newlist=[]
        for i in range(len(edegesValues)):
            e,v=edegesValues[i]
            d, l = self.graph_algo.shortest_path(src, e[0])
            d=d+self.graph_algo.shortest_path(e[0], e[1])[0]
            t=d/speed
            newlist.append((e,t))
        newlist.sort(key=lambda x:x[1])
        # newlist.reverse()
        return newlist

    def danielsort(self, edegesValues: list, src: int, speed: float):
        newlist = []
        for i in range(len(edegesValues)):
            e, v = edegesValues[i]
            d, l = self.graph_algo.shortest_path(src, e[0])
            l.reverse()
            l.append(e[1])
            # d = d + self.graph_algo.shortest_path(e[0], e[1])[0]
            val=0.0
            for k in range(len(l)-1):
                for j in edegesValues:
                    if j[0]==(l[k],l[k+1]):
                        val=val+j[1]
                    # if j[0]==(l[k+1],l[k]):
                    #     val=val+j[1]
            if d>0 and len(l)>1:
                val=v/d

            t = val / speed
            newlist.append((e, val))
        newlist.sort(key=lambda x: x[1])
        newlist.reverse()
        return newlist


    def choose_next_edge(self,characters,client)->tuple:
        lonlyagent=len(characters.agents)==1
        for agent in characters.agents:
            agentsnames={0:"Ash",1:"Misty",2:"Brook"}
            try:
                info = json.loads(client.get_info())
                score = info.get("GameServer")["grade"]
            except:
                break

            if self.sc[(int(agent.getId()) % 3)]<agent.value:
                name, points=agentsnames[(int(agent.getId()) % 3)],agent.value-self.sc[(int(agent.getId()) % 3)]
                print(f"{name} raised {points} points, total score: {score}.")
                log=self.gamelog
                self.gamelog = f"{log}{float(client.time_to_end())/1000} seconds to end: +{points} to {name} {client.get_info()}\n"
                self.sc[(int(agent.getId()) % 3)] = agent.value

            if agent.dest == -1:
                if characters.agentspaths[agent.getId()] == []:
                    # if agent.getId()%3==0:
                    #     agentlist=self.danielsort(characters.edegesValues,agent.src,agent.speed)
                    # elif agent.getId()%3==1:
                    #     agentlist=self.sortByPaths(characters.edegesValues,agent.src,agent.speed)
                    # elif agent.getId() % 3 == 2:
                    #     agentlist = self.sortByPaths(characters.edegesValues,agent.src,agent.speed)
                    if lonlyagent:
                        agentlist = self.danielsort(characters.edegesValues, agent.src,agent.speed)
                    else:
                        agentlist = self.sortByPaths(characters.edegesValues, agent.src,agent.speed)
                    for ev in agentlist:
                        if self.isAgentSent[ev[0]] == False:
                            ps, pd = ev[0]
                            d, l = self.graph_algo.shortest_path(agent.src, ps)
                            l.insert(0, pd)
                            characters.agentspaths[agent.getId()] = l
                            self.isAgentSent[ev[0]] = True
                            break

                if characters.agentspaths[agent.getId()] == []:
                    characters.agentspaths[agent.getId()] = [agent.src]


                next_node = characters.agentspaths[agent.getId()].pop()
                self.isAgentSent[agent.src, next_node] = False
                client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')



    def save_log(self,level):
        file_name=f"logs/level_{level}_Log"
        with open(file_name+ ".txt", "w") as f:
            f.write(self.gamelog)
        print(file_name,"saved.")
        return True





