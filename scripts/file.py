def game(Spaceship):
    import sqlite3
    import pygame
    from pygame import mixer
    from mainMenu import mainMenu
    from time import sleep

    pygame.init()
    mixer.init()

    height = 700
    width = 500
    move_bullet = False

    def updateMoney(score):
            con = sqlite3.connect('data.db')
            cur = con.cursor()
            cur.execute("Select * from mn")
            data = cur.fetchall()
            for row in data:
                    cur.execute('''
                UPDATE mn
                SET money =  
            ''' + str(int(row[0]) + score))
            con.commit()
            con.close()

    x = 230
    y = 500
    bulletX = 260
    bulletY = 530

    alien = pygame.image.load("img/alien.png")
    alienX = 230
    alienY = 100
    hide = False
    
    laser_bullet = pygame.image.load("img/laser_bullet.png")
    space_ship = pygame.image.load(Spaceship)
    to_right = False

    background = pygame.image.load("img/background.jpg")
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("space invaders")
    score = 0

    font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 32)
    level_of_the_game = 1
    run = True

    def isCollide(x, y, x2, y2, width, height, width2, height2):
        return x < x2 + width2 and x + width > x2 and y < y2 + height2 and height + y > y2

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                updateMoney(score)
                mainMenu()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not move_bullet:
                        mixer.music.load("sound/laser-shoot.wav")
                        mixer.music.set_volume(1)
                        mixer.music.play()
                        move_bullet = True
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            if not x <= 0:
                if not move_bullet:
                    bulletX -= 3
                x -= 3
        if key_pressed[pygame.K_RIGHT]:
            if not x >= 440:
                if not move_bullet:
                    bulletX += 3
                x += 3
        if move_bullet and bulletY >= 0:
            if isCollide(bulletX, bulletY, alienX, alienY, 8, 16, 64, 64):
                level_of_the_game += 0.2
                score += 1
                hide = True
                alienX = 230
                alienY = 100
                hide = False
            bulletY -= 9
        else:
            move_bullet = False
            bulletY = 530
            bulletX = x + 30
        if not alienX <= 0 and not to_right:
            to_right = False
            alienX -= level_of_the_game
        elif alienX <= 0:
            alienY += 20
            to_right = True
        if not alienX >= 440 and to_right:
            to_right = True
            alienX += level_of_the_game
        elif alienX >= 440:
            alienY += 20
            to_right = False
        if isCollide(x, y, alienX, alienY, 64, 64, 64, 64):
            mixer.music.load("sound/invaderkilled.wav")
            mixer.music.set_volume(1)
            mixer.music.play()
            sleep(2)
            updateMoney(score)
            run = False
            mainMenu()
            quit()

        screen.blit(background, (0, 0))
        screen.blit(laser_bullet, (bulletX, bulletY))
        screen.blit(space_ship, (x, y))

        text = font.render(str(score), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (240, 100)
        screen.blit(text, textRect)

        if not hide:
            screen.blit(alien, (alienX, alienY))
        pygame.display.flip()

if __name__ == "__main__":
    print("please run the main menu file!")