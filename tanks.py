import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Tanks - By Dylan Goldberg')

clock = pygame.time.Clock()

# colors
wheat = (245, 222, 179)
cyan = (171, 219, 227)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)


# tanks dementions
tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

ground_height = 35

# fonts/text code
font1 = pygame.font.SysFont("Yu Mincho Demibold", 20)
font2 = pygame.font.SysFont("lucidaconsole", 25)
font3 = pygame.font.SysFont("comicsansms", 50)
font4 = pygame.font.SysFont("Yu Mincho Demibold", 85)


def text_objects(text, color, size="small"):
    global textsurface
    if size == "vsmall":
        textsurface = font1.render(text, True, color)
    if size == "small":
        textsurface = font2.render(text, True, color)
    if size == "medium":
        textsurface = font3.render(text, True, color)
    if size == "large":
        textsurface = font4.render(text, True, color)

    return textsurface, textsurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="vsmall"):
    textsurface, textrect = text_objects(msg, color, size)
    textrect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textsurface, textrect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textsurface, textrect = text_objects(msg, color, size)
    textrect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textsurface, textrect)


# start up screen
def startup():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Welcome to Tanks!", white, -100, size="large")
        message_to_screen("The objective is to shoot and destroy", cyan, 15)
        message_to_screen("All Black People Known to man Kind.", cyan, 60)
        message_to_screen("The more enemies you destroy, the harder they get.", cyan, 110)
        message_to_screen("Brought To You by: Dylan Goldberg", cyan, 280)

        button("Play", 150, 500, 100, 50, green, light_green, action="play", size="vsmall")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, action="controls", size="vsmall")
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit", size="vsmall")

        pygame.display.update()

        clock.tick(15)


# score
def score(score):
    text = font2.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0, 0])


# function for tank1, turrent positions

def tank1(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x - 27, y - 2),
                       (x - 26, y - 5),
                       (x - 25, y - 8),
                       (x - 23, y - 12),
                       (x - 20, y - 14),
                       (x - 18, y - 15),
                       (x - 15, y - 17),
                       (x - 13, y - 19),
                       (x - 11, y - 21)
                       ]

    pygame.draw.circle(gameDisplay, blue, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, blue, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, blue, (x, y), possibleTurrets[turPos])

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 15, y + 20), wheelWidth)

    return possibleTurrets[turPos]


# function for tank2, turrent positions
def tank2(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x + 27, y - 2),
                       (x + 26, y - 5),
                       (x + 25, y - 8),
                       (x + 23, y - 12),
                       (x + 20, y - 14),
                       (x + 18, y - 15),
                       (x + 15, y - 17),
                       (x + 13, y - 19),
                       (x + 11, y - 21)
                       ]

    pygame.draw.circle(gameDisplay, blue, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, blue, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, blue, (x, y), possibleTurrets[turPos])

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)

    pygame.draw.circle(gameDisplay, blue, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, blue, (x + 15, y + 20), wheelWidth)

    return possibleTurrets[turPos]
# control screen
def game_controls():
    control = True

    while control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        message_to_screen("Controls", white, -100, size="font3")
        message_to_screen("Fire: Spacebar", cyan, -30)
        message_to_screen("Move Turret: Up and Down arrows", cyan, 10)
        message_to_screen("Move Tank: Left and Right arrows", cyan, 50)
        message_to_screen("Press D to raise Power % AND Press A to lower Power % ", cyan, 140)
        message_to_screen("Pause: P", cyan, 90)

        button("Play", 150, 500, 100, 50, green, light_green, action="play")
        button("Main", 350, 500, 100, 50, yellow, light_yellow, action="main")
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)


# function for buttons having action calls and text on it callings
def button(text, x, y, width, height, inactive_color, active_color, action=None, size=" "):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                startup()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


# function for pause having transparent background
def pause():
    paused = True
    message_to_screen("Paused", white, -100, size="large")
    message_to_screen("Press C to continue playing or Q to quit", cyan, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)


# function for barrier
def barrier(xlocation, randomHeight, barrier_width):
    pygame.draw.rect(gameDisplay, green, [xlocation, display_height - randomHeight, barrier_width, randomHeight])



#function for explosion for both tanks
def explosion(x, y, size=50):
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        colorChoices = [red, light_red, yellow, light_yellow]

        magnitude = 1

        while magnitude < size:
            exploding_bit_x = x + random.randrange(-1 * magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1 * magnitude, magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y),
                               random.randrange(1, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False


# Firing function for tank1
def fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, tank2x, tank2y):
    fire = True
    damage = 0

    startingShell = list(xy)

    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)

        startingShell[0] -= (12 - turPos) * 2

        startingShell[1] += int(
            (((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50.0)) ** 2) - (turPos + turPos / (12.0 - turPos)))

        if startingShell[1] > display_height - ground_height:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Impact:", hit_x, hit_y)

            if tank2x + 10 > hit_x > tank2x - 10:
                print("Critical Hit!")
                damage = 25
            elif tank2x + 15 > hit_x > tank2x - 15:
                print("Hard Hit!")
                damage = 18
            elif tank2x + 25 > hit_x > tank2x - 25:
                print("Medium Hit")
                damage = 10
            elif tank2x + 35 > hit_x > tank2x - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage

# firing function for tank2
def e_fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, tank1x, tank1y):
    fire = True
    damage = 0

    startingShell = list(xy)

    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)

        #Makes it shoot right!
        #Makes it shoot right!
        startingShell[0] += (12 - turPos) * 2

        startingShell[1] += int(
            (((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50.0)) ** 2) - (turPos + turPos / (12.0 - turPos)))
        if startingShell[1] > display_height + ground_height:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Impact:", hit_x, hit_y)

            if tank1x + 10 > hit_x > tank1x - 10:
                print("Critical Hit!")
                damage = 25
            elif tank1x + 15 > hit_x > tank1x - 15:
                print("Hard Hit!")
                damage = 18
            elif tank1x + 25 > hit_x > tank1x - 25:
                print("Medium Hit")
                damage = 10
            elif tank1x + 35 > hit_x > tank1x - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight
        print(str(startingShell[0]) + " " + str(startingShell[1]))



        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage


# function for power level of players tank
def power(level):
    text = font2.render("Power: " + str(level) + "%", True, wheat)
    gameDisplay.blit(text, [display_width / 2, 0])


# gameoverscreen
def game_over():
    game_over = True

    while game_over:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        message_to_screen("Game Over", white, -100, size="large")
        message_to_screen("You died.", wheat, -30)

        button("Play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        button("Controls", 350, 500, 100, 50, wheat, light_yellow, action="controls")
        button("Quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)


# win screen
def you_win():
    win = True

    while win:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        message_to_screen("You won!", white, -100, size="large")
        message_to_screen("Congratulations!", cyan, -30)

        button("play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        button("controls", 350, 500, 100, 50, wheat, light_yellow, action="controls")
        button("quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)


# Health function
def health_bars(player_health, player2_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if player2_health > 75:
        player2_health_color = green
    elif player2_health > 50:
        player2_health_color = yellow
    else:
        player2_health_color = red

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, player2_health_color, (20, 25, player2_health, 25))


# game loop
def gameLoop():
    global enemy_gun, gun
    gameExit = False
    gameOver = False
    FPS = 25

    player_health = 100
    player2_health = 100

    barrier_width = 50

    mainTankX = display_width * .9
    mainTankY = display_height * .9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    tank2X = display_width * .1
    tank2Y = display_height * .9
    tank2TurPos = 0

    fire_power = 50
    power_change = 0

    xlocation = (display_width / 2.0) + random.randint((-1.0/10) * display_width, (1.0/10) * display_width)
    randomHeight = random.randrange(display_height * (1.0/10), display_height * (3.0/5))

    while not gameExit:

        if gameOver is True:
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver is True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:

                    damage = fireShell(gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation, barrier_width,
                                       randomHeight, tank2X, tank2Y)
                    player2_health -= damage

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):

                        if display_width * 0.3 > tank2X > display_width * 0.03:
                            if possibleMovement[moveIndex] == "f":
                                tank2X += 5
                            elif possibleMovement[moveIndex] == "r":
                                tank2X -= 5

                            gameDisplay.fill(black)
                            health_bars(player_health, player2_health)
                            gun = tank1(mainTankX, mainTankY, currentTurPos)
                            gun2 = tank2(tank2X, tank2Y, 8)
                            fire_power += power_change

                            power(fire_power)

                            barrier(xlocation, randomHeight, barrier_width)
                            print(str(xlocation) + " " + str(display_height))
                            gameDisplay.fill(green, rect=[0, display_height - ground_height, display_width, ground_height])
                            pygame.display.update()

                            clock.tick(FPS)

                    turposcom = [7, 8, 8, 8]
                    turpos2 = random.choice(turposcom)

                    comtankacc = [95, 93, 94, 88, 100, 100, 91, 78, 72, 75, 78, 80, 82, 85, 88, 90, 92, 100]
                    fire_power2 = random.choice(comtankacc)

                    damage = e_fireShell(gun2, tank2X, tank2Y, turpos2, fire_power2, xlocation, barrier_width,
                                         randomHeight, mainTankX, mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0

        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        if mainTankX - (tankWidth / 2) < xlocation + barrier_width:
            mainTankX += 5

        gameDisplay.fill(black)
        health_bars(player_health, player2_health)
        gun = tank1(mainTankX, mainTankY, currentTurPos)
        gun2 = tank2(tank2X, tank2Y, 8)

        fire_power += power_change

        if fire_power > 100:
            fire_power = 100
        elif fire_power < 1:
            fire_power = 1

        power(fire_power)

        barrier(xlocation, randomHeight, barrier_width)
        gameDisplay.fill(green, rect=[0, display_height - ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        elif player2_health < 1:
            you_win()
        clock.tick(FPS)

    pygame.quit()
    quit()


startup()
gameLoop()