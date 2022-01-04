"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import os.path
import sys

from types import SimpleNamespace

from pygame.draw import circle

from Characters import Characters
from GraphAlgo import GraphAlgo
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
import subprocess

#run server
subprocess.Popen(["powershell.exe","java -jar Ex4_Server_v0.0.jar 4"])
# init pygame
WIDTH, HEIGHT = 1920, 800
# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

screen = display.set_mode((1080, 800), depth=32, flags=RESIZABLE)

background_image = pygame.image.load("images/background.jpg").convert()
backmusic = 'music/intro.mp3'
pygame.mixer.init()
# pygame.mixer.music.load(backmusic)
# pygame.mixer.music.play()

clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

# pokemons = client.get_pokemons()
# pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))


# load the json string into SimpleNamespace Object
algo= GraphAlgo()
algo.load_from_json(client.get_graph())
characters=Characters()


#load images

rattataIM = pygame.image.load(os.path.join('images','rattata.jpg'))
rattataIM = pygame.transform.scale(rattataIM,(70,70))

koffingIM = pygame.image.load(os.path.join('images','koffing.jpg'))
koffingIM = pygame.transform.scale(koffingIM,(70,70))

psyduckIM = pygame.image.load(os.path.join('images','psyduck.jpg'))
psyduckIM = pygame.transform.scale(psyduckIM,(70,70))

squirtleIM = pygame.image.load(os.path.join('images','squirtle.jpg'))
squirtleIM = pygame.transform.scale(squirtleIM,(70,70))

jigglupuffIM = pygame.image.load(os.path.join('images','jigglupuff.jpg'))
jigglupuffIM = pygame.transform.scale(jigglupuffIM,(70,70))

alakazamIM = pygame.image.load(os.path.join('images','alakazam.jpg'))
alakazamIM = pygame.transform.scale(alakazamIM,(70,70))

bulbasaurIM = pygame.image.load(os.path.join('images','bulbasaur.jpg'))
bulbasaurIM = pygame.transform.scale(bulbasaurIM,(70,70))

charizardIM = pygame.image.load(os.path.join('images','charizard.jpg'))
charizardIM = pygame.transform.scale(charizardIM,(70,70))

pikacuIM = pygame.image.load(os.path.join('images','pikachu.jpg'))
pikacuIM = pygame.transform.scale(pikacuIM,(70,70))

kyorgeIM = pygame.image.load(os.path.join('images','kyorge.jpg'))
kyorgeIM = pygame.transform.scale(kyorgeIM,(70,70))

mewtwoIM = pygame.image.load(os.path.join('images','mewtwo.jpg'))
mewtwoIM = pygame.transform.scale(mewtwoIM,(70,70))

ashIM = pygame.image.load(os.path.join('images','ash.jpg'))
ashIM = pygame.transform.scale(ashIM,(40,80))

background_image=pygame.image.load(os.path.join('images','background1.jpg'))
background_image= pygame.transform.scale(background_image,(WIDTH,HEIGHT))


FONT = pygame.font.SysFont('Arial', 20, bold=True)


 # get data proportions
min_x = sys.float_info.max
min_y = sys.float_info.max
max_x = sys.float_info.min
max_y = sys.float_info.min
for n in algo.graph.get_all_v().values():
    x,y,z= n.getLocation()
    if min_x>x:
        min_x=x
    if min_y>y:
        min_y=y
    if max_x<x:
        max_x=x
    if max_y<y:
        max_y=y


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)


radius = 15

client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

# this commnad starts the server - the game is running now
client.start()
characters.load_Agents_from_json(client.get_agents())
characters.load_Pokemons_from_json(client.get_pokemons())
print(characters.pokemons)

#start playing background music
mixer.init()
mixer.music.load("music/PokemonIntroSaliEx4.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""

while client.is_running() == 'true':
    ship_top = screen.get_height() -HEIGHT
    ship_left = screen.get_width() - WIDTH
    screen.blit(background_image, (ship_left, ship_top))



    characters.load_Agents_from_json(client.get_agents())
    characters.load_Pokemons_from_json(client.get_pokemons())



    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(Color(0,0,0))
    screen.blit(background_image, (ship_left, ship_top))
    # score, time to end, move counter.

    #time
    timeleft = float(client.time_to_end()) / 1000
    timelabel = FONT.render(f"Time Left: {int(timeleft)}", True, Color(70, 70, 90))
    rect = timelabel.get_rect(center=(70, 10))
    screen.blit(timelabel, rect)

    #score
    info = json.loads(client.get_info())
    score = info.get("GameServer")["grade"]
    scorelabel = FONT.render(f"Score: {score}", True, Color(70, 70, 90))
    rect = scorelabel.get_rect(center=(200, 10))
    screen.blit(scorelabel, rect)
    #moves
    moves = info.get("GameServer")["moves"]
    moveslabel = FONT.render(f"Moves: {moves}", True, Color(70, 70, 90))
    rect = moveslabel.get_rect(center=(300, 10))
    screen.blit(moveslabel, rect)

    # draw nodes
    for n in algo.get_graph().get_all_v().values():
        X,Y,Z=n.getLocation()
        x = my_scale(X, x=True)
        y = my_scale(Y, y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)
        # draw edges
        for e in algo.get_graph().all_out_edges_of_node(n.id).keys():
            # find the edge nodes
            src = n.id
            dest = e

            # scaled positions
            sx,sy,sz=algo.graph.get_all_v()[src].getLocation()
            dx, dy, dz = algo.graph.get_all_v()[dest].getLocation()
            src_x = my_scale(sx, x=True)
            src_y = my_scale(sy, y=True)
            dest_x = my_scale(dx, x=True)
            dest_y = my_scale(dy, y=True)

            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126),
                             (src_x, src_y), (dest_x, dest_y))



    # draw agents
    for agent in characters.agents:
        X, Y, Z = agent.getLocation()
        x = my_scale(X, x=True)
        y = my_scale(Y, y=True)
        screen.blit(ashIM, (int(x), int(y)))
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in characters.pokemons:
        X, Y, Z = p.getLocation()
        x = my_scale(X, x=True)
        y = my_scale(Y, y=True)
        if (p.value%15)<6 and (p.value%15)>0:
            screen.blit(rattataIM,(int(x), int(y)))
        elif (p.value%15)==6:
            screen.blit(koffingIM,(int(x), int(y)))
        elif (p.value%15)==7:
            screen.blit(psyduckIM,(int(x), int(y)))
        elif (p.value%15)==8:
            screen.blit(squirtleIM,(int(x), int(y)))
        elif (p.value%15)==9:
            screen.blit(jigglupuffIM,(int(x), int(y)))
        elif (p.value%15)==10:
            screen.blit(alakazamIM,(int(x), int(y)))
        elif (p.value%15)==11:
            screen.blit(bulbasaurIM,(int(x), int(y)))
        elif (p.value%15)==12:
            screen.blit(charizardIM,(int(x), int(y)))
        elif (p.value%15)==13:
            screen.blit(pikacuIM,(int(x), int(y)))
        elif (p.value%15)==14:
            screen.blit(kyorgeIM,(int(x), int(y)))
        else:
            screen.blit(mewtwoIM,(int(x), int(y)))




    # update screen changes
    display.update()
    # refresh rate
    clock.tick(60)


    # choose next edge
    for agent in characters.agents:
        if agent.dest == -1:
            next_node = (agent.src - 1) % algo.get_graph().v_size()
            client.choose_next_edge(
                '{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)+'}')
            ttl = client.time_to_end()
            print(ttl, client.get_info())
            print(characters.pokemons)

    client.move()
# game over: