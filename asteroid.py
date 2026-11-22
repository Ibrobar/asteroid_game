from circleshape import *
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    def split(self) -> bool:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return True
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            pos_angle = self.velocity.rotate(random_angle)
            neg_angle = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            #self.velocity = pygame.Vector2(self.position.x, self.position.y).rotate(random_angle)
            #negative_angle = pygame.Vector2(self.position.x, self.position.y).rotate(-random_angle)
            
            asteroid_1.velocity = pos_angle * 1.2
            asteroid_2.velocity = neg_angle * 1.2
            return False
            #Asteroid(self.position.x, self.position.y, new_radius).velocity(pos_angle) * 1.2
            #asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius).velocity(negative_angle) * 1.2