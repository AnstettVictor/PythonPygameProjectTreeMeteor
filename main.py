import pygame

from game import Game
pygame.init()

#generer le fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))


# importer le background
background = pygame.image.load('assets/bg.jpg')

#charger notre jeu

game = Game()

running = True

#boucle tant que condition vrai
while running:

    #appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    #appliquer l'image de monjoueur
    screen.blit(game.player.image, game.player.rect)

    #mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evement fermeteure de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
