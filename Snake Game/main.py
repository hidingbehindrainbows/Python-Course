import pygame
import random
import tkinter
from tkinter import messagebox


class Cube(object):
    rows = 20
    width = 600

    def __init__(self, start,colour = (255,0,0)):
        self.pos = start
        self.cubeX = 1
        self.cubeY = 0
        self.colour = colour

    def move(self, cubeX, cubeY):
        self.cubeX = cubeX
        self.cubeY = cubeY
        self.pos = (self.pos[0] + self.cubeX, self.pos[1] + self.cubeY) # since we're not using pixels, and instead rows, and columns, we have to do this

    def draw(self, surface ,eye = False):
        dis = self.width // self.rows
        i = self.pos[0] # i is row
        j = self.pos[1] # j is column
        w = i*dis +1
        h = j*dis+1
        rectangle = (w, h, dis-2, dis-2)
        pygame.draw.rect(surface, self.colour, rectangle)
        if eye:
            centre = dis // 2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


class Snake(object):
    body = []
    turns = {}
    def __init__(self, colour, pos):
        self.colour = colour
        self.cubeX = 1
        self.cubeY = 0
        self.head = Cube(pos)
        self.body.append(self.head)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.cubeX = -1
                    self.cubeY = 0
                    self.turns[self.head.pos[:]] = [self.cubeX, self.cubeY]
                elif event.key == pygame.K_RIGHT:
                    self.cubeX = 1
                    self.cubeY = 0
                    self.turns[self.head.pos[:]] = [self.cubeX, self.cubeY]

                elif event.key ==pygame.K_UP:
                    self.cubeX = 0
                    self.cubeY = -1
                    self.turns[self.head.pos[:]] = [self.cubeX, self.cubeY]

                elif event.key ==pygame.K_DOWN:
                    self.cubeX = 0
                    self.cubeY = 1
                    self.turns[self.head.pos[:]] = [self.cubeX, self.cubeY]

        for index, cube in enumerate(self.body):
            p = cube.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                cube.move(turn[0],turn[1])
                if index == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if cube.cubeX == -1 and cube.pos[0] <= 0: 
                    cube.pos = (cube.rows-1, cube.pos[1])
                elif cube.cubeX == 1 and cube.pos[0] >= cube.rows-1: 
                    cube.pos = (0,cube.pos[1])
                elif cube.cubeY == 1 and cube.pos[1] >= cube.rows-1: 
                    cube.pos = (cube.pos[0], 0)
                elif cube.cubeY == -1 and cube.pos[1] <= 0: 
                    cube.pos = (cube.pos[0],cube.rows-1)
                else: 
                    cube.move(cube.cubeX,cube.cubeY)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.cubeX = 1
        self.cubeY = 0 

    def add_cube(self):
        tail = self.body[-1]
        x, y = tail.cubeX, tail.cubeY
        if x == 1 and y == 0:  # checking which direction the tail of our player is moving in
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        if x == -1 and y == 0:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        if x == 0 and y == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        if x == 0 and y == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))
        self.body[-1].cubeX = x
        self.body[-1].cubeY = y
    
    def draw(self, surface):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(surface, True) # adding the eye so that we know to differentiate front and back in the snake
            else:
                cube.draw(surface)


def draw_grid(surface):
    global rows
    size_of_x_boxes = 600 // rows
    x = y = 0
    for _ in range(rows):
        x += size_of_x_boxes
        y += size_of_x_boxes
        pygame.draw.line(surface, (255,255,255), (x,0), (x,600))
        pygame.draw.line(surface, (255,255,255), (0,y), (600,y))


def redraw_window(surface):
    global player, apple
    surface.fill((0,0,0))
    draw_grid(surface)
    apple.draw(surface)
    player.draw(surface)
    pygame.display.update()


def random_apple(item):
    global rows
    positions = item.body
    
    while True:
        x = random.randrange(rows)
        y =  random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:  # making sure the positions of the snake and apple don't coincide
            continue
        else:
            break
    return (x,y)


def message_box(subject, content):
    message = tkinter.Tk()
    message.attributes("-topmost",True)
    message.withdraw()
    messagebox.showinfo(subject, content)
    try:
        message.destroy()  # this isn't a good idea, but oh well
    except:
        pass

pygame.init()
mainwindow = pygame.display.set_mode((600, 600))
rows = 20
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("C:\\mycode\\python\\PyGame\\Snake game\\anaconda.png")
pygame.display.set_icon(icon)

# the player
player = Snake((255,0,0),(10,10))

# the apple
apple = Cube(random_apple(player), colour=(0,255,0))

# clock object
clock = pygame.time.Clock()

while True:
    pygame.time.delay(50)
    clock.tick(10)
    player.move()
    if player.body[0].pos == apple.pos:
        player.add_cube()
        apple = Cube(random_apple(player), colour=(0,255,0))
        
    for x in range(len(player.body)):
        if player.body[x].pos in list(map(lambda z:z.pos, player.body[x+1:])):
            message_box("You lost!", f"Do you want to play again? \nScore={len(player.body)}")
            player.reset((10,10))
            break
        
    redraw_window(mainwindow)
