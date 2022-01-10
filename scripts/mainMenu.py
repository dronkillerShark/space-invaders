def mainMenu():  
    from file import game
    from store import store
    import pygame
    from pygame import mixer
    import sqlite3

    pygame.init()
    mixer.init()
 
    height = 500
    width = 700

    def getAlienImgSource():
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('Select * from spaceShips')
        data = cur.fetchall()
        for row in data:
            if row[2] == str(1):
                if int(row[1]) == 1:
                    return 'img/spaceship.png'
            elif int(row[1]) == 1:
                    return 'img/spaceship (' + str(int(row[2]) - 1) + ').png'
        con.commit()
        con.close()

    background = pygame.image.load("img/background.jpg")
    alien = pygame.image.load("img/alien (2).png")
    alien2 = pygame.image.load("img/alien (1).png")
    alien3 = pygame.image.load("img/alien.png")
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("space invaders")

    font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 32)
    font2 = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 16)
    text = font.render("space invaders", True, (255, 255, 255))
    text2 = font2.render("press space to start", True, (255, 255, 255))
    text3 = font2.render("press enter to go to the store", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect.center = (350, 200)
    textRect2.center = (365, 240)
    textRect3.center = (365, 300)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                    store()
                    quit()
                if event.key == pygame.K_SPACE:
                    run = False
                    game(getAlienImgSource())
                    quit()
        screen.blit(background, (0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(alien, (200, 60))
        screen.blit(alien, (300, 400))
        screen.blit(alien, (60, 300))
        screen.blit(alien2, (500, 100))
        screen.blit(alien2, (440, 250))
        screen.blit(alien2, (30, 150))
        screen.blit(alien3, (300, 270))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)

        pygame.display.flip()

mainMenu()