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

    #actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)

    #recupere les projectiles dui joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # appliquer l'ensemble des images de mon groupe de projectile
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des images de mon groupes de monstres
    game.all_monsters.draw(screen)

    #verifier si le joueur souhaite aller a fauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    #mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evement fermeteure de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

