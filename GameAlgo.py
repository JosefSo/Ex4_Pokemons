import json


class GameAlgo:
    def __init__(self,graph_algo):
        self.graph_algo=graph_algo
        self.isAgentSent = {}
        for s in graph_algo.get_graph().get_all_v().keys():
            for d in graph_algo.get_graph().all_out_edges_of_node(s):
                self.isAgentSent[(s, d)] = False

    def choose_next_edge(self,characters,client)->tuple:
        #i = 0
        for agent in characters.agents:
            if agent.dest == -1:
                if characters.agentspaths[agent.getId()] == []:
                    for ev in characters.edegesValues:
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
                #print(characters.edegesValues)
                client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
            #i = (i + 1) % len(characters.pokemons)



