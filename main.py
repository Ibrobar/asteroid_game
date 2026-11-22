import pygame
from player import *
from constants import *
from logger import log_state, log_event
import player
from asteroid import *
import asteroid 
from asteroidfield import *
from circleshape import *
import sys
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    field = AsteroidField()
    ship = player.Player(x, y)
    #asteroid = asteroid.Asteroid
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
    
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        # print(dt)

if __name__ == "__main__":
    main()
