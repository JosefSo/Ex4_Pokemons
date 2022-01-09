import os

import pygame

class ImagesLoader:
    def __init__ (self,WIDTH:float,HEIGHT:float):
        # load images
        self.background_images ={}
        self.pokImages = {}
        self.agentsImages ={}
        self.countdownImages={}
        self.loadBackGrounds(WIDTH,HEIGHT)

        rattataIM = pygame.image.load(os.path.join('images', 'rattata.jpg'))
        rattataIM = pygame.transform.scale(rattataIM, (70, 70))
        self.pokImages[5]=rattataIM

        koffingIM = pygame.image.load(os.path.join('images', 'koffing.jpg'))
        koffingIM = pygame.transform.scale(koffingIM, (70, 70))
        self.pokImages[6] = koffingIM

        psyduckIM = pygame.image.load(os.path.join('images', 'psyduck.jpg'))
        psyduckIM = pygame.transform.scale(psyduckIM, (70, 70))
        self.pokImages[7] = psyduckIM

        squirtleIM = pygame.image.load(os.path.join('images', 'squirtle.jpg'))
        squirtleIM = pygame.transform.scale(squirtleIM, (70, 70))
        self.pokImages[8] = squirtleIM

        jigglupuffIM = pygame.image.load(os.path.join('images', 'jigglupuff.jpg'))
        jigglupuffIM = pygame.transform.scale(jigglupuffIM, (70, 70))
        self.pokImages[9] = jigglupuffIM

        alakazamIM = pygame.image.load(os.path.join('images', 'alakazam.jpg'))
        alakazamIM = pygame.transform.scale(alakazamIM, (70, 70))
        self.pokImages[10] = alakazamIM

        bulbasaurIM = pygame.image.load(os.path.join('images', 'bulbasaur.jpg'))
        bulbasaurIM = pygame.transform.scale(bulbasaurIM, (70, 70))
        self.pokImages[11] = bulbasaurIM

        charizardIM = pygame.image.load(os.path.join('images', 'charizard.jpg'))
        charizardIM = pygame.transform.scale(charizardIM, (70, 70))
        self.pokImages[12] = charizardIM

        pikacuIM = pygame.image.load(os.path.join('images', 'pikachu.jpg'))
        pikacuIM = pygame.transform.scale(pikacuIM, (70, 70))
        self.pokImages[13] = pikacuIM

        kyorgeIM = pygame.image.load(os.path.join('images', 'kyorge.jpg'))
        kyorgeIM = pygame.transform.scale(kyorgeIM, (70, 70))
        self.pokImages[14] = kyorgeIM

        mewtwoIM = pygame.image.load(os.path.join('images', 'mewtwo.jpg'))
        mewtwoIM = pygame.transform.scale(mewtwoIM, (70, 70))
        self.pokImages[15] = mewtwoIM

        ashIM = pygame.image.load(os.path.join('images', 'ash.jpg'))
        ashIM = pygame.transform.scale(ashIM, (40, 80))
        self.agentsImages[0]=ashIM

        brookIM = pygame.image.load(os.path.join('images', 'brook.jpg'))
        brookIM = pygame.transform.scale(brookIM, (40, 80))
        self.agentsImages[1]=brookIM

        mistyIM = pygame.image.load(os.path.join('images', 'misty.jpg'))
        mistyIM = pygame.transform.scale(mistyIM, (40, 80))
        self.agentsImages[2]=mistyIM

        self.countdownImages[3] = pygame.image.load(os.path.join('images', '3-Countdown-Photo-Strip.jpg'))
        self.countdownImages[3] = pygame.transform.scale(self.countdownImages[3], (WIDTH, HEIGHT))

        self.countdownImages[2] = pygame.image.load(os.path.join('images', '2-Countdown-Photo-Strip.jpg'))
        self.countdownImages[2] = pygame.transform.scale(self.countdownImages[2], (WIDTH, HEIGHT))

        self.countdownImages[1] = pygame.image.load(os.path.join('images', '1-Countdown-Photo-Strip.jpg'))
        self.countdownImages[1] = pygame.transform.scale(self.countdownImages[1], (WIDTH, HEIGHT))

        self.countdownImages[0] = pygame.image.load(os.path.join('images', 'logo.jpg'))
        self.countdownImages[0] = pygame.transform.scale(self.countdownImages[0], (WIDTH, HEIGHT))

    def loadBackGrounds(self,WIDTH,HEIGHT):

        b0 = pygame.image.load(os.path.join('images', 'background.jpg'))
        b0 = pygame.transform.scale(b0, (WIDTH, HEIGHT))
        self.background_images[0] = b0

        b1 = pygame.image.load(os.path.join('images', 'background1.jpg'))
        b1 = pygame.transform.scale(b1, (WIDTH, HEIGHT))
        self.background_images[1] = b1

        b2 = pygame.image.load(os.path.join('images', 'background2.jpg'))
        b2 = pygame.transform.scale(b2, (WIDTH, HEIGHT))
        self.background_images[2] = b2

        self.stopgameIM = pygame.image.load(os.path.join('images', 'stopgame.jpg'))
        self.stopgameIM = pygame.transform.scale(self.stopgameIM, (WIDTH, HEIGHT))

        self.finishgameIM = pygame.image.load(os.path.join('images', 'finishgame.jpg'))
        self.finishgameIM = pygame.transform.scale(self.finishgameIM, (WIDTH, HEIGHT))

