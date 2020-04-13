import pygame
pygame.init()
#Shneaks first game using pygame library
#creating the window the game will play on 
win = pygame.display.set_mode((500, 500))
#What will be displayed in the bar at the top of the window we have created 
pygame.display.set_caption("MAGA 2020")

icon = pygame.image.load('videogame.png')
pygame.display.set_icon(icon)


#Screen width integers for use later 
screenWidth = 500
screenHeight = 500 

x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10 

#Running the game
run = True
while run:
    #time delay for start of game 
    pygame.time.delay(100)
    #ability to end the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #importing key pressing 
    keys = pygame.key.get_pressed()
        
    #creating keystrokes for up, down, left, right
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    #when jumping we do not want keys to go up and down
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel 
        if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    #quad func for jump       
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
        #move downward after jump
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10 
    #filling background colour with black (0, 0, 0) 
    win.fill((0, 0, 0))
    #green square, (rgb  0, 255, 0) 
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()



                           

