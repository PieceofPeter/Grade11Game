from pygame import display
from pygameMenuPro import *
import sys
import pygame
import time
import os

# pygame initialization
pygame.init()
pygame.font.init()
pygame.display.set_caption('BALLOONS VS TOWERS')
pygame.mixer.init()
key = pygame.key.get_pressed()

# colours
red = (255, 0, 0)
blue = (38, 91, 200)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
orange = (255, 97, 3)
yellow = (255, 242, 56)

# displays
screen = pygame.display.set_mode((1280, 720))
width = screen.get_width()
height = screen.get_height()

# fonts
Option.font.set_default_option(pygame.font.Font('8-bit.ttf', 40))
Option.font.set_default_title(pygame.font.Font('8-bit.ttf', 65))
Option.font.set_default_highlight(pygame.font.Font('8-bit.ttf', 55))
mainpos = (screen.get_width() // 2, screen.get_height() // 4)
mainpos2 = (screen.get_width() // 2, screen.get_height() // 12)
titlefont = pygame.font.Font('8-bit.ttf', 42)
font = pygame.font.Font('8-bit.ttf', 42)
font2 = pygame.font.Font('8-bit.ttf', 28)
font3 = pygame.font.Font('8-bit.ttf', 22)

# splashcreen code
def splashscreen(x, y):
    colour = (255, 255, 255)
    text1 = titlefont.render("MADE BY:", True, colour)
    text2 = titlefont.render("PETER. A AND EGOR. M", True, colour)
    text3 = titlefont.render("Press Enter to Continue....", True, colour)
    text4 = font3.render('"Next-level gameplay" - Egor M.', True, colour)
    screen.blit(text1, ((width / 2) - 165, y))
    screen.blit(text2, ((width / 2) - 400, (y + 70)))
    screen.blit(text3, ((width / 2) - 540, (y + 300)))
    screen.blit(text4, ((width / 2) - 325, (y + 150)))

# function for when start game is called on menu
def startgame():
    menu.run_display = False
    while True:
        Option.input.check_input()
        Option.clock.tick(60)
        display.update()
        Option.input.reset()
        game = False

        def difficulty():
            pygame.init()
            pygame.display.set_caption('SELECT DIFFICULTY') # select difficulty screen
            pygame.display.update()

            # colours
            red = (255, 0, 0)
            green = (0, 255, 0)
            yellow = (255, 242, 56)

            # displays
            screen = pygame.display.set_mode((1280, 720))

            # fonts
            Option.font.set_default_option(pygame.font.Font('8-bit.ttf', 40))
            Option.font.set_default_title(pygame.font.Font('8-bit.ttf', 70))
            Option.font.set_default_highlight(pygame.font.Font('8-bit.ttf', 55, bold=True))
            mainpos = (screen.get_width() // 2, screen.get_height() // 4)

            # function made to start the game once the start game button is pressed
            def easy():
                var = 1
                tutorial(1)
                return var

            def medium():
                var = 2
                tutorial(2)
                return var

            def hard():
                var = 3
                tutorial(3)
                return var

            # function for quitting menus
            def difquit_menu(menu: Menu):
                time.sleep(0.25)
                dif_menu.run_display = False
                Option.input.reset()
                menu.run_display = True
                menu.display_menu()
                pygame.display.update()

            # options menu code
            spc = Option(' ')
            ez = Option('EASY', color=green).add.highlight().add.select_listener(lambda _: easy())
            med = Option('NORMAL', color=yellow).add.highlight().add.select_listener(lambda _: medium())
            hrd = Option('HARD', color=red).add.highlight().add.select_listener(lambda _: hard())
            difquit = Option('Back To Main Menu').add.highlight().add.select_listener(lambda _: difquit_menu(dif_menu))

            # menu with all the options
            dif_menu = Option('SELECT DIFFICULTY', color=white).add.mouse_menu(screen, mainpos,
                                                                               background_color=black).set_options(
                [spc, ez, spc, med, spc, hrd, spc]).add.highlight().add.select_listener(
                lambda _: Option.input.reset())

            # main code
            while game == False:
                dif_menu.display_menu()
                break

        running = True
        while running:
            for event in pygame.event.get():
                difficulty()

        pygame.display.update()

# some sound effects
lifelostsfx = pygame.mixer.Sound('lifelost.mp3')
pygame.mixer.Sound.set_volume(lifelostsfx, 0.4)

towerlifelostsfx = pygame.mixer.Sound('towerlifelost.mp3')
pygame.mixer.Sound.set_volume(towerlifelostsfx, 0.4)

# the tutorial
def tutorial(var):
    # assets for tutorial
    pygame.mixer.music.stop()
    pygame.mixer.music.load('tutorial.mp3.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.time.delay(300)
    pygame.mixer.music.play(-1)
    icon_r = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
    resize_r = pygame.transform.scale(icon_r, (170, 170))
    icon_l = pygame.image.load(os.path.join("assets", "guyleft.png")).convert_alpha()
    resize_l = pygame.transform.scale(icon_l, (170, 170))
    # background
    background = pygame.image.load(os.path.join("assets", "background.jpg")).convert_alpha()
    # projectile
    tack = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack.png")).convert_alpha(), (50, 50))
    tack_l = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack_l.png")).convert_alpha(), (50, 50))
    # enemies
    green_balloon = pygame.transform.scale(pygame.image.load(os.path.join("assets", "green_balloon.png")).convert_alpha(), (100, 100))
    popped = pygame.transform.scale(pygame.image.load(os.path.join("assets", "balloonpopped.png")).convert_alpha(), (200, 200))
    # tower
    tower = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tower.png")).convert_alpha(), (300, 300))

    damagesound = pygame.mixer.Sound('hurtsfx.mp3')
    pygame.mixer.Sound.set_volume(damagesound, 0.6)
    popsfx = pygame.mixer.Sound('popsfx.mp3')
    pygame.mixer.Sound.set_volume(popsfx, 0.6)

    # jump
    jump = False
    # default character position
    x = 100
    y = 425
    # set windows mode
    scr = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Balloons vs Towers")
    # dimensions of the object
    width = 200
    height = 100

    # velocity / speed of movement
    tackspeed = 38
    hitvar = False
    move_speed = 20
    player_life = 100
    speed_balloon = 10
    towerhealth = 99
    cooldown = 1

    # character class
    class Player:
        def __init__(self, x, y):
            # walk
            self.x = x
            self.y = y
            self.spd = move_speed
            self.spd_jump = 14.5
            self.face_right = True
            self.face_left = False

            # jumping
            self.jump = False

            # projectiles
            self.projectiles = []
            self.cooldown = cooldown
            # health
            self.hitbox = (self.x + 30, self.y + 45, 100, 150)
            self.hitvar = hitvar
            self.health = 100
            self.lives = player_life
            self.alive = True

    # moving player
        def move_player(self, userInput):
            if userInput[pygame.K_RIGHT] and self.x < 1280 - width:
                self.spd = move_speed
                self.x += self.spd
                self.face_right = True
                self.face_left = False

            if userInput[pygame.K_d] and self.x < 1280 - width:
                self.spd = move_speed
                self.x += self.spd
                self.face_right = True
                self.face_left = False

            if userInput[pygame.K_LEFT] and self.x > 0:
                self.spd = move_speed
                self.x -= self.spd
                self.face_right = False
                self.face_left = True

            if userInput[pygame.K_a] and self.x > 0:
                self.spd = move_speed
                self.x -= self.spd
                self.face_right = False
                self.face_left = True

    # drawing hitboxes
        def draw(self, scr):
            self.hitbox = (self.x + 30, self.y + 35, 100, 170)

            pygame.draw.rect(scr, (255, 0, 0), (self.x + 30, self.y, 100, 10))
            if self.health >= 0:
                pygame.draw.rect(scr, (0, 255, 0), (self.x + 30, self.y, self.health, 10))

            if self.face_left:
                scr.blit(resize_l, (self.x, self.y + 20))
            if self.face_right:
                scr.blit(resize_r, (self.x, self.y + 20))

    # jumping and gravity
        def jump_motion(self, userInput):
            if userInput[pygame.K_UP] or userInput[pygame.K_SPACE] or userInput[pygame.K_w] and self.jump is False:
                self.jump = True
            if self.jump == True:
                self.y -= self.spd_jump
                self.spd_jump -= 1
                if self.spd_jump < -14.5:
                    self.jump = False
                    self.spd_jump = 14.5

        def direction(self):
            if self.face_right:
                return 1
            if self.face_left:
                return -1

    # cooldown for shooting so game dont crash
        def cooldown_func(self):
            if self.cooldown >= 20:
                self.cooldown = 0
            elif self.cooldown > 0:
                self.cooldown += 1

    # fun for player shootingf and it either hits or goes out of bounds
        def shoot(self):
            self.hit()
            self.cooldown_func()
            if (userInput[pygame.K_RETURN] and self.cooldown == 0):
                projectile = Projectile(self.x, self.y, self.direction())
                self.projectiles.append(projectile)
                self.cooldown = cooldown
            for projectile in self.projectiles:
                projectile.move()
                if projectile.out_of_bounds():
                    self.projectiles.remove(projectile)
                if self.hitvar == True:
                    self.projectiles.remove(projectile)

    # this is hit the other one is out of bounds
        def hit(self):
            for ez in easy_balloon:
                for projectile in self.projectiles:
                    if ez.hitbox[0] < projectile.x < ez.hitbox[0] + ez.hitbox[2] and ez.hitbox[1] < projectile.y + 100 < \
                            ez.hitbox[1] + ez.hitbox[3]:
                        self.hitvar = True

    # thumbtacks
    class Projectile:
        def __init__(self, x, y, direction):
            self.x = x + 15
            self.y = y + 25
            self.direction = direction
            self.hitvar = hitvar
            self.speed = tackspeed

        def draw_projectile(self):
            if self.direction == 1:
                scr.blit(tack, (self.x + 50, self.y + 75))
            if self.direction == -1:
                scr.blit(tack_l, (self.x + 50, self.y + 75))

        def move(self):
            if self.direction == 1:
                self.x += self.speed
            if self.direction == -1:
                self.x -= self.speed

        def out_of_bounds(self):
            return not (self.x >= 0 and self.x <= 1280)

    # enemy
    class Easy_Enemy:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.spd = speed_balloon
            # health
            self.hitbox = (self.x, self.y, 100, 100)

        def draw(self, scr):
            self.hitbox = (self.x, self.y, 100, 100)

            scr.blit(green_balloon, (self.x, self.y))

    # how bloons move on its own
        def move(self):
            self.hit()
            self.x -= self.spd

        def hit(self):
            if init.hitbox[0] < ez.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < ez.y + 32 < \
                    init.hitbox[1] + init.hitbox[3]:
                if init.health > 0:
                    init.health -= 3
                    if init.health % 5 == 0:
                        pygame.mixer.Channel(2).play(damagesound)
                    if init.health <= 0 and init.lives > 0:
                        pygame.mixer.Channel(0).play(lifelostsfx)
                        init.lives -= 1
                        init.health = 100
                    elif init.health == 1 and init.lives == 1:
                        init.alive = False

        def out_of_bounds(self):

            return not (self.x >= 0 and self.x <= 1280)

    # draws the entire game
    def draw_game():
        scr.fill((0, 0, 0))
        scr.blit(background, (0, 0))
        init.draw(scr)
        scr.blit(tower, (-75, 330))

        # draw number of lives left for tower and player

        tuttitlefont = pygame.font.Font('8-bit.ttf', 62)
        tutfont4 = pygame.font.Font('8-bit.ttf', 18)
        black = (0, 0, 0)

        towerlives = font.render(str(towerhealth), True, black)
        scr.blit(towerlives, (36, 325))

        tuttitle = tuttitlefont.render("TUTORIAL", True, black)
        scr.blit(tuttitle, (360, 50))
        tutsub6 = tutfont4.render('DO NOT GET HIT BY THE BALLOONS OR LET THE BALLOONS HIT YOUR TOWER', True, black)
        scr.blit(tutsub6, (82, 118))
        tutsub1 = tutfont4.render('POP ALL BALLOONS IN TIME TO WIN!',True,black)
        scr.blit(tutsub1, (330, 145))
        tutsub2 = tutfont4.render('MOVE FORWARD USING [D] OR [RIGHT ARROW]', True, black) # controls layout
        scr.blit(tutsub2, (300, 175))
        tutsub3 = tutfont4.render('MOVE BACK USING [A] OR [LEFT ARROW]', True, black)
        scr.blit(tutsub3, (315, 205))
        tutsub4 = tutfont4.render('JUMP USING [SPACE] [W] OR [UP ARROW]', True, black)
        scr.blit(tutsub4, (360, 235))
        tutsub5 = tutfont4.render('SHOOT USING [ENTER]', True, black)
        scr.blit(tutsub5, (450, 265))
        tutsub8 = tutfont4.render('PAUSE USING [ESCAPE]', True, black)
        scr.blit(tutsub8, (450, 295))
        tutsub9 = tutfont4.render('PRESS [N] TO MOVE ONTO LEVEL 1!', True, black)
        scr.blit(tutsub9, (360, 325))

        for projectile in init.projectiles:
            projectile.draw_projectile()
        for ez in easy_balloon:
            ez.draw(scr)

    # transitions from tutorial to level1
            if userInput[pygame.K_n]:
                if var == 1:
                    level1(10, 25, 20, 5, 4, 30)

                if var == 2:
                    level1(10, 20, 20, 3, 3, 30)

                if var == 3:
                    level1(14, 10, 20, 2, 2, 30)

        pygame.time.delay(30)

        pygame.display.update()

    # instance of the player
    init = Player(50, 425)

    # instance of the easy balloons
    easy_balloon = []

    # Indicates pygame is running
    run = True
    while run == True:

        # mouse position
        mouse = pygame.mouse.get_pos()
        userInput = pygame.key.get_pressed()

        # creates time delay of 10ms
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if userInput[pygame.K_ESCAPE]:
                bloop = pygame.mixer.Sound('bloop.mp3')
                pygame.mixer.Sound.set_volume(bloop, 0.8)
                pygame.mixer.Channel(7).play(bloop)
                menu2.display_menu()

        init.shoot()
        init.move_player(userInput)
        init.jump_motion(userInput)

        # enemies
        if len(easy_balloon) == 0:
            ez = Easy_Enemy(1100, 500)
            easy_balloon.append(ez)

        for ez in easy_balloon:
            ez.move()
            if ez.out_of_bounds():
                easy_balloon.remove(ez)
                towerhealth = towerhealth - 1
                pygame.mixer.Channel(1).play(towerlifelostsfx)

                if towerhealth == 0:
                    init.alive = False
                    towerhealth = 99

            if init.hitvar == True:
                scr.blit(popped, (ez.x - 20, ez.y - 40))
                pygame.mixer.Channel(3).play(popsfx)
                easy_balloon.remove(ez)
                init.hitvar = False

        pygame.display.update()

        # Draw Game in Window
        draw_game()

    # closes the pygame window
    pygame.quit()

# function made to start the game once the start game button is pressed
def level1(speed_balloon, money_gain, move_speed, tower_life, player_life, time_of_level):
    # the way it transitions from level to level
    level_one = True
    # the way it saves difficulty when respawning
    while level_one == True:
        if tower_life == 5:
            eas = True
            med = False
            har = False

        if tower_life == 3:
            eas = False
            med = True
            har = False

        if tower_life == 2:
            eas = False
            med = False
            har = True

        # imports
        import os
        import pygame
        pygame.init()

        # variables and assets
        # player
        pygame.mixer.music.stop()
        pygame.mixer.music.load('battle.wav')
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(-1)

        icon_r = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        resize_r = pygame.transform.scale(icon_r, (170, 170))
        icon_l = pygame.image.load(os.path.join("assets", "guyleft.png")).convert_alpha()

        resize_l = pygame.transform.scale(icon_l, (170, 170))
        # background
        background = pygame.image.load(os.path.join("assets", "background.jpg")).convert_alpha()
        # projectile
        tack = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack.png")).convert_alpha(), (50, 50))
        tack_l = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack_l.png")).convert_alpha(), (50, 50))
        # enemies
        green_balloon = pygame.transform.scale(pygame.image.load(os.path.join("assets", "green_balloon.png")).convert_alpha(), (100, 100))
        popped = pygame.transform.scale(pygame.image.load(os.path.join("assets", "balloonpopped.png")).convert_alpha(), (200, 200))
        # tower
        tower = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tower.png")).convert_alpha(), (300, 300))
        towerhealth = tower_life

        damagesound = pygame.mixer.Sound('hurtsfx.mp3')
        pygame.mixer.Sound.set_volume(damagesound, 0.6)
        popsfx = pygame.mixer.Sound('popsfx.mp3')
        pygame.mixer.Sound.set_volume(popsfx, 0.6)
        winsfx = pygame.mixer.Sound('victory.wav')
        pygame.mixer.Sound.set_volume(winsfx, 0.5)

        # jump
        jump = False
        # default character position
        x = 100
        y = 425
        # set windows mode
        scr = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Balloons vs Towers")
        # dimensions of the object
        width = 200
        height = 100

        # velocity / speed of movement
        tackspeed = 38
        hitvar = False
        # colours for buttons
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        # upgrades
        score = 0
        money = 0
        moneygain = money_gain
        moneypthreshold = 50
        cooldownpthreshold = 100
        mvmentupgradethreshold = 100
        moneyfont = pygame.font.Font('8-bit.ttf', 30)
        upgradefont = pygame.font.Font('8-bit.ttf', 20)
        smallerupgradefont = pygame.font.Font('8-bit.ttf', 15)
        cooldown = 1

        # character class
        # same as tutorial code but some parts added on
        class Player:
            def __init__(self, x, y):
                # walk
                self.x = x
                self.y = y
                self.spd = move_speed
                self.spd_jump = 14.5
                self.face_right = True
                self.face_left = False

                # jumping
                self.jump = False

                # projectiles
                self.projectiles = []
                self.cooldown = cooldown
                # health
                self.hitbox = (self.x + 30, self.y + 45, 100, 150)
                self.hitvar = hitvar
                self.health = 100
                self.lives = player_life
                self.alive = True

            def move_player(self, userInput):
                if userInput[pygame.K_RIGHT] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_d] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_LEFT] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

                if userInput[pygame.K_a] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

            def draw(self, scr):
                self.hitbox = (self.x + 30, self.y + 35, 100, 170)

                pygame.draw.rect(scr, (255, 0, 0), (self.x + 30, self.y, 100, 10))
                if self.health >= 0:
                    pygame.draw.rect(scr, (0, 255, 0), (self.x + 30, self.y, self.health, 10))

                if self.face_left:
                    scr.blit(resize_l, (self.x, self.y + 20))
                if self.face_right:
                    scr.blit(resize_r, (self.x, self.y + 20))

            def jump_motion(self, userInput):
                if userInput[pygame.K_UP] or userInput[pygame.K_SPACE] or userInput[pygame.K_w] and self.jump is False:
                    self.jump = True
                if self.jump == True:
                    self.y -= self.spd_jump
                    self.spd_jump -= 1
                    if self.spd_jump < -14.5:
                        self.jump = False
                        self.spd_jump = 14.5

            def direction(self):
                if self.face_right:
                    return 1
                if self.face_left:
                    return -1

            def cooldown_func(self):
                if self.cooldown >= 20:
                    self.cooldown = 0
                elif self.cooldown > 0:
                    self.cooldown += 1

            def shoot(self):
                self.hit()
                self.cooldown_func()
                if (userInput[pygame.K_RETURN] and self.cooldown == 0):
                    projectile = Projectile(self.x, self.y, self.direction())
                    self.projectiles.append(projectile)
                    self.cooldown = cooldown
                for projectile in self.projectiles:
                    projectile.move()
                    if projectile.out_of_bounds():
                        self.projectiles.remove(projectile)
                    if self.hitvar == True:
                        self.projectiles.remove(projectile)

            def hit(self):
                for ez in easy_balloon:
                    for projectile in self.projectiles:
                        if ez.hitbox[0] < projectile.x < ez.hitbox[0] + ez.hitbox[2] and ez.hitbox[1] < projectile.y + 100 < \
                                ez.hitbox[1] + ez.hitbox[3]:
                            self.hitvar = True

        # thumbtacks
        class Projectile:
            def __init__(self, x, y, direction):
                self.x = x + 15
                self.y = y + 25
                self.direction = direction
                self.hitvar = hitvar
                self.speed = tackspeed

            def draw_projectile(self):
                if self.direction == 1:
                    scr.blit(tack, (self.x + 50, self.y + 75))
                if self.direction == -1:
                    scr.blit(tack_l, (self.x + 50, self.y + 75))

            def move(self):
                if self.direction == 1:
                    self.x += self.speed
                if self.direction == -1:
                    self.x -= self.speed

            def out_of_bounds(self):
                return not (self.x >= 0 and self.x <= 1280)

        # enemy
        class Easy_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = speed_balloon
                # health
                self.hitbox = (self.x, self.y, 100, 100)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 100, 100)

                scr.blit(green_balloon, (self.x, self.y))
                scr.blit(green_balloon, (self.x, self.y))

            def move(self):
                self.hit()
                self.x -= self.spd

            def hit(self):
                if init.hitbox[0] < ez.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < ez.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

    # draws level 1
        def draw_game():
            upgrade_bckg = (0, 0, 1280, 150)
            bckg_border = (1000, 0, 1280, 150)
            lives_border = (0, 0, 225, 150)
            scr.fill((0, 0, 0))
            scr.blit(background, (0, 0))
            init.draw(scr)
            scr.blit(tower, (-75, 350))
            pygame.draw.rect(scr, ((230,220,170)), upgrade_bckg, 100)
            pygame.draw.rect(scr, (0, 0, 0), upgrade_bckg, 10)
            pygame.draw.rect(scr, (0, 0, 0), bckg_border, 10)
            pygame.draw.rect(scr, (0, 0, 0), lives_border, 10)
            colour = (0, 0, 0)

            # draw number of lives left for tower and player
            leveltext = smallerupgradefont.render("LEVEL 1", True, colour)
            livestext = smallerupgradefont.render("Lives left:", True, colour)
            numberoflives = moneyfont.render(str(init.lives), True, colour)
            towerlives = moneyfont.render(str(towerhealth), True, colour)
            scr.blit(towerlives, (65, 325))
            scoretext = upgradefont.render("Score:" + str(score), True, colour)
            scr.blit(leveltext,(18,187))
            scr.blit(scoretext, (18, 165))

            scr.blit(numberoflives, (15, 75))
            scr.blit(livestext, (15, 50))

            # following lines draw upgrades
            message = 'TIME LEFT: ' + str(time_of_level) + 's'
            timetext = font3.render(message, True, colour)
            scr.blit(timetext, (500, 170))
            moneytext = moneyfont.render("$" + str(money), True, colour)
            moneyupgradetext = upgradefont.render("+10 per pop", True, colour)
            moneyupgradetextprice = upgradefont.render("($" + str(moneypthreshold) + ")", True, colour)
            currentrate = upgradefont.render("(" + str(moneygain) + " per pop)", True, colour)
            cooldownupgrade = upgradefont.render("Tack speed", True, colour)
            cooldownupgradeprice = upgradefont.render("($" + str(cooldownpthreshold) + ")", True, colour)
            maxupgrade = upgradefont.render("MAX", True, colour)
            mvmmentupgrade = smallerupgradefont.render("Movement speed", True, colour)
            mvmentupgradeprice = upgradefont.render("($" + str(mvmentupgradethreshold) + ")", True, colour)
            scr.blit(moneytext, (1025, 65))

            for projectile in init.projectiles:
                projectile.draw_projectile()

            for ez in easy_balloon:
                ez.draw(scr)

            if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [750, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [750, 40, 225, 65])
            if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [500, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [500, 40, 225, 65])
            if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [250, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [250, 40, 225, 65])

            scr.blit(moneyupgradetext, (750, 50))
            scr.blit(moneyupgradetextprice, (810, 80))
            scr.blit(currentrate, (1025, 100))
            scr.blit(cooldownupgrade, (510, 50))

            if cooldown >= 10:
                scr.blit(maxupgrade, (585, 80))
            else:
                scr.blit(cooldownupgradeprice, (550, 80))
            if move_speed == 50:
                scr.blit(maxupgrade, (335, 80))
            else:
                scr.blit(mvmentupgradeprice, (300, 80))
            scr.blit(mvmmentupgrade, (260, 50))

    # draws respawn screen
            if init.alive == False:
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

                def level_lose():
                    if eas == True:
                        init.alive = True
                        level1(8, 25, 23, 5, 4, 30)

                    if med == True:
                        init.alive = True
                        level1(10, 20, 20, 3, 3, 30)

                    if har == True:
                        init.alive = True
                        level1(18, 10, 20, 2, 2, 30)

                    pygame.time.delay(30)
                    pygame.display.update()

                lose_level = Option('RESPAWN').add.highlight().add.select_listener(lambda _: level_lose())
                losemenu = Option('YOU DIED').add.mouse_menu(screen, mainpos).set_options([space, lose_level, space, space, back_menu, space, quit])
                losemenu.display_menu()

    # victory menu
            if time_of_level <= 0 and init.alive == True:
                level_one = False
                run = False
                pygame.mixer.Sound.set_volume(popsfx, 0)
                pygame.mixer.Sound.set_volume(damagesound,0)
                pygame.mixer.music.stop()
                pygame.mixer.music.load('victory.wav')
                pygame.mixer.music.set_volume(0.30)
                pygame.mixer.music.play()

                def winlevel():
                    if eas == True:
                        level2(8, 25, 23, 5, 4, 45, score)

                    if med == True:
                        level2(10, 20, 20, 3, 3, 45, score)

                    if har == True:
                        level2(18, 10, 20, 2, 2, 45, score)

                win_level = Option('NEXT LEVEL!',color=green).add.highlight().add.select_listener(lambda _: winlevel())
                winmenu = Option('YOU WIN!').add.mouse_menu(screen, mainpos).set_options(
                    [space, win_level, space, space, back_menu, space, quit])
                winmenu.display_menu()

            pygame.time.delay(30)
            pygame.display.update()

        # instance of the player
        init = Player(50, 425)

        # instance of the easy balloons
        easy_balloon = []

        # Indicates pygame is running
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        run = True
        while run == True:
            pygame.display.flip()
            clock.tick(60)

            # mouse position
            mouse = pygame.mouse.get_pos()
            userInput = pygame.key.get_pressed()

            # creates time delay of 10ms
            pygame.time.delay(10)

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    time_of_level -= 1

                if event.type == pygame.QUIT:
                    run = False

                if userInput[pygame.K_ESCAPE]:
                    bloop = pygame.mixer.Sound('bloop.mp3')
                    pygame.mixer.Sound.set_volume(bloop, 0.8)
                    pygame.mixer.Channel(7).play(bloop)
                    menu2.display_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65 and money >= moneypthreshold:
                        money = money - moneypthreshold
                        moneygain = moneygain + 10
                        moneypthreshold = moneypthreshold * 2
                    if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= cooldownpthreshold and cooldown < 10:
                        money = money - cooldownpthreshold
                        cooldown = cooldown + 3
                        tackspeed = tackspeed + 12
                        cooldownpthreshold = cooldownpthreshold * 2
                    if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= mvmentupgradethreshold and move_speed < 50:
                        money = money - mvmentupgradethreshold
                        move_speed = move_speed + 4
                        mvmentupgradethreshold = mvmentupgradethreshold * 2

            init.shoot()
            init.move_player(userInput)
            init.jump_motion(userInput)

            # enemies
            if len(easy_balloon) == 0:
                ez = Easy_Enemy(1100, 500)
                easy_balloon.append(ez)

            for ez in easy_balloon: # for loop for checking what bloon does. moves, out of bounds, hits tower, gets hit
                ez.move()
                if ez.out_of_bounds():
                    easy_balloon.remove(ez)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life
                if init.hitvar == True:
                    scr.blit(popped, (ez.x - 20, ez.y - 40))
                    pygame.mixer.Channel(3).play(popsfx)
                    easy_balloon.remove(ez)
                    init.hitvar = False
                    money = money + moneygain
                    if speed_balloon <= 24:
                        speed_balloon = speed_balloon + .5
                    score = score + 5


            pygame.display.update()

            # Draw Game in Window
            draw_game()

        # closes the pygame window
        pygame.quit()

# repeated code for l2 with dif variables and new bloon
def level2(speed_balloon, money_gain, move_speed, tower_life, player_life, time_of_level, score):
    # the way it transitions from level to level
    level_two = True
    # the way it saves difficulty when respawning
    while level_two == True:
        if tower_life == 5:
            eas = True
            med = False
            har = False

        if tower_life == 3:
            eas = False
            med = True
            har = False

        if tower_life == 2:
            eas = False
            med = False
            har = True

        # imports
        import os
        import pygame
        pygame.init()

        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        # variables and assets
        # player
        pygame.mixer.music.stop()
        pygame.mixer.music.load('level2.mp3')
        pygame.mixer.music.play(-1)
        icon_r = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        resize_r = pygame.transform.scale(icon_r, (170, 170))
        icon_l = pygame.image.load(os.path.join("assets", "guyleft.png")).convert_alpha()
        resize_l = pygame.transform.scale(icon_l, (170, 170))
        # background
        background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Background2.png")).convert_alpha(), (1500,780))

        # projectile
        tack = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack.png")), (50, 50)).convert_alpha()
        tack_l = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack_l.png")), (50, 50)).convert_alpha()
        # enemies
        green_balloon = pygame.transform.scale(pygame.image.load(os.path.join("assets", "green_balloon.png")).convert_alpha(), (100, 100))
        flying_balloon = pygame.transform.scale(pygame.image.load(os.path.join("assets", "flyingballoon.png")).convert_alpha(), (200,200))
        popped = pygame.transform.scale(pygame.image.load(os.path.join("assets", "balloonpopped.png")).convert_alpha(), (200, 200))
        # tower
        tower = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tower.png")).convert_alpha(), (300, 300))
        towerhealth = tower_life

        popsfx = pygame.mixer.Sound('popsfx.mp3')
        pygame.mixer.Sound.set_volume(popsfx, 0.6)
        damagesound = pygame.mixer.Sound('hurtsfx.mp3')
        pygame.mixer.Sound.set_volume(damagesound, 0.6)

        # jump
        jump = False
        # default character position
        x = 100
        y = 425
        # set windows mode
        scr = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Balloons vs Towers")
        # dimensions of the object
        width = 200
        height = 100

        # velocity / speed of movement
        tackspeed = 38
        hitvar = False
        hitvar_fly = False
        # colours for buttons
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        # upgrades
        score2 = score
        money = 0
        moneygain = money_gain
        moneypthreshold = 50
        cooldownpthreshold = 100
        mvmentupgradethreshold = 100
        moneyfont = pygame.font.Font('8-bit.ttf', 30)
        upgradefont = pygame.font.Font('8-bit.ttf', 20)
        smallerupgradefont = pygame.font.Font('8-bit.ttf', 15)
        cooldown = 1

        # character class
        class Player:
            def __init__(self, x, y):
                # walk
                self.x = x
                self.y = y
                self.spd = move_speed
                self.spd_jump = 14.5
                self.face_right = True
                self.face_left = False

                # jumping
                self.jump = False

                # projectiles
                self.projectiles = []
                self.cooldown = cooldown
                # health
                self.hitbox = (self.x + 30, self.y + 45, 100, 150)
                self.hitvar = hitvar
                self.hitvar_fly = hitvar_fly
                self.health = 100
                self.lives = player_life
                self.alive = True

            def move_player(self, userInput):
                if userInput[pygame.K_RIGHT] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_d] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_LEFT] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

                if userInput[pygame.K_a] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

            def draw(self, scr):
                self.hitbox = (self.x + 30, self.y + 35, 100, 170)

                pygame.draw.rect(scr, (255, 0, 0), (self.x + 30, self.y, 100, 10))
                if self.health >= 0:
                    pygame.draw.rect(scr, (0, 255, 0), (self.x + 30, self.y, self.health, 10))

                if self.face_left:
                    scr.blit(resize_l, (self.x, self.y + 20))
                if self.face_right:
                    scr.blit(resize_r, (self.x, self.y + 20))

            def jump_motion(self, userInput):
                if userInput[pygame.K_UP] or userInput[pygame.K_SPACE] or userInput[pygame.K_w] and self.jump is False:
                    self.jump = True
                if self.jump == True:
                    self.y -= self.spd_jump
                    self.spd_jump -= 1
                    if self.spd_jump < -14.5:
                        self.jump = False
                        self.spd_jump = 14.5

            def direction(self):
                if self.face_right:
                    return 1
                if self.face_left:
                    return -1

            def cooldown_func(self):
                if self.cooldown >= 20:
                    self.cooldown = 0
                elif self.cooldown > 0:
                    self.cooldown += 1

            def shoot(self):
                self.hit()
                self.hit_fly()
                self.cooldown_func()
                if (userInput[pygame.K_RETURN] and self.cooldown == 0):
                    projectile = Projectile(self.x, self.y, self.direction())
                    self.projectiles.append(projectile)
                    self.cooldown = cooldown
                for projectile in self.projectiles:
                    projectile.move()
                    if projectile.out_of_bounds():
                        self.projectiles.remove(projectile)
                    if self.hitvar == True:
                        self.projectiles.remove(projectile)
                    if self.hitvar_fly == True:
                        self.projectiles.remove(projectile)

            def hit(self):
                for ez in easy_balloon:
                    for projectile in self.projectiles:
                        if ez.hitbox[0] < projectile.x < ez.hitbox[0] + ez.hitbox[2] and ez.hitbox[
                            1] < projectile.y + 100 < \
                                ez.hitbox[1] + ez.hitbox[3]:
                            self.hitvar = True

            def hit_fly(self):
                for fly in fly_balloon:
                    for projectile in self.projectiles:
                        if fly.hitbox[0] < projectile.x < fly.hitbox[0] + fly.hitbox[2] and fly.hitbox[
                            1] < projectile.y + 100 < \
                                fly.hitbox[1] + fly.hitbox[3]:
                            self.hitvar_fly = True

        # thumbtacks
        class Projectile:
            def __init__(self, x, y, direction):
                self.x = x + 15
                self.y = y + 25
                self.direction = direction
                self.hitvar = hitvar
                self.hitvar = hitvar_fly
                self.speed = tackspeed

            def draw_projectile(self):
                if self.direction == 1:
                    scr.blit(tack, (self.x + 50, self.y + 75))
                if self.direction == -1:
                    scr.blit(tack_l, (self.x + 50, self.y + 75))

            def move(self):
                if self.direction == 1:
                    self.x += self.speed
                if self.direction == -1:
                    self.x -= self.speed

            def out_of_bounds(self):
                return not (self.x >= 0 and self.x <= 1280)

        # enemy
        class Easy_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = speed_balloon - 4
                # health
                self.hitbox = (self.x, self.y, 100, 100)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 100, 100)

                scr.blit(green_balloon, (self.x, self.y))
                scr.blit(green_balloon, (self.x, self.y))

            def move(self):
                self.hit()
                self.x -= self.spd

            def hit(self):
                if init.hitbox[0] < ez.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < ez.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        # same code for easy but flying
        class Fly_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = speed_balloon - 6
                # health
                self.hitbox = (self.x, self.y, 200, 200)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 200, 200)
                scr.blit(flying_balloon, (self.x, self.y))

            def move_fly(self):
                self.hit_fly()
                self.x -= self.spd

            def hit_fly(self):
                if init.hitbox[0] < fly.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] > fly.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)


        def draw_game():
            upgrade_bckg = (0, 0, 1280, 150)
            bckg_border = (1000, 0, 1280, 150)
            lives_border = (0, 0, 225, 150)
            scr.fill((0, 0, 0))
            scr.blit(background, (0, -30))
            init.draw(scr)
            scr.blit(tower, (-75, 350))
            pygame.draw.rect(scr, ((230,220,170)), upgrade_bckg, 100)
            pygame.draw.rect(scr, (0, 0, 0), upgrade_bckg, 10)
            pygame.draw.rect(scr, (0, 0, 0), bckg_border, 10)
            pygame.draw.rect(scr, (0, 0, 0), lives_border, 10)
            colour = (0, 0, 0)

            # draw number of lives left for tower and player
            leveltext = smallerupgradefont.render("LEVEL 2", True, colour)
            livestext = smallerupgradefont.render("Lives left:", True, colour)
            numberoflives = moneyfont.render(str(init.lives), True, colour)
            towerlives = moneyfont.render(str(towerhealth), True, colour)
            scr.blit(towerlives, (65, 325))
            scoretext = upgradefont.render("Score:" + str(score2), True, colour)
            scr.blit(leveltext, (18, 187))
            scr.blit(scoretext, (18, 165))
            scr.blit(numberoflives, (15, 75))
            scr.blit(livestext, (15, 50))

            # following lines draw upgrades
            message = 'TIME LEFT: ' + str(time_of_level) + 's'
            timetext = font3.render(message, True, colour)
            scr.blit(timetext, (490, 175))
            moneytext = moneyfont.render("$" + str(money), True, colour)
            moneyupgradetext = upgradefont.render("+10 per pop", True, colour)
            moneyupgradetextprice = upgradefont.render("($" + str(moneypthreshold) + ")", True, colour)
            currentrate = upgradefont.render("(" + str(moneygain) + " per pop)", True, colour)
            cooldownupgrade = upgradefont.render("Tack speed", True, colour)
            cooldownupgradeprice = upgradefont.render("($" + str(cooldownpthreshold) + ")", True, colour)
            maxupgrade = upgradefont.render("MAX", True, colour)
            mvmmentupgrade = smallerupgradefont.render("Movement speed", True, colour)
            mvmentupgradeprice = upgradefont.render("($" + str(mvmentupgradethreshold) + ")", True, colour)
            scr.blit(moneytext, (1025, 65))

            for projectile in init.projectiles:
                projectile.draw_projectile()

            for ez in easy_balloon:
                ez.draw(scr)

            for fly in fly_balloon:
                fly.draw(scr)

            if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [750, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [750, 40, 225, 65])
            if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [500, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [500, 40, 225, 65])
            if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [250, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [250, 40, 225, 65])

            scr.blit(moneyupgradetext, (750, 50))
            scr.blit(moneyupgradetextprice, (810, 80))
            scr.blit(currentrate, (1025, 100))
            scr.blit(cooldownupgrade, (510, 50))

            if cooldown >= 10:
                scr.blit(maxupgrade, (585, 80))
            else:
                scr.blit(cooldownupgradeprice, (550, 80))
            if move_speed == 50:
                scr.blit(maxupgrade, (335, 80))
            else:
                scr.blit(mvmentupgradeprice, (300, 80))
            scr.blit(mvmmentupgrade, (260, 50))

            # draws respawn screen
            if init.alive == False:
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

                def level_lose():
                    if eas == True:
                        init.alive = True
                        level2(8, 25, 23, 5, 4, 45, score)

                    if med == True:
                        init.alive = True
                        level2(10, 20, 20, 3, 3, 45, score)

                    if har == True:
                        init.alive = True
                        level2(18, 10, 20, 2, 2, 45, score)

                    pygame.time.delay(30)
                    pygame.display.update()

                lose_level = Option('RESPAWN').add.highlight().add.select_listener(lambda _: level_lose())
                losemenu = Option('YOU DIED').add.mouse_menu(screen, mainpos).set_options(
                    [space, lose_level, space, space, back_menu, space, quit])
                losemenu.display_menu()

            if time_of_level <= 0 and init.alive == True:
                level_one = False
                run = False
                pygame.mixer.Sound.set_volume(popsfx, 0)
                pygame.mixer.Sound.set_volume(damagesound, 0)
                pygame.mixer.music.stop()
                pygame.mixer.music.load('victory.wav')
                pygame.mixer.music.set_volume(0.30)
                pygame.mixer.music.play()

                def winlevel():
                    if eas == True:
                        level3(10, 25, 20, 5, 4, 45, score2)

                    if med == True:
                        level3(10, 20, 20, 3, 3, 45, score2)

                    if har == True:
                        level3(10, 10, 20, 2, 2, 45, score2)

                win_level = Option('NEXT LEVEL!', color=green).add.highlight().add.select_listener(
                    lambda _: winlevel())
                winmenu = Option('YOU WIN!').add.mouse_menu(screen, mainpos).set_options(
                    [space, win_level, space, space, back_menu, space, quit])
                winmenu.display_menu()

            pygame.time.delay(30)
            pygame.display.update()

        # instance of the player
        init = Player(50, 446)

        # instance of the easy balloons
        easy_balloon = []
        fly_balloon = []

        # Indicates pygame is running
        run = True
        while run == True:
            pygame.display.flip()
            clock.tick(60)

            # mouse position
            mouse = pygame.mouse.get_pos()
            userInput = pygame.key.get_pressed()

            # creates time delay of 10ms
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.USEREVENT:
                    time_of_level -= 1

                if userInput[pygame.K_ESCAPE]:
                    bloop = pygame.mixer.Sound('bloop.mp3')
                    pygame.mixer.Sound.set_volume(bloop, 0.8)
                    pygame.mixer.Channel(7).play(bloop)
                    menu2.display_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65 and money >= moneypthreshold:
                        money = money - moneypthreshold
                        moneygain = moneygain + 10
                        moneypthreshold = moneypthreshold * 2
                    if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= cooldownpthreshold and cooldown < 10:
                        money = money - cooldownpthreshold
                        cooldown = cooldown + 3
                        tackspeed = tackspeed + 12
                        cooldownpthreshold = cooldownpthreshold * 2
                    if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= mvmentupgradethreshold and move_speed < 50:
                        money = money - mvmentupgradethreshold
                        move_speed = move_speed + 4
                        mvmentupgradethreshold = mvmentupgradethreshold * 2

            init.shoot()
            init.move_player(userInput)
            init.jump_motion(userInput)

            # enemies
            if len(easy_balloon) == 0:
                ez = Easy_Enemy(1100, 550)
                easy_balloon.append(ez)

            if len(fly_balloon) == 0:
                fly = Fly_Enemy(1100, 330)
                fly_balloon.append(fly)

            for ez in easy_balloon:
                ez.move()
                if ez.out_of_bounds():
                    easy_balloon.remove(ez)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar == True:
                    scr.blit(popped, (ez.x, ez.y))
                    pygame.mixer.Channel(3).play(popsfx)
                    easy_balloon.remove(ez)
                    init.hitvar = False
                    money = money + moneygain
                    if speed_balloon <= 24:
                        speed_balloon = speed_balloon + .25
                    score2 = score2 + 5

            for fly in fly_balloon:
                fly.move_fly()
                if fly.out_of_bounds():
                    fly_balloon.remove(fly)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar_fly == True:
                    scr.blit(popped, (fly.x, fly.y))
                    pygame.mixer.Channel(3).play(popsfx)
                    fly_balloon.remove(fly)
                    init.hitvar_fly = False
                    money = money + moneygain
                    if speed_balloon <= 24:
                        speed_balloon = speed_balloon + .25
                    score2 = score2 + 8

            pygame.display.update()

            # Draw Game in Window
            draw_game()

        # closes the pygame window
        pygame.quit()

def level3(speed_balloon, money_gain, move_speed, tower_life, player_life, time_of_level, score2):
    # the way it transitions from level to level
    level_three = True
    # the way it saves difficulty when respawning
    while level_three == True:
        if tower_life == 5:
            eas = True
            med = False
            har = False

        if tower_life == 3:
            eas = False
            med = True
            har = False

        if tower_life == 2:
            eas = False
            med = False
            har = True

        # imports
        import os
        import pygame
        pygame.init()

        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        # variables and assets
        # player
        pygame.mixer.music.stop()
        pygame.mixer.music.load('main.mp3')
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(-1)
        icon_r = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        resize_r = pygame.transform.scale(icon_r, (170, 170))
        icon_l = pygame.image.load(os.path.join("assets", "guyleft.png")).convert_alpha()
        resize_l = pygame.transform.scale(icon_l, (170, 170))
        # background
        background = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "Background3.png")).convert_alpha(), (1350, 800))

        # projectile
        tack = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack.png")),
                                      (50, 50)).convert_alpha()
        tack_l = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack_l.png")),
                                        (50, 50)).convert_alpha()
        # enemies
        green_balloon = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "green_balloon.png")).convert_alpha(), (100, 100))

        red_cluster = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "redcluster.png")).convert_alpha(), (100, 100))
        red_balloon = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "redballoon.png")).convert_alpha(), (50, 50))
        flying_balloon = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "flyingballoon.png")).convert_alpha(), (200, 200))
        popped = pygame.transform.scale(pygame.image.load(os.path.join("assets", "balloonpopped.png")).convert_alpha(),
                                        (200, 200))
        # tower
        tower = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tower.png")).convert_alpha(),
                                       (300, 300))
        towerhealth = tower_life

        popsfx = pygame.mixer.Sound('popsfx.mp3')
        pygame.mixer.Sound.set_volume(popsfx, 0.6)
        damagesound = pygame.mixer.Sound('hurtsfx.mp3')
        pygame.mixer.Sound.set_volume(damagesound, 0.6)

        # jump
        jump = False
        # default character position
        x = 100
        y = 425
        # set windows mode
        scr = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Balloons vs Towers")
        # dimensions of the object
        width = 200
        height = 100

        # velocity / speed of movement
        tackspeed = 38
        hitvar = False
        hitvar_fly = False
        hitvar_cluster = False
        hitvar_clusterm = False
        # colours for buttons
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        # upgrades
        score3 = score2
        money = 0
        moneygain = money_gain
        moneypthreshold = 50
        cooldownpthreshold = 100
        mvmentupgradethreshold = 100
        moneyfont = pygame.font.Font('8-bit.ttf', 30)
        upgradefont = pygame.font.Font('8-bit.ttf', 20)
        smallerupgradefont = pygame.font.Font('8-bit.ttf', 15)
        cooldown = 1
        clusterspawn = False

        # character class
        class Player:
            def __init__(self, x, y):
                # walk
                self.x = x
                self.y = y
                self.spd = move_speed
                self.spd_jump = 14.5
                self.face_right = True
                self.face_left = False

                # jumping
                self.jump = False

                # projectiles
                self.projectiles = []
                self.cooldown = cooldown
                # health
                self.hitbox = (self.x + 30, self.y + 45, 100, 150)
                self.hitvar = hitvar
                self.hitvar_fly = hitvar_fly
                self.hitvar_cluster = hitvar_cluster
                self.hitvar_clusterm = hitvar_clusterm
                self.health = 100
                self.lives = player_life
                self.alive = True

            def move_player(self, userInput):
                if userInput[pygame.K_RIGHT] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_d] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_LEFT] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

                if userInput[pygame.K_a] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

            def draw(self, scr):
                self.hitbox = (self.x + 30, self.y + 35, 100, 170)

                pygame.draw.rect(scr, (255, 0, 0), (self.x + 30, self.y, 100, 10))
                if self.health >= 0:
                    pygame.draw.rect(scr, (0, 255, 0), (self.x + 30, self.y, self.health, 10))

                if self.face_left:
                    scr.blit(resize_l, (self.x, self.y + 20))
                if self.face_right:
                    scr.blit(resize_r, (self.x, self.y + 20))

            def jump_motion(self, userInput):
                if userInput[pygame.K_UP] or userInput[pygame.K_SPACE] or userInput[pygame.K_w] and self.jump is False:
                    self.jump = True
                if self.jump == True:
                    self.y -= self.spd_jump
                    self.spd_jump -= 1
                    if self.spd_jump < -14.5:
                        self.jump = False
                        self.spd_jump = 14.5

            def direction(self):
                if self.face_right:
                    return 1
                if self.face_left:
                    return -1

            def cooldown_func(self):
                if self.cooldown >= 20:
                    self.cooldown = 0
                elif self.cooldown > 0:
                    self.cooldown += 1

            def shoot(self):
                self.hit()
                self.hit_fly()
                self.hit_cluster()
                self.hit_clusterm()
                self.cooldown_func()
                if (userInput[pygame.K_RETURN] and self.cooldown == 0):
                    projectile = Projectile(self.x, self.y, self.direction())
                    self.projectiles.append(projectile)
                    self.cooldown = cooldown
                for projectile in self.projectiles:
                    projectile.move()
                    if projectile.out_of_bounds():
                        self.projectiles.remove(projectile)
                    if self.hitvar_clusterm == True and self.hitvar == True:
                        self.projectiles.append(projectile)
                    if self.hitvar_cluster == True and self.hitvar == True:
                        self.projectiles.append(projectile)
                    if self.hitvar_cluster == True and self.hitvar_clusterm == True:
                        self.projectiles.append(projectile)
                    if self.hitvar_cluster == True and self.hitvar_clusterm == True and self.hitvar == True:
                        self.projectiles.append(projectile)

                    if self.hitvar == True:
                        self.projectiles.remove(projectile)

                    if self.hitvar_fly == True:
                        self.projectiles.remove(projectile)

                    if self.hitvar_cluster == True:
                        self.projectiles.remove(projectile)

                    if self.hitvar_clusterm == True:
                        self.projectiles.remove(projectile)


            def hit(self):
                for ez in easy_balloon:
                    for projectile in self.projectiles:
                        if ez.hitbox[0] < projectile.x < ez.hitbox[0] + ez.hitbox[2] and ez.hitbox[
                            1] < projectile.y + 125 < \
                                ez.hitbox[1] + ez.hitbox[3]:
                            self.hitvar = True

            def hit_fly(self):
                for fly in fly_balloon:
                    for projectile in self.projectiles:
                        if fly.hitbox[0] < projectile.x < fly.hitbox[0] + fly.hitbox[2] and fly.hitbox[
                            1] < projectile.y + 100 < \
                                fly.hitbox[1] + fly.hitbox[3]:
                            self.hitvar_fly = True

            def hit_cluster(self):
                for cluster in cluster_balloon:
                    for projectile in self.projectiles:
                        if cluster.hitbox[0] < projectile.x < cluster.hitbox[0] + cluster.hitbox[2] and cluster.hitbox[
                            1] < projectile.y + 100 < \
                                cluster.hitbox[1] + cluster.hitbox[3]:
                            self.hitvar_cluster = True

            def hit_clusterm(self):
                for clusterm in clusterm_balloon:
                    for projectile in self.projectiles:
                        if clusterm.hitbox[0] < projectile.x < clusterm.hitbox[0] + clusterm.hitbox[2] and clusterm.hitbox[
                            1] < projectile.y + 100 < \
                                clusterm.hitbox[1] + clusterm.hitbox[3]:
                            self.hitvar_clusterm = True

        # thumbtacks
        class Projectile:
            def __init__(self, x, y, direction):
                self.x = x + 15
                self.y = y + 25
                self.direction = direction
                self.hitvar = hitvar
                self.hitvar = hitvar_fly
                self.hitvar = hitvar_cluster
                self.hitvar = hitvar_clusterm
                self.speed = tackspeed

            def draw_projectile(self):
                if self.direction == 1:
                    scr.blit(tack, (self.x + 50, self.y + 75))
                if self.direction == -1:
                    scr.blit(tack_l, (self.x + 50, self.y + 75))

            def move(self):
                if self.direction == 1:
                    self.x += self.speed
                if self.direction == -1:
                    self.x -= self.speed

            def out_of_bounds(self):
                return not (self.x >= 0 and self.x <= 1280)

        # enemy
        class Easy_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = speed_balloon - 4
                # health
                self.hitbox = (self.x, self.y, 100, 100)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 100, 100)

                scr.blit(green_balloon, (self.x, self.y))
                scr.blit(green_balloon, (self.x, self.y))

            def move(self):
                self.hit()
                self.x -= self.spd

            def hit(self):
                if init.hitbox[0] < ez.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < ez.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        class Fly_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = speed_balloon - 6
                # health
                self.hitbox = (self.x, self.y, 200, 200)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 200, 200)
                scr.blit(flying_balloon, (self.x, self.y))

            def move_fly(self):
                self.hit_fly()
                self.x -= self.spd

            def hit_fly(self):
                if init.hitbox[0] < fly.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] > fly.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        # CLUSTER DROPPLINGS
        class Cluster_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = 3
                # health
                self.hitbox = (self.x, self.y, 100, 100)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 200, 200)
                scr.blit(red_balloon, (self.x, self.y))

            def move_cluster(self):
                self.hit_cluster()
                self.x -= self.spd

            def hit_cluster(self):
                if init.hitbox[0] < cluster.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < cluster.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        # CLUSTER MAIN
        class Clusterm_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = -3
                # health
                self.hitbox = (self.x, self.y, 100, 100)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 200, 200)
                scr.blit(red_cluster, (self.x, self.y))

            def move_clusterm(self):
                self.hit_clusterm()
                self.x += self.spd

            def hit_clusterm(self):
                if init.hitbox[0] < clusterm.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < clusterm.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        def draw_game():
            upgrade_bckg = (0, 0, 1280, 150)
            bckg_border = (1000, 0, 1280, 150)
            lives_border = (0, 0, 225, 150)
            scr.fill((0, 0, 0))
            scr.blit(background, (0, -30))
            init.draw(scr)
            scr.blit(tower, (-75, 370))
            pygame.draw.rect(scr, ((230,220,170)), upgrade_bckg, 100)
            pygame.draw.rect(scr, (0, 0, 0), upgrade_bckg, 10)
            pygame.draw.rect(scr, (0, 0, 0), bckg_border, 10)
            pygame.draw.rect(scr, (0, 0, 0), lives_border, 10)
            colour = (0, 0, 0)

            # draw number of lives left for tower and player
            leveltext = smallerupgradefont.render("LEVEL 3", True, colour)
            livestext = smallerupgradefont.render("Lives left:", True, colour)
            numberoflives = moneyfont.render(str(init.lives), True, colour)
            towerlives = moneyfont.render(str(towerhealth), True, colour)
            scr.blit(towerlives, (65, 325))
            scoretext = upgradefont.render("Score:" + str(score3), True, colour)
            scr.blit(leveltext, (18, 187))
            scr.blit(scoretext, (18, 165))
            scr.blit(numberoflives, (15, 75))
            scr.blit(livestext, (15, 50))

            # following lines draw upgrades
            message = 'TIME LEFT: ' + str(time_of_level) + 's'
            timetext = font3.render(message, True, colour)
            scr.blit(timetext, (490, 175))
            moneytext = moneyfont.render("$" + str(money), True, colour)
            moneyupgradetext = upgradefont.render("+10 per pop", True, colour)
            moneyupgradetextprice = upgradefont.render("($" + str(moneypthreshold) + ")", True, colour)
            currentrate = upgradefont.render("(" + str(moneygain) + " per pop)", True, colour)
            cooldownupgrade = upgradefont.render("Tack speed", True, colour)
            cooldownupgradeprice = upgradefont.render("($" + str(cooldownpthreshold) + ")", True, colour)
            maxupgrade = upgradefont.render("MAX", True, colour)
            mvmmentupgrade = smallerupgradefont.render("Movement speed", True, colour)
            mvmentupgradeprice = upgradefont.render("($" + str(mvmentupgradethreshold) + ")", True, colour)
            scr.blit(moneytext, (1025, 65))

            for projectile in init.projectiles:
                projectile.draw_projectile()

            for ez in easy_balloon:
                ez.draw(scr)

            for fly in fly_balloon:
                fly.draw(scr)

            for cluster in cluster_balloon:
                cluster.draw(scr)

            for clusterm in clusterm_balloon:
                clusterm.draw(scr)

            if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [750, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [750, 40, 225, 65])
            if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [500, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [500, 40, 225, 65])
            if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [250, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [250, 40, 225, 65])

            scr.blit(moneyupgradetext, (750, 50))
            scr.blit(moneyupgradetextprice, (810, 80))
            scr.blit(currentrate, (1025, 100))
            scr.blit(cooldownupgrade, (510, 50))

            if cooldown >= 10:
                scr.blit(maxupgrade, (585, 80))
            else:
                scr.blit(cooldownupgradeprice, (550, 80))
            if move_speed == 50:
                scr.blit(maxupgrade, (335, 80))
            else:
                scr.blit(mvmentupgradeprice, (300, 80))
            scr.blit(mvmmentupgrade, (260, 50))

            # draws respawn screen
            if init.alive == False:
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

                def level_lose():
                    if eas == True:
                        init.alive = True
                        level3(10, 25, 20, 5, 4, 45, score3)

                    if med == True:
                        init.alive = True
                        level3(10, 20, 20, 3, 3, 45, score3)

                    if har == True:
                        init.alive = True
                        level3(10, 10, 20, 2, 2, 45, score3)

                    pygame.time.delay(30)
                    pygame.display.update()

                lose_level = Option('RESPAWN').add.highlight().add.select_listener(lambda _: level_lose())
                losemenu = Option('YOU DIED').add.mouse_menu(screen, mainpos).set_options(
                    [space, lose_level, space, space, back_menu, space, quit])
                losemenu.display_menu()

            if time_of_level <= 0 and init.alive == True:
                level_one = False
                run = False
                pygame.mixer.Sound.set_volume(popsfx, 0)
                pygame.mixer.Sound.set_volume(damagesound, 0)
                pygame.mixer.music.stop()
                pygame.mixer.music.load('victory.wav')
                pygame.mixer.music.set_volume(0.30)
                pygame.mixer.music.play()

                def winlevel():
                    if eas == True:
                        init.alive = True
                        level4(10, 25, 13, 5, 4, 60, score3)

                    if med == True:
                        init.alive = True
                        level4(10, 20, 13, 3, 3, 60, score3)

                    if har == True:
                        init.alive = True
                        level4(10, 10, 13, 2, 2, 60, score3)

                win_level = Option('NEXT LEVEL!', color=green).add.highlight().add.select_listener(
                    lambda _: winlevel())

                winmenu = Option('YOU WIN!').add.mouse_menu(screen, mainpos).set_options(
                    [space, win_level, space, space, back_menu, space, quit])
                winmenu.display_menu()

            pygame.time.delay(30)
            pygame.display.update()

        # instance of the player
        init = Player(50, 468)

        # instance of the easy balloons
        easy_balloon = []
        fly_balloon = []
        cluster_balloon = []
        clusterm_balloon = []

        # Indicates pygame is running
        run = True
        while run == True:
            pygame.display.flip()
            clock.tick(60)

            # mouse position
            mouse = pygame.mouse.get_pos()
            userInput = pygame.key.get_pressed()

            # creates time delay of 10ms
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.USEREVENT:
                    time_of_level -= 1

                if userInput[pygame.K_ESCAPE]:
                    bloop = pygame.mixer.Sound('bloop.mp3')
                    pygame.mixer.Sound.set_volume(bloop, 0.8)
                    pygame.mixer.Channel(7).play(bloop)
                    menu2.display_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65 and money >= moneypthreshold:
                        money = money - moneypthreshold
                        moneygain = moneygain + 10
                        moneypthreshold = moneypthreshold * 2
                    if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= cooldownpthreshold and cooldown < 10:
                        money = money - cooldownpthreshold
                        cooldown = cooldown + 3
                        tackspeed = tackspeed + 12
                        cooldownpthreshold = cooldownpthreshold * 2
                    if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= mvmentupgradethreshold and move_speed < 50:
                        money = money - mvmentupgradethreshold
                        move_speed = move_speed + 4
                        mvmentupgradethreshold = mvmentupgradethreshold * 2

            init.shoot()
            init.move_player(userInput)
            init.jump_motion(userInput)

            # enemies
            if len(easy_balloon) == 0:
                ez = Easy_Enemy(1100, 550)
                easy_balloon.append(ez)

            if clusterspawn == True and len(cluster_balloon) == 0:
                cluster_pop = Cluster_Enemy(clusterm.x, clusterm.y)
                cluster_pop1 = Cluster_Enemy(clusterm.x-50, clusterm.y)
                cluster_pop2 = Cluster_Enemy(clusterm.x+50, clusterm.y)
                cluster_balloon.append(cluster_pop)
                cluster_balloon.append(cluster_pop1)
                cluster_balloon.append(cluster_pop2)

                if len(cluster_balloon) == 3:

                    clusterspawn = False

            if len(fly_balloon) == 0:
                fly = Fly_Enemy(1100, 330)
                fly_balloon.append(fly)

            if len(clusterm_balloon) == 0:
                clusterm = Clusterm_Enemy(1100, 550)
                clusterm_balloon.append(clusterm)

            for cluster in cluster_balloon:
                cluster.move_cluster()
                if cluster.out_of_bounds():
                    cluster_balloon.remove(cluster)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    clusterspawn = False
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar_cluster == True:
                    scr.blit(popped, (cluster.x, cluster.y - 75))
                    pygame.mixer.Channel(3).play(popsfx)
                    cluster_balloon.remove(cluster)
                    init.hitvar_cluster = False
                    money = money + moneygain
                    score3 = score3 + 3

            for clusterm in clusterm_balloon:
                clusterm.move_clusterm()
                if clusterm.out_of_bounds():
                    clusterm_balloon.remove(clusterm)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    clusterspawn = False
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar_clusterm == True:
                    clusterspawn = True
                    scr.blit(popped, (clusterm.x, clusterm.y - 75))
                    pygame.mixer.Channel(3).play(popsfx)
                    clusterm_balloon.remove(clusterm)
                    init.hitvar_clusterm = False
                    money = money + moneygain
                    score3 = score3 + 3

            for ez in easy_balloon:
                ez.move()
                if ez.out_of_bounds():
                    easy_balloon.remove(ez)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar == True:
                    scr.blit(popped, (ez.x, ez.y - 75))
                    pygame.mixer.Channel(3).play(popsfx)
                    easy_balloon.remove(ez)
                    init.hitvar = False
                    money = money + moneygain
                    if speed_balloon <= 24:
                        speed_balloon = speed_balloon + .25
                    score3 = score3 + 10

            for fly in fly_balloon:
                fly.move_fly()
                if fly.out_of_bounds():
                    fly_balloon.remove(fly)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar_fly == True:
                    scr.blit(popped, (fly.x, fly.y))
                    pygame.mixer.Channel(3).play(popsfx)
                    fly_balloon.remove(fly)
                    init.hitvar_fly = False
                    money = money + moneygain
                    if speed_balloon <= 24:
                        speed_balloon = speed_balloon + .25
                    score3 = score3 + 8

            pygame.display.update()

            # Draw Game in Window
            draw_game()

        # closes the pygame window
        pygame.quit()

def level4(speed_balloon, money_gain, move_speed, tower_life, player_life, time_of_level, score3):
    # the way it transitions from level to level
    level_four = True
    # the way it saves difficulty when respawning
    while level_four == True:
        if tower_life == 5:
            eas = True
            med = False
            har = False

        if tower_life == 3:
            eas = False
            med = True
            har = False

        if tower_life == 2:
            eas = False
            med = False
            har = True

        # imports
        import os
        import pygame
        pygame.init()

        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        # variables and assets
        # player
        pygame.mixer.music.stop()
        pygame.mixer.music.load('level3.mp3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)
        icon_r = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        resize_r = pygame.transform.scale(icon_r, (170, 170))
        icon_l = pygame.image.load(os.path.join("assets", "guyleft.png")).convert_alpha()
        resize_l = pygame.transform.scale(icon_l, (170, 170))
        # background
        background = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "level35.png")).convert_alpha(), (1350, 800))

        # projectile
        tack = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack.png")),
                                      (50, 50)).convert_alpha()
        tack_l = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack_l.png")),
                                        (50, 50)).convert_alpha()
        # enemies
        green_balloon = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "green_balloon.png")).convert_alpha(), (100, 100))

        red_cluster = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "redcluster.png")).convert_alpha(), (100, 100))
        red_balloon = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "redballoon.png")).convert_alpha(), (50, 50))
        flying_balloon = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "flyingballoon.png")).convert_alpha(), (200, 200))
        popped = pygame.transform.scale(pygame.image.load(os.path.join("assets", "balloonpopped.png")).convert_alpha(),
                                        (200, 200))
        # tower
        tower = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tower.png")).convert_alpha(),
                                       (300, 300))
        towerhealth = tower_life

        popsfx = pygame.mixer.Sound('popsfx.mp3')
        pygame.mixer.Sound.set_volume(popsfx, 0.6)
        damagesound = pygame.mixer.Sound('hurtsfx.mp3')
        pygame.mixer.Sound.set_volume(damagesound, 0.6)

        # jump
        jump = False
        # default character position
        x = 100
        y = 425
        # set windows mode
        scr = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Balloons vs Towers")
        # dimensions of the object
        width = 200
        height = 100

        # velocity / speed of movement
        tackspeed = 30
        hitvar = False
        hitvar_fly = False
        hitvar_cluster = False
        hitvar_clusterm = False
        # colours for buttons
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        # upgrades
        score4 = score3
        money = 0
        moneygain = money_gain
        moneypthreshold = 50
        cooldownpthreshold = 100
        mvmentupgradethreshold = 100
        moneyfont = pygame.font.Font('8-bit.ttf', 30)
        upgradefont = pygame.font.Font('8-bit.ttf', 20)
        smallerupgradefont = pygame.font.Font('8-bit.ttf', 15)
        cooldown = 1
        clusterspawn = False

        # character class
        class Player:
            def __init__(self, x, y):
                # walk
                self.x = x
                self.y = y
                self.spd = move_speed
                self.spd_jump = 18
                self.face_right = True
                self.face_left = False

                # jumping
                self.jump = False

                # projectiles
                self.projectiles = []
                self.cooldown = cooldown
                # health
                self.hitbox = (self.x + 30, self.y + 45, 100, 150)
                self.hitvar = hitvar
                self.hitvar_fly = hitvar_fly
                self.hitvar_cluster = hitvar_cluster
                self.hitvar_clusterm = hitvar_clusterm
                self.health = 100
                self.lives = player_life
                self.alive = True

            def move_player(self, userInput):
                if userInput[pygame.K_RIGHT] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_d] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_LEFT] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

                if userInput[pygame.K_a] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

            def draw(self, scr):
                self.hitbox = (self.x + 30, self.y + 35, 100, 170)

                pygame.draw.rect(scr, (255, 0, 0), (self.x + 30, self.y, 100, 10))
                if self.health >= 0:
                    pygame.draw.rect(scr, (0, 255, 0), (self.x + 30, self.y, self.health, 10))

                if self.face_left:
                    scr.blit(resize_l, (self.x, self.y + 20))
                if self.face_right:
                    scr.blit(resize_r, (self.x, self.y + 20))

            def jump_motion(self, userInput):
                if userInput[pygame.K_UP] or userInput[pygame.K_SPACE] or userInput[pygame.K_w] and self.jump is False:
                    self.jump = True
                if self.jump == True:
                    self.y -= self.spd_jump
                    self.spd_jump -= 1
                    if self.spd_jump < -18:
                        self.jump = False
                        self.spd_jump = 18

            def direction(self):
                if self.face_right:
                    return 1
                if self.face_left:
                    return -1

            def cooldown_func(self):
                if self.cooldown >= 20:
                    self.cooldown = 0
                elif self.cooldown > 0:
                    self.cooldown += 1

            def shoot(self):
                self.hit()
                self.hit_fly()
                self.hit_cluster()
                self.hit_clusterm()
                self.cooldown_func()
                if (userInput[pygame.K_RETURN] and self.cooldown == 0):
                    projectile = Projectile(self.x, self.y, self.direction())
                    self.projectiles.append(projectile)
                    self.cooldown = cooldown
                for projectile in self.projectiles:
                    projectile.move()
                    if projectile.out_of_bounds():
                        self.projectiles.remove(projectile)
                    if self.hitvar_clusterm == True and self.hitvar == True:
                        self.projectiles.append(projectile)
                    if self.hitvar_cluster == True and self.hitvar == True:
                        self.projectiles.append(projectile)
                    if self.hitvar_cluster == True and self.hitvar_clusterm == True:
                        self.projectiles.append(projectile)
                    if self.hitvar_cluster == True and self.hitvar_clusterm == True and self.hitvar == True:
                        self.projectiles.append(projectile)

                    if self.hitvar == True:
                        self.projectiles.remove(projectile)

                    if self.hitvar_fly == True:
                        self.projectiles.remove(projectile)

                    if self.hitvar_cluster == True:
                        self.projectiles.remove(projectile)

                    if self.hitvar_clusterm == True:
                        self.projectiles.remove(projectile)


            def hit(self):
                for ez in easy_balloon:
                    for projectile in self.projectiles:
                        if ez.hitbox[0] < projectile.x < ez.hitbox[0] + ez.hitbox[2] and ez.hitbox[
                            1] < projectile.y + 125 < \
                                ez.hitbox[1] + ez.hitbox[3]:
                            self.hitvar = True

            def hit_fly(self):
                for fly in fly_balloon:
                    for projectile in self.projectiles:
                        if fly.hitbox[0] < projectile.x < fly.hitbox[0] + fly.hitbox[2] and fly.hitbox[
                            1] < projectile.y + 100 < \
                                fly.hitbox[1] + fly.hitbox[3]:
                            self.hitvar_fly = True

            def hit_cluster(self):
                for cluster in cluster_balloon:
                    for projectile in self.projectiles:
                        if cluster.hitbox[0] < projectile.x < cluster.hitbox[0] + cluster.hitbox[2] and cluster.hitbox[
                            1] < projectile.y + 100 < \
                                cluster.hitbox[1] + cluster.hitbox[3]:
                            self.hitvar_cluster = True

            def hit_clusterm(self):
                for clusterm in clusterm_balloon:
                    for projectile in self.projectiles:
                        if clusterm.hitbox[0] < projectile.x < clusterm.hitbox[0] + clusterm.hitbox[2] and clusterm.hitbox[
                            1] < projectile.y + 100 < \
                                clusterm.hitbox[1] + clusterm.hitbox[3]:
                            self.hitvar_clusterm = True

        # thumbtacks
        class Projectile:
            def __init__(self, x, y, direction):
                self.x = x + 15
                self.y = y + 25
                self.direction = direction
                self.hitvar = hitvar
                self.hitvar = hitvar_fly
                self.hitvar = hitvar_cluster
                self.hitvar = hitvar_clusterm
                self.speed = tackspeed

            def draw_projectile(self):
                if self.direction == 1:
                    scr.blit(tack, (self.x + 50, self.y + 75))
                if self.direction == -1:
                    scr.blit(tack_l, (self.x + 50, self.y + 75))

            def move(self):
                if self.direction == 1:
                    self.x += self.speed
                if self.direction == -1:
                    self.x -= self.speed

            def out_of_bounds(self):
                return not (self.x >= 0 and self.x <= 1280)

        # enemy
        class Easy_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = speed_balloon - 4
                # health
                self.hitbox = (self.x, self.y, 100, 100)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 100, 100)

                scr.blit(green_balloon, (self.x, self.y))
                scr.blit(green_balloon, (self.x, self.y))

            def move(self):
                self.hit()
                self.x -= self.spd

            def hit(self):
                if init.hitbox[0] < ez.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < ez.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        class Fly_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = speed_balloon - 6
                # health
                self.hitbox = (self.x, self.y, 200, 200)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 200, 200)
                scr.blit(flying_balloon, (self.x, self.y))

            def move_fly(self):
                self.hit_fly()
                self.x -= self.spd

            def hit_fly(self):
                if init.hitbox[0] < fly.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] > fly.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        # CLUSTER DROPPLINGS
        class Cluster_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = 3
                # health
                self.hitbox = (self.x, self.y, 100, 100)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 200, 200)
                scr.blit(red_balloon, (self.x, self.y))

            def move_cluster(self):
                self.hit_cluster()
                self.x -= self.spd

            def hit_cluster(self):
                if init.hitbox[0] < cluster.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < cluster.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        # CLUSTER MAIN
        class Clusterm_Enemy:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.spd = -3
                # health
                self.hitbox = (self.x, self.y, 100, 100)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 200, 200)
                scr.blit(red_cluster, (self.x, self.y))

            def move_clusterm(self):
                self.hit_clusterm()
                self.x += self.spd

            def hit_clusterm(self):
                if init.hitbox[0] < clusterm.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] < clusterm.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 3
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        def draw_game():
            upgrade_bckg = (0, 0, 1280, 150)
            bckg_border = (1000, 0, 1280, 150)
            lives_border = (0, 0, 225, 150)
            scr.fill((0, 0, 0))
            scr.blit(background, (0, -30))
            init.draw(scr)
            scr.blit(tower, (-75, 370))
            pygame.draw.rect(scr, ((230,220,170)), upgrade_bckg, 100)
            pygame.draw.rect(scr, (0, 0, 0), upgrade_bckg, 10)
            pygame.draw.rect(scr, (0, 0, 0), bckg_border, 10)
            pygame.draw.rect(scr, (0, 0, 0), lives_border, 10)
            colour = (0, 0, 0)

            # draw number of lives left for tower and player
            leveltext = smallerupgradefont.render("LEVEL 4", True, colour)
            livestext = smallerupgradefont.render("Lives left:", True, colour)
            numberoflives = moneyfont.render(str(init.lives), True, colour)
            towerlives = moneyfont.render(str(towerhealth), True, colour)
            scr.blit(towerlives, (65, 325))
            scoretext = upgradefont.render("Score:" + str(score4), True, colour)
            scr.blit(leveltext, (18, 187))
            scr.blit(scoretext, (18, 165))
            scr.blit(numberoflives, (15, 75))
            scr.blit(livestext, (15, 50))

            # following lines draw upgrades
            message = 'TIME LEFT: ' + str(time_of_level) + 's'
            timetext = font3.render(message, True, colour)
            scr.blit(timetext, (490, 175))
            moneytext = moneyfont.render("$" + str(money), True, colour)
            moneyupgradetext = upgradefont.render("+10 per pop", True, colour)
            moneyupgradetextprice = upgradefont.render("($" + str(moneypthreshold) + ")", True, colour)
            currentrate = upgradefont.render("(" + str(moneygain) + " per pop)", True, colour)
            cooldownupgrade = upgradefont.render("Tack speed", True, colour)
            cooldownupgradeprice = upgradefont.render("($" + str(cooldownpthreshold) + ")", True, colour)
            maxupgrade = upgradefont.render("MAX", True, colour)
            mvmmentupgrade = smallerupgradefont.render("Movement speed", True, colour)
            mvmentupgradeprice = upgradefont.render("($" + str(mvmentupgradethreshold) + ")", True, colour)
            scr.blit(moneytext, (1025, 65))

            for projectile in init.projectiles:
                projectile.draw_projectile()

            for ez in easy_balloon:
                ez.draw(scr)

            for fly in fly_balloon:
                fly.draw(scr)

            for cluster in cluster_balloon:
                cluster.draw(scr)

            for clusterm in clusterm_balloon:
                clusterm.draw(scr)

            if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [750, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [750, 40, 225, 65])
            if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [500, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [500, 40, 225, 65])
            if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [250, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [250, 40, 225, 65])

            scr.blit(moneyupgradetext, (750, 50))
            scr.blit(moneyupgradetextprice, (810, 80))
            scr.blit(currentrate, (1025, 100))
            scr.blit(cooldownupgrade, (510, 50))

            if cooldown >= 10:
                scr.blit(maxupgrade, (585, 80))
            else:
                scr.blit(cooldownupgradeprice, (550, 80))
            if move_speed == 50:
                scr.blit(maxupgrade, (335, 80))
            else:
                scr.blit(mvmentupgradeprice, (300, 80))
            scr.blit(mvmmentupgrade, (260, 50))

            # draws respawn screen
            if init.alive == False:
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

                def level_lose():
                    if eas == True:
                        init.alive = True
                        level4(10, 25, 13, 5, 4, 60, score3)

                    if med == True:
                        init.alive = True
                        level4(10, 20, 13, 3, 3, 60, score3)

                    if har == True:
                        init.alive = True
                        level4(10, 10, 13, 2, 2, 60, score3)

                    pygame.time.delay(30)
                    pygame.display.update()

                lose_level = Option('RESPAWN').add.highlight().add.select_listener(lambda _: level_lose())
                losemenu = Option('YOU DIED').add.mouse_menu(screen, mainpos).set_options(
                    [space, lose_level, space, space, back_menu, space, quit])
                losemenu.display_menu()

            if time_of_level <= 0 and init.alive == True:
                level_one = False
                run = False
                pygame.mixer.Sound.set_volume(popsfx, 0)
                pygame.mixer.Sound.set_volume(damagesound, 0)
                pygame.mixer.music.stop()
                pygame.mixer.music.load('victory.wav')
                pygame.mixer.music.set_volume(0.30)
                pygame.mixer.music.play()

                def winlevel():
                    if eas == True:
                        init.alive = True
                        level5(score4)

                    if med == True:
                        init.alive = True
                        level5(score4)

                    if har == True:
                        init.alive = True
                        level5(score4)

                win_level = Option('NEXT LEVEL!', color=green).add.highlight().add.select_listener(
                    lambda _: winlevel())

                winmenu = Option('YOU WIN!').add.mouse_menu(screen, mainpos).set_options(
                    [space, win_level, space, space, back_menu, space, quit])
                winmenu.display_menu()

            pygame.time.delay(30)
            pygame.display.update()

        # instance of the player
        init = Player(50, 468)

        # instance of the easy balloons
        easy_balloon = []
        fly_balloon = []
        cluster_balloon = []
        clusterm_balloon = []

        # Indicates pygame is running
        run = True
        while run == True:
            pygame.display.flip()
            clock.tick(60)

            # mouse position
            mouse = pygame.mouse.get_pos()
            userInput = pygame.key.get_pressed()

            # creates time delay of 10ms
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.USEREVENT:
                    time_of_level -= 1

                if userInput[pygame.K_ESCAPE]:
                    bloop = pygame.mixer.Sound('bloop.mp3')
                    pygame.mixer.Sound.set_volume(bloop, 0.8)
                    pygame.mixer.Channel(7).play(bloop)
                    menu2.display_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65 and money >= moneypthreshold:
                        money = money - moneypthreshold
                        moneygain = moneygain + 10
                        moneypthreshold = moneypthreshold * 2
                    if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= cooldownpthreshold and cooldown < 10:
                        money = money - cooldownpthreshold
                        cooldown = cooldown + 3
                        tackspeed = tackspeed + 12
                        cooldownpthreshold = cooldownpthreshold * 2
                    if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= mvmentupgradethreshold and move_speed < 50:
                        money = money - mvmentupgradethreshold
                        move_speed = move_speed + 4
                        mvmentupgradethreshold = mvmentupgradethreshold * 2

            init.shoot()
            init.move_player(userInput)
            init.jump_motion(userInput)

            # enemies
            if len(easy_balloon) == 0:
                ez = Easy_Enemy(1100, 550)
                easy_balloon.append(ez)

            if clusterspawn == True and len(cluster_balloon) == 0:
                cluster_pop = Cluster_Enemy(clusterm.x, clusterm.y)
                cluster_pop1 = Cluster_Enemy(clusterm.x-50, clusterm.y)
                cluster_pop2 = Cluster_Enemy(clusterm.x+50, clusterm.y)
                cluster_balloon.append(cluster_pop)
                cluster_balloon.append(cluster_pop1)
                cluster_balloon.append(cluster_pop2)

                if len(cluster_balloon) == 3:

                    clusterspawn = False

            if len(fly_balloon) == 0:
                fly = Fly_Enemy(1100, 330)
                fly_balloon.append(fly)

            if len(clusterm_balloon) == 0:
                clusterm = Clusterm_Enemy(1100, 550)
                clusterm_balloon.append(clusterm)

            for cluster in cluster_balloon:
                cluster.move_cluster()
                if cluster.out_of_bounds():
                    cluster_balloon.remove(cluster)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    clusterspawn = False
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar_cluster == True:
                    scr.blit(popped, (cluster.x, cluster.y - 75))
                    pygame.mixer.Channel(3).play(popsfx)
                    cluster_balloon.remove(cluster)
                    init.hitvar_cluster = False
                    money = money + moneygain
                    score4 = score4 + 3

            for clusterm in clusterm_balloon:
                clusterm.move_clusterm()
                if clusterm.out_of_bounds():
                    clusterm_balloon.remove(clusterm)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    clusterspawn = False
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar_clusterm == True:
                    clusterspawn = True
                    scr.blit(popped, (clusterm.x, clusterm.y - 75))
                    pygame.mixer.Channel(3).play(popsfx)
                    clusterm_balloon.remove(clusterm)
                    init.hitvar_clusterm = False
                    money = money + moneygain
                    score4 = score4 + 3

            for ez in easy_balloon:
                ez.move()
                if ez.out_of_bounds():
                    easy_balloon.remove(ez)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar == True:
                    scr.blit(popped, (ez.x, ez.y - 75))
                    pygame.mixer.Channel(3).play(popsfx)
                    easy_balloon.remove(ez)
                    init.hitvar = False
                    money = money + moneygain
                    if speed_balloon <= 24:
                        speed_balloon = speed_balloon + .25
                    score4 = score4 + 10

            for fly in fly_balloon:
                fly.move_fly()
                if fly.out_of_bounds():
                    fly_balloon.remove(fly)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar_fly == True:
                    scr.blit(popped, (fly.x, fly.y))
                    pygame.mixer.Channel(3).play(popsfx)
                    fly_balloon.remove(fly)
                    init.hitvar_fly = False
                    money = money + moneygain
                    if speed_balloon <= 24:
                        speed_balloon = speed_balloon + .25
                    score4 = score4 + 8

            pygame.display.update()

            # Draw Game in Window
            draw_game()

        # closes the pygame window
        pygame.quit()

def level5(score4):
    # final level
    # the way it transitions from level to level
    level_four = True
    # the way it saves difficulty when respawning
    while level_four == True:

        tower_life = 1
        # imports
        import os
        import pygame
        pygame.init()

        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        move_speed = 20
        player_life = 1
        # variables and assets
        # player
        pygame.mixer.music.stop()
        icon_r = pygame.image.load(os.path.join("assets", "guy.png")).convert_alpha()
        resize_r = pygame.transform.scale(icon_r, (170, 170))
        icon_l = pygame.image.load(os.path.join("assets", "guyleft.png")).convert_alpha()
        resize_l = pygame.transform.scale(icon_l, (170, 170))
        # background
        background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "level4.png")).convert_alpha(), (1350, 800))

        # projectile
        tack = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack.png")),
                                      (50, 50)).convert_alpha()
        tack_l = pygame.transform.scale(pygame.image.load(os.path.join("assets", "thumbtack_l.png")),
                                        (50, 50)).convert_alpha()
        # enemies
        boss = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "boss.png")).convert_alpha(), (600, 400))

        popped = pygame.transform.scale(pygame.image.load(os.path.join("assets", "balloonpopped.png")).convert_alpha(),
                                        (200, 200))
        # tower
        tower = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tower.png")).convert_alpha(),
                                       (300, 300))
        towerhealth = tower_life


        pygame.mixer.music.load('level4.wav')
        pygame.mixer.music.play(-1)
        popsfx = pygame.mixer.Sound('popsfx.mp3')
        pygame.mixer.Sound.set_volume(popsfx, 0.6)
        damagesound = pygame.mixer.Sound('hurtsfx.mp3')
        pygame.mixer.Sound.set_volume(damagesound, 0.6)

        # jump
        jump = False
        # default character position
        x = 100
        y = 425
        # set windows mode
        scr = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Balloons vs Towers")
        # dimensions of the object
        width = 200
        height = 100

        # velocity / speed of movement
        tackspeed = 38
        hitvar = False

        # colours for buttons
        color_light = (170, 170, 170)
        color_dark = (100, 100, 100)
        # upgrades
        score5 = score4
        money = 0
        moneygain = 10
        money_gain = 10
        moneypthreshold = 50
        cooldownpthreshold = 100
        mvmentupgradethreshold = 100
        moneyfont = pygame.font.Font('8-bit.ttf', 30)
        upgradefont = pygame.font.Font('8-bit.ttf', 20)
        smallerupgradefont = pygame.font.Font('8-bit.ttf', 15)
        cooldown = 1


        # character class
        class Player:
            def __init__(self, x, y):
                # walk
                self.x = x
                self.y = y
                self.spd = move_speed
                self.spd_jump = 14.5
                self.face_right = True
                self.face_left = False

                # jumping
                self.jump = False

                # projectiles
                self.projectiles = []
                self.cooldown = cooldown
                # health
                self.hitbox = (self.x + 30, self.y + 45, 100, 150)
                self.hitvar = hitvar
                self.health = 100
                self.lives = player_life
                self.alive = True

            def move_player(self, userInput):
                if userInput[pygame.K_RIGHT] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_d] and self.x < 1280 - width:
                    self.spd = move_speed
                    self.x += self.spd
                    self.face_right = True
                    self.face_left = False

                if userInput[pygame.K_LEFT] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

                if userInput[pygame.K_a] and self.x > 0:
                    self.spd = move_speed
                    self.x -= self.spd
                    self.face_right = False
                    self.face_left = True

            def draw(self, scr):
                self.hitbox = (self.x + 30, self.y + 35, 100, 170)

                pygame.draw.rect(scr, (255, 0, 0), (self.x + 30, self.y, 100, 10))
                if self.health >= 0:
                    pygame.draw.rect(scr, (0, 255, 0), (self.x + 30, self.y, self.health, 10))

                if self.face_left:
                    scr.blit(resize_l, (self.x, self.y + 20))
                if self.face_right:
                    scr.blit(resize_r, (self.x, self.y + 20))

            def jump_motion(self, userInput):
                if userInput[pygame.K_UP] or userInput[pygame.K_SPACE] or userInput[pygame.K_w] and self.jump is False:
                    self.jump = True
                if self.jump == True:
                    self.y -= self.spd_jump
                    self.spd_jump -= 1
                    if self.spd_jump < -14.5:
                        self.jump = False
                        self.spd_jump = 14.5

            def direction(self):
                if self.face_right:
                    return 1
                if self.face_left:
                    return -1

            def cooldown_func(self):
                if self.cooldown >= 20:
                    self.cooldown = 0
                elif self.cooldown > 0:
                    self.cooldown += 1

            def shoot(self):
                self.hit()
                self.cooldown_func()
                if (userInput[pygame.K_RETURN] and self.cooldown == 0):
                    projectile = Projectile(self.x, self.y, self.direction())
                    self.projectiles.append(projectile)
                    self.cooldown = cooldown
                for projectile in self.projectiles:
                    projectile.move()
                    if projectile.out_of_bounds():
                        self.projectiles.remove(projectile)

                    if self.hitvar == True:
                        self.projectiles.remove(projectile)

            def hit(self):
                for ez in easy_balloon:
                    for projectile in self.projectiles:
                        if ez.hitbox[0] < projectile.x < ez.hitbox[0] + ez.hitbox[2] and ez.hitbox[
                            1] < projectile.y + 100 < \
                                ez.hitbox[1] + ez.hitbox[3]:
                            self.hitvar = True

        # thumbtacks
        class Projectile:
            def __init__(self, x, y, direction):
                self.x = x + 15
                self.y = y + 25
                self.direction = direction
                self.hitvar = hitvar
                self.speed = tackspeed

            def draw_projectile(self):
                if self.direction == 1:
                    scr.blit(tack, (self.x + 50, self.y + 75))
                if self.direction == -1:
                    scr.blit(tack_l, (self.x + 50, self.y + 75))

            def move(self):
                if self.direction == 1:
                    self.x += self.speed
                if self.direction == -1:
                    self.x -= self.speed

            def out_of_bounds(self):
                return not (self.x >= 0 and self.x <= 1280)

        # one big slow boss that takes 60 shots to kill (need upgrade)
        class Boss:
            def __init__(self, x, y):
                self.x = 1100
                self.y = 300
                self.spd = 1
                # health
                self.hitbox = (self.x, self.y, 1100, 300)

            def draw(self, scr):
                self.hitbox = (self.x, self.y, 1100, 300)
                scr.blit(boss, (self.x, self.y))

            def move(self):
                self.hit()
                self.x -= self.spd

            def hit(self):
                if init.hitbox[0] > ez.x + 32 < init.hitbox[0] + init.hitbox[2] and init.hitbox[1] > ez.y + 32 < \
                        init.hitbox[1] + init.hitbox[3]:
                    if init.health > 0:
                        init.health -= 99
                        if init.health % 5 == 0:
                            pygame.mixer.Channel(2).play(damagesound)
                        if init.health <= 0 and init.lives > 0:
                            pygame.mixer.Channel(0).play(lifelostsfx)
                            init.lives -= 1
                            init.health = 100
                        elif init.health == 1 and init.lives == 1:
                            init.alive = False

            def out_of_bounds(self):

                return not (self.x >= 0 and self.x <= 1280)

        def draw_game():
            upgrade_bckg = (0, 0, 1280, 150)
            bckg_border = (1000, 0, 1280, 150)
            lives_border = (0, 0, 225, 150)
            scr.fill((0, 0, 0))
            scr.blit(background, (0, -30))
            init.draw(scr)
            scr.blit(tower, (-75, 350))
            pygame.draw.rect(scr, ((230,220,170)), upgrade_bckg, 100)
            pygame.draw.rect(scr, (0, 0, 0), upgrade_bckg, 10)
            pygame.draw.rect(scr, (0, 0, 0), bckg_border, 10)
            pygame.draw.rect(scr, (0, 0, 0), lives_border, 10)
            colour = (0, 0, 0)

            # draw number of lives left for tower and player
            leveltext = smallerupgradefont.render("LEVEL 4", True, colour)
            livestext = smallerupgradefont.render("Lives left:", True, colour)
            numberoflives = moneyfont.render(str(init.lives), True, colour)
            towerlives = moneyfont.render(str(towerhealth), True, colour)
            scr.blit(towerlives, (65, 325))
            scoretext = upgradefont.render("Score:" + str(score4), True, colour)
            scr.blit(leveltext, (18, 187))
            scr.blit(scoretext, (18, 165))
            scr.blit(numberoflives, (15, 75))
            scr.blit(livestext, (15, 50))

            # following lines draw upgrades
            moneytext = moneyfont.render("$" + str(money), True, colour)
            moneyupgradetext = upgradefont.render("+10 per pop", True, colour)
            moneyupgradetextprice = upgradefont.render("($" + str(moneypthreshold) + ")", True, colour)
            currentrate = upgradefont.render("(" + str(moneygain) + " per pop)", True, colour)
            cooldownupgrade = upgradefont.render("Tack speed", True, colour)
            cooldownupgradeprice = upgradefont.render("($" + str(cooldownpthreshold) + ")", True, colour)
            maxupgrade = upgradefont.render("MAX", True, colour)
            mvmmentupgrade = smallerupgradefont.render("Movement speed", True, colour)
            mvmentupgradeprice = upgradefont.render("($" + str(mvmentupgradethreshold) + ")", True, colour)
            scr.blit(moneytext, (1025, 65))

            for projectile in init.projectiles:
                projectile.draw_projectile()

            for ez in easy_balloon:
                ez.draw(scr)

            if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [750, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [750, 40, 225, 65])
            if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [500, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [500, 40, 225, 65])
            if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[1] <= 40 + 65:
                pygame.draw.rect(scr, color_light, [250, 40, 225, 65])
            else:
                pygame.draw.rect(scr, color_dark, [250, 40, 225, 65])

            scr.blit(moneyupgradetext, (750, 50))
            scr.blit(moneyupgradetextprice, (810, 80))
            scr.blit(currentrate, (1025, 100))
            scr.blit(cooldownupgrade, (510, 50))

            if cooldown >= 10:
                scr.blit(maxupgrade, (585, 80))
            else:
                scr.blit(cooldownupgradeprice, (550, 80))
            if move_speed == 50:
                scr.blit(maxupgrade, (335, 80))
            else:
                scr.blit(mvmentupgradeprice, (300, 80))
            scr.blit(mvmmentupgrade, (260, 50))

            # draws respawn screen
            if init.alive == False:
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

                def level_lose():
                    level5(score4)
                    pygame.time.delay(30)
                    pygame.display.update()

                lose_level = Option('RESPAWN').add.highlight().add.select_listener(lambda _: level_lose())
                losemenu = Option('YOU DIED').add.mouse_menu(screen, mainpos).set_options(
                    [space, lose_level, space, space, back_menu, space, quit])
                losemenu.display_menu()


            pygame.time.delay(30)
            pygame.display.update()

        # instance of the player
        init = Player(50, 450)

        # instance of the easy balloons
        boss_lives = []
        easy_balloon = []

        # Indicates pygame is running
        run = True
        while run == True:
            pygame.display.flip()
            clock.tick(60)

            # mouse position
            mouse = pygame.mouse.get_pos()
            userInput = pygame.key.get_pressed()

            # creates time delay of 10ms
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if userInput[pygame.K_ESCAPE]:
                    bloop = pygame.mixer.Sound('bloop.mp3')
                    pygame.mixer.Sound.set_volume(bloop, 0.8)
                    pygame.mixer.Channel(7).play(bloop)
                    menu2.display_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    move_speed = 20
                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 750 <= mouse[0] <= 750 + 225 and 40 <= mouse[1] <= 40 + 65 and money >= moneypthreshold:
                        money = money - moneypthreshold
                        moneygain = moneygain + 10
                        moneypthreshold = moneypthreshold * 2
                    if 500 <= mouse[0] <= 500 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= cooldownpthreshold and cooldown < 10:
                        money = money - cooldownpthreshold
                        cooldown = cooldown + 3
                        tackspeed = tackspeed + 12
                        cooldownpthreshold = cooldownpthreshold * 2
                    if 250 <= mouse[0] <= 250 + 225 and 40 <= mouse[
                        1] <= 40 + 65 and money >= mvmentupgradethreshold and move_speed < 50:
                        money = money - mvmentupgradethreshold
                        move_speed = move_speed + 4
                        mvmentupgradethreshold = mvmentupgradethreshold * 2

            init.shoot()
            init.move_player(userInput)
            init.jump_motion(userInput)

            # calculates the hit by the boss taken
            if len(easy_balloon) == 0:
                boss_lives = 60
                ez = Boss(1100, 280)
                easy_balloon.append(ez)

            # when all lives are out final screen
            if boss_lives == 0:
                level_four = False
                run = False
                pygame.mixer.Sound.set_volume(popsfx, 0)
                pygame.mixer.Sound.set_volume(damagesound, 0)
                pygame.mixer.music.stop()
                pygame.mixer.music.load('victory.wav')
                pygame.mixer.music.set_volume(0.30)
                pygame.mixer.music.play()

                # calculates score on final menu
                final_score = Option('TOTAL SCORE:' + str(score5))
                winmenu = Option('YOU WIN!').add.mouse_menu(screen, mainpos).set_options(
                    [space, final_score, space, space,space,space,back_menu, quit])
                winmenu.display_menu()
                pygame.time.delay(30)
                pygame.display.update()

            for ez in easy_balloon:
                ez.move()
                if ez.out_of_bounds():
                    easy_balloon.remove(ez)
                    towerhealth = towerhealth - 1
                    pygame.mixer.Channel(1).play(towerlifelostsfx)
                    if towerhealth == 0:
                        init.alive = False
                        towerhealth = tower_life

                if init.hitvar == True:
                    boss_lives -= 1
                    pygame.mixer.Channel(3).play(popsfx)
                    init.hitvar = False
                    money = money + moneygain
                    score5 = score5 + 5

            pygame.display.update()

            # Draw Game in Window
            draw_game()

        # closes the pygame window
        pygame.quit()

# function for quitting menus
def quit_menu(menu: Menu):
    time.sleep(0.25)
    menu.run_display = False
    Option.input.reset()

def quit_menu2(menu: Menu):
    time.sleep(0.25)
    menu2.run_display = False
    Option.input.reset()

def quit_sidemenu(menu: Menu):
    time.sleep(0.25)
    menu.run_display = False
    Option.input.reset()

def quit_game(menu: Menu):
    sys.exit()

# music and sounds
def mute_music():
    pygame.mixer.music.pause()

def unmute_music():
    pygame.mixer.music.unpause()

volumeMAIN = Option('MUTE MUSIC').add.highlight().add.select_listener(lambda _: mute_music())
volumeSFX = Option('UNMUTE MUSIC').add.highlight().add.select_listener(lambda _: unmute_music())

def music_player():
    pygame.mixer.music.load('menu.mp3')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

# Back to Main Menu
back1 = Option('Back To Main Menu').add.highlight().add.select_listener(lambda _: quit_menu(options))
back2 = Option('Back To Main Menu').add.highlight().add.select_listener(lambda _: quit_menu(credits))
back4 = Option('Back To Options Menu').add.highlight().add.select_listener(lambda _: quit_sidemenu(Controls))
back5 = Option('Back To Credits Menu').add.highlight().add.select_listener(lambda _: quit_sidemenu(song_credits))
back_to_game = Option('Back To Game', color=blue).add.highlight().add.select_listener(lambda _: quit_menu2(menu2))

# variable to start the game
start = Option('Start Game', color=blue).add.highlight().add.select_listener(lambda _: startgame())

# Control menu
space = Option(' ')
control1 = Option('MOVE FORWARD [D OR RIGHT ARROW]')
control2 = Option('MOVE BACKWARD [A OR LEFT ARROW]')
control3 = Option('JUMP [SPACE OR W OR UP ARROW]')
control4 = Option('SHOOT [ENTER]')
control5 = Option('OPTIONS [ESCAPE]')
Controls = Option('Controls', color=white).add.mouse_menu(screen, mainpos2, background_color=orange).set_options(
    [space, control1, control2, control3, control4, control5, space, space, space,back4]).add.highlight().add.select_listener(
    lambda _: Option.input.reset())

# options menu code
options = Option('Options', color=orange).add.mouse_menu(screen, mainpos2, background_color=orange).set_options(
    [space, space, volumeMAIN, space, volumeSFX, space, space, Controls,
     back1]).add.highlight().add.select_listener(lambda _: Option.input.reset())

# Credits code
credit = Option('CREATED BY PETER AND EGOR', color=white)
credit2 = Option('ICS3U1-01 CPT', color=white)
credit3 = Option('BALLOONS VS TOWERS', color=white)
credspace = Option(' ', color=white)

scredit0 = Option('All Music Done By kleffon', color=white)
scredit1 = Option('1. unrenovated taco bell', color=white)
scredit2 = Option('2. tutorial', color=white)
scredit3 = Option('3. BATTLE!', color=white)
scredit4 = Option('4. BOSS', color=white)
song_credits = Option('Song Credits', color=white).add.mouse_menu(screen, mainpos2, background_color=blue).set_options(
    [scredit0, credspace, scredit1, scredit2, scredit3, scredit4, space, back5]).add.highlight().add.select_listener(
    lambda _: Option.input.reset())

credits = Option('Credits', color=green).add.mouse_menu(screen, mainpos2, background_color=black).set_options(
    [space, credit3, credit2, credit, credspace, song_credits, credspace, space, space,space,
     back2]).add.highlight().add.select_listener(lambda _: Option.input.reset())

# Exit the game
quit = Option('Quit', color=red).add.highlight().add.select_listener(lambda _: quit_game(menu))
quit2 = Option('Quit', color=red).add.highlight().add.select_listener(lambda _: quit_game(menu2))

# back to menu func
def back_to_menu():
    run = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load('menu.mp3')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
    menu.display_menu()
    pygame.display.update()

back_menu = Option('Back To Main Menu', color=blue).add.highlight().add.select_listener(lambda _: back_to_menu())

# menu with all the options
menu = Option('BALLOONS VS TOWERS').add.mouse_menu(screen, mainpos).set_options([space, start, space, options, space, credits, space, quit])
menu2 = Option('PAUSED').add.mouse_menu(screen, mainpos2).set_options([space,back_menu,space,back_to_game, space, options, space, credits, space, quit])

# main code
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                music_player()
                menu.display_menu()

        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    splashscreen(600, 175)
    pygame.display.update()