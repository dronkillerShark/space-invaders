def store():
    import sqlite3
    import pygame
    from mainMenu import mainMenu
    pygame.init()

    height = 500
    width = 700
    money = 0

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("store")
    background = pygame.image.load("img/background.jpg")
    spaceShip = pygame.image.load("img/spaceship.png")
    spaceShip1 = pygame.image.load("img/spaceship (1).png")
    spaceShip2 = pygame.image.load("img/spaceship (2).png")
    spaceShip3 = pygame.image.load("img/spaceship (3).png")
    spaceShip4 = pygame.image.load("img/spaceship (4).png")
    coin = pygame.image.load("img/dollar.png")

    def newText(value, x, y, r, g, b):
        font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 10)
        text = font.render(str(value), True, (r, g, b))
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)
    def getData(num):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('Select * from spaceShips')
        data = cur.fetchall()
        for row in data:
            if row[2] == str(num):
                return row
        con.commit()
        con.close()

    def getSpaceShipNum():
        count = 0
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('Select * from spaceShips')
        data = cur.fetchall()
        for row in data:
            count += 1
        con.commit()
        con.close()
        return count
        
    
    def setData(newValue, num, el):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('''UPDATE spaceShips
        set ''' + str(el) + ' = ' + str(newValue) + ' \nWHERE num = ' + str(num))
        con.commit()
        con.close()

    def clickedObj(x, y, num):
        if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if x < pos[0] + 5 and x + 64 > pos[0] and y < pos[1] + 5 and 64 + y > pos[1]: 
                    if int(getData(num)[0]) == 1:
                        for spc in range(1, getSpaceShipNum() + 1):
                            getSpaceShipNum()
                            if(int(getData(spc)[1]) == 1):
                                setData('False', spc, 'isSelected')
                        
                        setData('True', num, 'isSelected')
                    else:
                        con = sqlite3.connect('data.db')
                        cur = con.cursor()
                        cur.execute('Select * from mn')
                        data = cur.fetchall()
                        con.commit()
                        con.close()
                        if (int(data[0][0]) - 500) < 0:
                            return 500
                        else:
                            con = sqlite3.connect('data.db')
                            cur = con.cursor()
                            cur.execute('''
                            UPDATE mn
                            SET money = ''' + str(int(data[0][0]) - 500))  
                            con.commit()
                            con.close()
                            setData('True', num, 'isOwned')
                        
        if int(getData(num)[0]) == 1:
            if int(getData(num)[1]) == 1:
                return 'selected'
            else:
                return 'owned'
        if int(getData(num)[0]) == 0:
                return 500   

    run = True
    while run:
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute("Select * from mn")

        data = cur.fetchall()
        for row in data:
            money = row[0]
        con.commit()
        con.close()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mainMenu()
                quit()
        screen.blit(background, (0, 0))
        screen.blit(spaceShip, (50, 50))
        newText(clickedObj(50, 50, 1), 90, 140, 255, 255, 255)
        screen.blit(coin, (50, 130))
        screen.blit(spaceShip1, (300, 50))
        newText(clickedObj(300, 50, 2), 340, 140, 255, 255, 255)
        screen.blit(coin, (300, 130))
        screen.blit(spaceShip2, (600, 50))
        newText(clickedObj(600, 50, 3), 640, 140, 255, 255, 255)
        screen.blit(coin, (600, 130))
        newText(clickedObj(300, 200, 4), 340, 310, 255, 255, 255)
        screen.blit(spaceShip3, (300, 200))
        screen.blit(coin, (300, 300))
        screen.blit(spaceShip4, (50, 200))
        screen.blit(coin, (50, 300))
        newText(clickedObj(50, 200, 5), 90, 310, 255, 255, 255)
        screen.blit(coin, (10, 20))
        newText(money, 35, 30, 255, 255, 255)

        pygame.display.flip()

if __name__ == "__main__":
    print("please run the main menu file!")