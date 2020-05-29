import pygame
from player import Player
from monster import Monster
#cree une seconde class qui va representer notre jeu
class Game:

    def __init__(self):
        # definir si notre jeu a commencé ou non
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
    def game_over(self):
        #remettre le jeu a neuf, retirer les monstres , remettre le joueur a 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
         # appliquer l'image de monjoueur
         screen.blit(self.player.image, self.player.rect)

         # actualiser la barre de vie du joueur
         self.player.update_health_bar(screen)

         # recupere les projectiles dui joueur
         for projectile in self.player.all_projectiles:
             projectile.move()

         # recuperer les monstres de notre jeu
         for monster in self.all_monsters:
             monster.forward()
             monster.update_health_bar(screen)

         # appliquer l'ensemble des images de mon groupe de projectile
         self.player.all_projectiles.draw(screen)

         # appliquer l'ensemble des images de mon groupes de monstres
         self.all_monsters.draw(screen)

         # verifier si le joueur souhaite aller a fauche ou a droite
         if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
             self.player.move_right()
         elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)