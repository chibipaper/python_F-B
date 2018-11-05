import pygame
def display_map():
    W = int(2003*0.25)
    H = int(2500*0.25)
    introScreenImage = pygame.image.load("map.png")
    introScreenImage = pygame.transform.smoothscale(introScreenImage, (W, H))
    screen = pygame.display.set_mode((W+300,H))
    screen.blit(introScreenImage, (300,0))
    pygame.display.flip()

    buttonX, buttonY = MouseClick()
    print((buttonX,buttonY))


def MouseClick():
    finish = False
    while finish == False:
    ##pygame.event contains all functions needed by user to retrieve
    #and manipulate all relevant events. button, keyboard.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 finish = True
             #extract relevant event object
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print(mouseX, mouseY)
    return (mouseX, mouseY)


#source: pradyunsg from StakeExchange
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
                break # break out of the for loop
        elif event.type == pygame.QUIT:
            done = True
            break # break out of the for loop
    if done:
        break # to break out of the while loop

    # your game stuff
    display_map()
