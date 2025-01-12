import pygame
import random
pygame.init()


screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman Game by Alp")

pacman_image = pygame.image.load("pacman/pacman.png")
pacman_image = pygame.transform.scale(pacman_image, (40,40))
class Pacman():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.radius = 20

    def draw(self):
        # pygame.draw.circle(screen, "yellow", (self.x, self.y), self.radius)
        screen.blit(pacman_image, (self.x - 20, self.y - 20))

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= 1
        if keys[pygame.K_DOWN]:
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.x -= 1
        if keys[pygame.K_RIGHT]:
            self.x += 1

class Food():
    def __init__(self):
        self.x = random.randint(20, 580)
        self.y = random.randint(20, 380)
        self.radius = 10

    def draw(self):
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)


def main():
    run = True
    pacman = Pacman(300, 200)
    food = Food()
    score = 0

    while run:
        screen.fill("black")

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        
        keys = pygame.key.get_pressed()
        pacman.move(keys)
        distance = ((pacman.x - food.x) ** 2 + (pacman.y - food.y) ** 2) ** 0.5
        if distance < pacman.radius + food.radius:
            food = Food()
            score = score + 1
        pacman.draw()
        food.draw()
        
        font = pygame.font.SysFont("Arial", 40)
        scoretext = font.render("Score: " +str(score), True, (255,255,255))
        screen.blit(scoretext, (50, 350))

        pygame.display.update()

main()


