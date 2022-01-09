import json
import subprocess
import sys
import threading
import time as ti
import pygame
from pygame import *
from pygame import gfxdraw
from Characters import Characters
from GameAlgo import GameAlgo
from GraphAlgo import GraphAlgo
from ImagesManager import ImagesLoader
from client import Client

#counter=0
if len(sys.argv) > 1:
    try:
        subprocess.Popen(["powershell.exe", "java -jar Ex4_Server_v0.0.jar", sys.argv[1]])
    except("ERR"):
        print("The server is already running")
else:
    try:
        subprocess.Popen(["powershell.exe", "java -jar Ex4_Server_v0.0.jar 0"])
    except("ERR"):
        print("The server is already running")

# default port
PORT = 6666

# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

# init pygame
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
radius = 15

#Set screen
screen = display.set_mode((1000, 800), depth=32, flags=RESIZABLE)

#Load images
imageCollection=ImagesLoader(screen.get_width(), screen.get_height())

#Count down
try:
    mixer.music.load("music/3-2-1.mp3")
    mixer.music.play()
except:
    print("no sound")
for i in range(4):
    screen.blit(imageCollection.countdownImages[3-i], (0, 0))
    display.update()
    ti.sleep(1)

#choose Background Image
backnum=1
background_image=imageCollection.background_images[backnum]
screen.blit(background_image, (0, 0))

#start playing background music
try:
    mixer.init()
    mixer.music.load("music/PokemonIntroSaliEx4.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
except:
    print("no music")

#colors
crimson=(184,15,10)
white=(255, 255, 255)
blue=(64, 80, 174)

#Set stop button
stop = FONT.render('stop game', True, crimson)

#Init Client
client = Client()
client.start_connection(HOST, PORT)

#Init Graph Algorithm
graph_algo= GraphAlgo()
graph_algo.load_from_json(client.get_graph())

#Init Game Algorithm
game_algo=GameAlgo(graph_algo)

#Init Characters
characters=Characters()

#Load Pokemons to Chatacters
characters.load_Pokemons_from_json(client.get_pokemons(), graph_algo.get_graph())

#add agents to client
str1="{\"id\":"
str2="}"
for i in range(int(json.loads(client.get_info())["GameServer"]["agents"])):
    if i<len(characters.edegesValues):
        client.add_agent(f"{str1}{characters.edegesValues[i][0][0]}{str2}")
    else:
        client.add_agent(f"{str1}{characters.edegesValues[0][0][0]}{str2}")

#Load Agents to Chatacters
c=client.get_agents()
characters.load_Agents_from_json(c)
for ag in characters.agents:
    characters.agentspaths[ag.getId()] = []

# get data proportions
min_x = sys.float_info.max
min_y = sys.float_info.max
max_x = sys.float_info.min
max_y = sys.float_info.min
for n in graph_algo.graph.get_all_v().values():
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

# this commnad starts the server - the game is running now
client.start()
flag=False
sc=0

# def moveThread():
#     while client.is_running() == 'true':
#         print("move")
#         # move agents
#         ti.sleep(0.1)
#
#         client.move()

# t1=threading.Thread(target=moveThread())
# t1.start()
# t1.join()


while client.is_running() == 'true':
    #Update BackGround images
    imageCollection.loadBackGrounds(screen.get_width(),screen.get_height())
    background_image = imageCollection.background_images[backnum]
    screen.blit(background_image, (0, 0))
    characters.load_Agents_from_json(client.get_agents())
    if flag:
        characters.load_Pokemons_from_json(client.get_pokemons(), graph_algo.get_graph())
    flag=True

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 432 <= mouse[0] <= 432 + 140 and 7 <= mouse[1] <= 30:
                screen.blit(imageCollection.stopgameIM, (0, 0))
                try:
                    mixer.music.load("music/Bye Bye Bye Sound Effect.mp3")
                    mixer.music.play()
                except:
                    print("no sound")
                display.update()
                ti.sleep(1)
                client.stop()
                client.stop_connection()
                print(f"You stopped the game with {score} points.")
                sys.exit()
    mouse = pygame.mouse.get_pos()

    # score, time to end, move counter.

    # level
    info = json.loads(client.get_info())
    level = info.get("GameServer")["game_level"]
    levelabel = FONT.render(f"Level: {level}", True, crimson)
    rect = levelabel.get_rect(center=(50, 10))
    screen.blit(levelabel, rect)

    # time
    timeleft = float(client.time_to_end()) / 1000
    timelabel = FONT.render(f"Time Left: {int(timeleft)}", True, crimson)
    rect = timelabel.get_rect(center=(150, 10))
    screen.blit(timelabel, rect)

    # score
    info = json.loads(client.get_info())
    score = info.get("GameServer")["grade"]
    if sc<score:
        print(f"+{score-sc} total: {score}")
        sc=score
    scorelabel = FONT.render(f"Score: {score}", True, crimson)
    rect = scorelabel.get_rect(center=(250, 10))
    screen.blit(scorelabel, rect)

    # moves
    moves = info.get("GameServer")["moves"]
    moveslabel = FONT.render(f"Moves: {moves}", True, crimson)
    rect = moveslabel.get_rect(center=(350, 10))
    screen.blit(moveslabel, rect)

    # stop game button
    if 450 <= mouse[0] <= 432 + 100 and 7 <= mouse[1] <= 30:
        pygame.draw.rect(screen, white, [450, 7, 85, 20])
        screen.blit(stop, (400 + 50, 1))
    else:
        # superimposing the text onto our button
        screen.blit(stop, (400 + 50, 1))

    # draw agents
    for agent in characters.agents:
        X, Y, Z = agent.getLocation()
        x = my_scale(X, x=True)
        y = my_scale(Y, y=True)
        screen.blit(imageCollection.agentsImages[agent.getId()%3], (int(x), int(y)))
        # draw edges
        for n in graph_algo.get_graph().get_all_v().values():
            for e in graph_algo.get_graph().all_out_edges_of_node(n.id).keys():
                # find the edge nodes
                src = n.id
                dest = e

                # scaled positions
                sx, sy, sz = graph_algo.graph.get_all_v()[src].getLocation()
                dx, dy, dz = graph_algo.graph.get_all_v()[dest].getLocation()
                src_x = my_scale(sx, x=True)
                src_y = my_scale(sy, y=True)
                dest_x =my_scale(dx, x=True)
                dest_y =my_scale(dy, y=True)

                # draw the line
                pygame.draw.line(screen, (61, 72, 126), (src_x, src_y), (dest_x, dest_y))

        # draw nodes
        for n in graph_algo.get_graph().get_all_v().values():
            X, Y, Z = n.getLocation()
            x = my_scale(X, x=True)
            y = my_scale(Y, y=True)
            # its just to get a nice antialiased circle
            # gfxdraw.filled_circle(screen, int(x), int(y),radius, blue)
            gfxdraw.aacircle(screen, int(x), int(y), radius, blue)

            # draw the node id
            id_srf = FONT.render(str(n.id), True, white)
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)

    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in characters.pokemons:
        X, Y, Z = p.getLocation()
        x = my_scale(X, x=True)
        y = my_scale(Y, y=True)
        if (p.value % 15) == 0:
            screen.blit(imageCollection.pokImages[15], (int(x), int(y)))
        elif (p.value % 15) > 5:
            screen.blit(imageCollection.pokImages[p.value % 15], (int(x), int(y)))
        else:
            screen.blit(imageCollection.pokImages[5], (int(x), int(y)))
    # update screen changes
    display.update()

    # refresh rate
    clock.tick(10)
    game_algo.choose_next_edge(characters,client)

    # #move agents
    client.move()

# game over:
print(f"You have finished the game with {score} points and {moves} moves.")
screen.blit(imageCollection.finishgameIM, (0, 0))
try:
    mixer.music.load("music/PikachuSound.mp3")
    mixer.music.play()
except:
    print("no sound")
display.update()
ti.sleep(3)
sys.exit()
