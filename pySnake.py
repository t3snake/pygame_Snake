import pygame
import random

fps=int(input("Enter FPS: "))
# screen set
scr = pygame.display.set_mode((800, 600))
pygame.display.set_caption("T3's Snake")
pygame.display.flip()
scr.fill((255, 255, 200))
x = random.randint(10, 40)
y = random.randint(10, 30)
clock = pygame.time.Clock()

# initial snake position and velocity
snake = [(x, y), (x + 1, y), (x + 2, y), (x + 3, y), (x + 4, y)]
foodx,foody=(0,0)
lt,rt,up,dn = (-1, 0),(1, 0),(0, -1),(0, 1)
veloc = rt


# functions
def draw():
    # draw border padding 10
    pygame.draw.rect(scr, (0,0,0), (10,10,780,580), 2)

    # draw food
    pygame.draw.circle(scr, (100, 100, 0), (foodx * 10 + 5,foody * 10 + 5), 5)

    # draw snake
    for z in snake:
        pygame.draw.rect(scr, (0, 0, 0), (z[0] * 10, z[1] * 10, 10, 10), 0)


def food():
    c=0
    while c==0:
        x = random.randint(2, 78)
        y = random.randint(2, 58)
        if (x,y) not in snake:
            c=1
    return x,y


def upd():
    snake.pop(0)  # temp for food collision
    new = snake[-1]  # last block = head

    # boundary conditions
    if new[0]>=78 and veloc is rt:
        new = 0,new[1]
    if new[1]>=58 and veloc is dn:
        new = new[0],0
    if new[0]<=1 and veloc is lt:
        new = 79,new[1]
    if new[1]<=1 and veloc is up:
        new = new[0],59

    new = new[0]+veloc[0],new[1]+veloc[1]  # add velocity per unit time(displacement) to the head block
    if new in snake:
        print("Snek is ded by suside.")
        pygame.quit()
        quit()
    snake.append(new)



i=0
foodx,foody = food()
# 1 step per loop
while True:
    clock.tick(fps)
    scr.fill((100, 100, 200))
    draw()
    if (foodx,foody) in snake:
        foodx,foody = food()
        i+=1
        snake.insert(0,snake[1])
    pygame.display.flip()
    upd()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # kb hit detection
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and veloc != up:
                veloc=dn
            if event.key == pygame.K_UP and veloc != dn:
                veloc=up
            if event.key == pygame.K_LEFT and veloc != rt:
                veloc=lt
            if event.key == pygame.K_RIGHT and veloc != lt:
                veloc=rt
    i+=1
