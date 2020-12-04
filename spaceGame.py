import pygame
import random
import math
from pygame import mixer
 
def start():
    # initializing the pygame module
    pygame.init()

    # creating the screen for the game(game window)
    screen = pygame.display.set_mode((800, 600))

    # Background for the game
    backgroundImg = pygame.image.load('background.png')

    # Background Sound
    mixer.music.load('backgrounds.mp3')
    mixer.music.play(-1)

    # Changing window title and icon
    pygame.display.set_caption("SpaceInvaders")
    icon = pygame.image.load('AlienUfo.png')
    pygame.display.set_icon(icon)

    # Adding the player
    playerImg = pygame.image.load('spaceship.png')

    # Setting the position of the player
    x_axis = 400
    y_axis = 500
    change_x = 0

    # Adding the enemies (multiple enemies using list)
    # Creating a list
    enemyImg = []
    X_axis = []
    Y_axis = []
    change_X = []
    change_Y = []
    number_of_enemies = 5
    for i in range(number_of_enemies):
        enemyImg.append(pygame.image.load('alien.png'))

        # Setting the position of the enemy (randomizing the movement of the enemy)
        X_axis.append(random.randint(0, 735))
        Y_axis.append(random.randint(0, 150))
        change_X.append(4)
        change_Y.append(30)

    # Adding the bullet
    bulletImg = pygame.image.load('bullet.png')

    # Setting the position of the enemy (randomizing the movement of the enemy)
    bullet_X = 0
    bullet_Y = 500
    bullet_change_X = 0
    bullet_change_Y = 5
    # In 'ready' state you cannot see the bullet on the screen
    # In 'fire' state you can see the bullet on the screen(moving)
    global bullet_state
    bullet_state = "ready"

    # Game Over text
    over = pygame.font.Font('space_age.ttf', 72)

    # Score
    score_val = 0
    font = pygame.font.Font('space_age.ttf', 32)
    # Positioning the score on the screen
    text_x = 10
    text_y = 10


    # Game over
    def game_over():
        over_game = over.render("GAME OVER", True, (200, 200, 200))
        screen.blit(over_game, (125, 250))


    # Displaying the score
    def display_score(x, y):
        # First render then blit
        score = font.render("Score: " + str(score_val), True, (200, 200, 200))
        screen.blit(score, (round(x), round(y)))


    def player(x, y):
        # Drawing the player onto the screen
        screen.blit(playerImg, (round(x), round(y)))


    def enemy(x, y, a):
        # Drawing the player onto the screen
        screen.blit(enemyImg[a], (round(x), round(y)))


    def bullet_fire(x, y):
        global bullet_state
        bullet_state = "fire"
        # To shoot the bullet from the middle of the spaceship 10 and 16 is added
        screen.blit(bulletImg, (round(x + 16), round(y + 10)))


    # Checking for collision
    def has_collided(a, b, c, d):
        # using the distance formula
        distance = math.sqrt((math.pow(a - c, 2)) + (math.pow(b - d, 2)))
        if distance < 27:
            return True
        else:
            return False


    # Making a game loop here we will include every event that has to run throughout the program

    run_while = True
    while run_while:
        # Changing background color
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(backgroundImg, (0, 0))

        # Loops through all the events happening
        for event in pygame.event.get():
            # have to click on 'X' to exit
            if event.type == pygame.QUIT:
                run_while = False

            # Keyboard input process. (To move the player left and right as the buttons are pressed on the keyboard)
            # KEYDOWN is for pressing the button on the keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -5
                if event.key == pygame.K_RIGHT:
                    change_x = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("laser.wav")
                        bullet_sound.play()
                        # Getting the X axis of the spaceship
                        bullet_X = x_axis
                        bullet_fire(bullet_X, bullet_Y)
            # KEYUP is for releasing the button on the keyboard
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change_x = 0

        # Changing the coordinates values of the player (Movement of the enemy)
        x_axis += change_x
        # Creating a boundary for the player
        if x_axis <= 0:
            x_axis = 0
        elif x_axis >= 736:
            # Considering the size of the spaceship which we have taken of 64 pixels.
            x_axis = 736

        # Enemy Movement
        for i in range(number_of_enemies):
            # Game over
            if Y_axis[i] > 440:
                # To remove the enemies from the screen
                for j in range(number_of_enemies):
                    Y_axis[j] = 2000
                game_over()
                break

            # Changing the coordinates values of the enemy
            X_axis[i] += change_X[i]
            # Creating a boundary for the enemy
            if X_axis[i] <= 0:
                change_X[i] = 4
                Y_axis[i] += change_Y[i]
            elif X_axis[i] >= 736:
                # Considering the size of the spaceship which we have taken of 64 pixels.
                change_X[i] = -4
                Y_axis[i] += change_Y[i]

            # Collision
            collision = has_collided(X_axis[i], Y_axis[i], bullet_X, bullet_Y)
            # Resetting everything is there has been a collision and awarding a point
            if collision:
                collision_sound = mixer.Sound("explosion.wav")
                collision_sound.play()
                bullet_Y = 480
                bullet_state = "ready"
                score_val += 1
                X_axis[i] = random.randint(0, 735)
                Y_axis[i] = random.randint(0, 150)
            # Calling the function to draw the enemy and providing the coordinates
            enemy(X_axis[i], Y_axis[i], i)

        # Bullet movement
        # For multiple bullets
        if bullet_Y <= 0:
            bullet_Y = 500
            bullet_state = "ready"
        # Firing the bullet
        if bullet_state == "fire":
            bullet_fire(bullet_X, bullet_Y)
            bullet_Y -= bullet_change_Y

        # Calling the function to draw the player and providing the coordinates
        player(x_axis, y_axis)
        # Score function call
        display_score(text_x, text_y)
        # Updating the window
        pygame.display.update()
        
#suru()