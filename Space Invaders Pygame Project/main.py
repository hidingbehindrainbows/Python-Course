#TODO clean up code later
import math
import pygame
import random

def get_random(x,y):
    return random.randint(x,y)


def player(x, y):  # X and Y determine the position of the player_img, not it's size
    mainwindow.blit(player_img , (x,y)) # drawing the image of our player onto the mainwindow


def get_enemy(enemy, x,y):
    mainwindow.blit(enemy, (x,y))
    # return (x,y)
    return


def attack(x,y):
    global bullet_state
    bullet_state = False
    mainwindow.blit(bullet_img, (x + 16,y + 10))


def isCollision(index, x1, y1, x2, y2):
    distance =  math.sqrt((math.pow(x1-x2, 2)) + (math.pow(y1-y2, 2)))
    if distance < 27:
        global player_score, enemy_X, enemy_Y
        enemy_X[index] = get_random(0,736)
        enemy_Y[index] = get_random(0,150)
        player_score +=1
        # print("Enemy destroyed")
        respawn[index] = False
        # get_enemy(enemy_X, enemy_Y)
        return True
    return False
    
    # OR USE BUILT IN FUNCTION, WHICH IS ALWAYS BETTER NOT ABLE TO FIND ANY RN 
    
def show_score():
    score = font.render(f"Score: {player_score}", True, (255, 255, 255))
    mainwindow.blit(score, (10,10)) # showing the score at 10 pixels in x and y axis

pygame.init()
#                                     width, height
mainwindow = pygame.display.set_mode(( 800,  600))  # Always add the second parenthesis

# The title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("C:\\mycode\\python\PyGame\\Space Invaders\\black-cat.png")
pygame.display.set_icon(icon)

# background:
background = pygame.image.load("C:\\mycode\\python\\PyGame\\Space Invaders\\background.png")

# backgroun music:
background_music = pygame.mixer.music.load("C:\\mycode\\python\\PyGame\\Space Invaders\\background.wav")
pygame.mixer.music.play(-1)

# Player
player_img = pygame.image.load("C:\\mycode\\python\\PyGame\\Space Invaders\\player.png")
playerX = 370
# playerY = 480
playerX_change = 0

# Player Score
player_score = 0
font = pygame.font.Font("freesansbold.ttf", 32)


# The Enemy Type 1:
enemy_img = []
enemy_X = []
enemy_Y = []
enemy_X_change = []
enemy_num = 6
respawn = [True] * enemy_num
# enemy_img = pygame.image.load("C:\\mycode\\python\\PyGame\\Space Invaders\\enemy.png")
for i in range(enemy_num):
    # get_enemy(enemy_img)
    enemy_img.append(pygame.image.load("C:\\mycode\\python\\PyGame\\Space Invaders\\enemy1.png"))
    enemy_X.append(get_random(0,736))
    enemy_Y.append(get_random(0,150))
    enemy_X_change.append(2)
# enemy_Y_change = 30

# Bullet:
bullet_img = pygame.image.load("C:\\mycode\\python\\PyGame\\Space Invaders\\bullet.png")
bullet_x = playerX
bullet_y = 480
button_y_change = 10
# bullet_state we're gonna use it to see whether we can fire or not. If the bullet is not visible, we can fire it, if it is visible, we can't
# bullet_state is True when you can't see the bullet and False when you can see it
bullet_state = True
collision = False
running = True
# Game Loop
while running:
# since we want the screen to be whatever colour we need all the time, we need to put it inside the while loop
    # initializing the backgroun
    mainwindow.blit(background, (0,0))
    # playerX += .1
    for event in pygame.event.get():
        # check if the user wants to exit
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed, check whether it is right, left, up or down
        if event.type == pygame.KEYDOWN:
            # the print statements added to check
            if event.key == pygame.K_LEFT:
                # print("Left arrow key is pressed")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = +5
                # print("Right arrow key is pressed")
            if event.key == pygame.K_SPACE:    
                if bullet_state:
                    bullet_sound = pygame.mixer.Sound("C:\\mycode\\python\\PyGame\\Space Invaders\\laser.wav")
                    bullet_sound.play()
                    bullet_x = playerX
                    attack(bullet_x, bullet_y)
                # attack_button = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                # print("Key has been released")
                playerX_change =  playerY_change = 0

    # changing player and enemy postion
    if any(respawn) and 440 not in enemy_Y:
        playerX += playerX_change
        
        # checking boundaries and making sure neither the player nor the enemy go out of bounds
        # player
        if playerX < 0:
            playerX = 0
        elif playerX > 736:
            playerX = 736  # width of the screen - the size of the image
        for i in range(enemy_num):
            if not 0<=enemy_X[i] <= 736:
                enemy_X_change[i] = -enemy_X_change[i]
                enemy_Y[i] += 30
                if enemy_X[i] < 0:
                    enemy_X_change[i] += .3
                elif enemy_X[i] > 736:
                    enemy_X_change[i] -= .3
            if enemy_Y[i] < 440 and respawn[i]:
                get_enemy(enemy_img[i], enemy_X[i], enemy_Y[i])
                enemy_X[i] += enemy_X_change[i]

            if enemy_Y[i] >=440:
                player_score = "You lost, you loser!!!!!"
                enemy_Y[i] = 440
                break

            if not bullet_state:
                collision = isCollision(i, enemy_X[i], enemy_Y[i], bullet_x, bullet_y)    
                if bullet_y < 0 or collision:
                    collision_sound = pygame.mixer.Sound("C:\\mycode\\python\\PyGame\\Space Invaders\\explosion.wav")
                    collision_sound.play()
                    bullet_y = 480
                    bullet_state = True

        # bullet movement
        if not bullet_state:
            bullet_y -= 7.5
            attack(bullet_x, bullet_y)

    if not any(respawn):
        player_score = "You won"
    
    player(playerX, 480) # y position never changes
    show_score()
    pygame.display.update()
