import json


class GameAlgo:
    def __init__(self,graph_algo):
        self.graph_algo=graph_algo
        self.isAgentSent = {}
        for s in graph_algo.get_graph().get_all_v().keys():
            for d in graph_algo.get_graph().all_out_edges_of_node(s):
                self.isAgentSent[(s, d)] = False

    def syncValuesWithShorterPath(self,edegesValues:list,src:int,dest:int):
        newlist=[]
        #print("before",edegesValues)
        for i in range(len(edegesValues)):
            e,v=edegesValues[i]
            d, l = self.graph_algo.shortest_path(src, e[0])
           # print(l,self.graph_algo.get_graph().all_out_edges_of_node(e[0]),e)
            d=d+self.graph_algo.get_graph().all_out_edges_of_node(e[0])[e[1]]
            # d=d/speed
            # if len(l)<2:
            #     v=v+999
            # else:
            if d!=0:
                v=v/d
            newlist.append((e,v))
        newlist.sort(key=lambda x:x[1])
        newlist.reverse()
        #print("after", newlist)
        return newlist


    def choose_next_edge(self,characters,client)->tuple:
        for agent in characters.agents:
           # print(agent.value)
            if agent.dest == -1:
                if characters.agentspaths[agent.getId()] == []:
                    syncedlist=self.syncValuesWithShorterPath(characters.edegesValues,agent.getId(),agent.dest)
                    for ev in syncedlist:
                    #for ev in characters.edegesValues:
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




