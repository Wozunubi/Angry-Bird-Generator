# Name: George Fan
# Date: May 14, 2021
# Class: ICS3U1-01
# Description: Draws an angry bird and surrounding background, while also randomizing the position of the elements

# Importing libraries for drawing in pygame, and randomizing elements
import random, pygame


# <---------------Constants--------------->

# Declaring constants for the size of the screen, animation length and various colours
SIZE = (800, 600)
ANIMATION_LENGTH = 22

# Shades
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)

# Angry bird colours
RED = (243, 39, 39)
DARK_RED = (200, 30, 30)
BEIGE = (242, 225, 191)

# Sun colours
YELLOW = (245, 237, 48)
ORANGE_YELLOW = (250, 210, 53)
ORANGE = (255, 173, 66)

# Cloud colours
LIGHT_GREY = (240, 240, 240)
GREY = (230, 230, 230)
DARK_GREY = (105, 105, 105)

# Tree colours
BROWN = (101, 67, 33)
LIGHT_BROWN = (139, 69, 19)
TREE_GREEN = (99, 170, 66)
DARK_TREE_GREEN = (90, 162, 55)

# Plant colours
GREEN = (23, 158, 73)
LIGHT_GREEN = (118, 193, 66)
VERY_LIGHT_GREEN = (119, 199, 72)

# Flower colours
BLUE = (69, 96, 233)
VIOLET = (185, 62, 238)



# <---------------Functions--------------->

# Drawing the hills in the background
def drawHill(xPos, hillLength, hillHeight, colour):   
    pygame.draw.ellipse(screen, colour, pygame.Rect(xPos, 600-(hillHeight/3), hillLength, hillHeight))
    
# Drawing the sun
def drawSun(xPos, yPos):
    pygame.draw.circle(screen, YELLOW, (xPos, yPos), 45)
    pygame.draw.circle(screen, ORANGE_YELLOW, (xPos, yPos), 41)
    pygame.draw.circle(screen, ORANGE, (xPos, yPos), 37)
    
# Drawing the moon
def drawMoon(xPos, yPos, frameNum):
    pygame.draw.circle(screen, DARK_GREY, (xPos, yPos), 40)
    pygame.draw.circle(screen, (150-(frameNum*4), 217-(frameNum*7), 233-(frameNum*8)), (xPos+15, yPos-15), 40) # Covering part of the moon to make it look like a crescent moon
    
    # Adding reflection spots
    pygame.draw.circle(screen, GREY, (xPos-25, yPos+13), 5)
    pygame.draw.circle(screen, GREY, (xPos-10, yPos+25), 3)
    
# Drawing a big cloud
def drawBigCloud(xPos, yPos):
    pygame.draw.circle(screen, GREY, (xPos, yPos), 30)
    pygame.draw.circle(screen, GREY, (xPos+30, yPos+8), 30)
    pygame.draw.circle(screen, GREY, (xPos-30, yPos+8), 30)
    pygame.draw.circle(screen, GREY, (xPos+53, yPos+23), 30)
    pygame.draw.circle(screen, GREY, (xPos-53, yPos+23), 30)    
    pygame.draw.circle(screen, GREY, (xPos+18, yPos+26), 30)
    pygame.draw.circle(screen, GREY, (xPos-18, yPos+26), 30)
    
# Drawing a medium cloud
def drawMediumCloud(xPos, yPos):
    pygame.draw.circle(screen, LIGHT_GREY, (xPos, yPos), 30)
    pygame.draw.circle(screen, LIGHT_GREY, (xPos+30, yPos+15), 30)
    pygame.draw.circle(screen, LIGHT_GREY, (xPos-30, yPos+15), 30)  
    pygame.draw.circle(screen, LIGHT_GREY, (xPos, yPos+15), 30)

# Drawing a small cloud
def drawSmallCloud(xPos, yPos):
    pygame.draw.circle(screen, WHITE, (xPos, yPos), 30)
    pygame.draw.circle(screen, WHITE, (xPos-15, yPos+15), 30)
    pygame.draw.circle(screen, WHITE, (xPos+15, yPos+15), 30)    
    
# Drawing a seagull
def drawSeagull(xPos, yPos, frameNum):
    # Drawing the wings of the seagull
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(xPos, yPos, 50, 20))
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(xPos-40, yPos, 50, 20))
    
    # Hollowing out the previous ellipses to create concave bird wings
    pygame.draw.circle(screen, (150-(frameNum*4), 217-(frameNum*7), 233-(frameNum*8)), (xPos+25, yPos+25), 20)
    pygame.draw.circle(screen, (150-(frameNum*4), 217-(frameNum*7), 233-(frameNum*8)), (xPos-15, yPos+25), 20)    

# Drawing a tree
def drawTree(xPos, yPos):
    # Drawing the trunk and an owl nest as well as adding shading
    pygame.draw.rect(screen, LIGHT_BROWN, (xPos+25, yPos, 50, 400))
    pygame.draw.line(screen, BROWN, (xPos+30, yPos+85), (xPos+30, yPos+300), 5)
    pygame.draw.line(screen, BROWN, (xPos+40, yPos+95), (xPos+40, yPos+300), 5)
    pygame.draw.circle(screen, BROWN, (xPos+60, yPos+110), 10)
    
    # Drawing the outermost layer of leaves
    pygame.draw.circle(screen, DARK_TREE_GREEN, (xPos, yPos), 30)     
    pygame.draw.circle(screen, DARK_TREE_GREEN, (xPos+100, yPos), 30)
    pygame.draw.circle(screen, DARK_TREE_GREEN, (xPos+75, yPos-43), 30)
    pygame.draw.circle(screen, DARK_TREE_GREEN, (xPos+25, yPos-43), 30)
    pygame.draw.circle(screen, DARK_TREE_GREEN, (xPos+75, yPos+43), 30)
    pygame.draw.circle(screen, DARK_TREE_GREEN, (xPos+25, yPos+43), 30)     
    
    # Drawing the second outermost layer of leaves
    pygame.draw.circle(screen, TREE_GREEN, (xPos+50, yPos-50), 30)
    pygame.draw.circle(screen, TREE_GREEN, (xPos+50, yPos+50), 30)
    pygame.draw.circle(screen, TREE_GREEN, (xPos+7, yPos-25), 30)
    pygame.draw.circle(screen, TREE_GREEN, (xPos+93, yPos-25), 30)
    pygame.draw.circle(screen, TREE_GREEN, (xPos+7, yPos+25), 30)
    pygame.draw.circle(screen, TREE_GREEN, (xPos+93, yPos+25), 30)   
    
    # Drawing the inner layer of leaves
    pygame.draw.circle(screen, VERY_LIGHT_GREEN, (xPos+50, yPos), 30)
    pygame.draw.circle(screen, VERY_LIGHT_GREEN, (xPos+70, yPos+20), 20)
    pygame.draw.circle(screen, VERY_LIGHT_GREEN, (xPos+30, yPos-20), 20)
    pygame.draw.circle(screen, VERY_LIGHT_GREEN, (xPos+70, yPos-20), 20)
    pygame.draw.circle(screen, VERY_LIGHT_GREEN, (xPos+30, yPos+20), 20)
    
    # Drawing apples
    pygame.draw.circle(screen, RED, (xPos+10, yPos), 10)
    pygame.draw.line(screen, BROWN, (xPos+10, yPos-10), (xPos+10, yPos-17), 3)
    pygame.draw.circle(screen, RED, (xPos+50, yPos-30), 10)
    pygame.draw.line(screen, BROWN, (xPos+50, yPos-40), (xPos+50, yPos-47), 3)
    pygame.draw.circle(screen, RED, (xPos+70, yPos+40), 10)
    pygame.draw.line(screen, BROWN, (xPos+70, yPos+30), (xPos+70, yPos+23), 3)
    pygame.draw.circle(screen, RED, (xPos+30, yPos+30), 10)
    pygame.draw.line(screen, BROWN, (xPos+30, yPos+20), (xPos+30, yPos+13), 3)    
    pygame.draw.circle(screen, RED, (xPos+90, yPos-10), 10)
    pygame.draw.line(screen, BROWN, (xPos+90, yPos-20), (xPos+90, yPos-27), 3)        
    
# Drawing a slingshot
def drawSlingshot(xPos, yPos):
    # Drawing the frame of the slingshot
    pygame.draw.rect(screen, LIGHT_BROWN, pygame.Rect(xPos, yPos, 25, 400))
    pygame.draw.ellipse(screen, LIGHT_BROWN, pygame.Rect(xPos-35, yPos-100, 100, 150))
    pygame.draw.ellipse(screen, (150-(frameNum*4), 217-(frameNum*7), 233-(frameNum*8)), pygame.Rect(xPos-20, yPos-85, 70, 120))
    
    # Drawing the rubber band of the slingshot
    pygame.draw.polygon(screen, BROWN, ((xPos-35, yPos-35), (xPos-20, yPos-35), (xPos-20, yPos-30), (xPos+50, yPos-30), (xPos+50, yPos-35), (xPos+65, yPos-35), (xPos+65, yPos-5), (xPos+50, yPos-5), (xPos+50, yPos-10), (xPos-20, yPos-10), (xPos-20, yPos-5), (xPos-35, yPos-5)))
    pygame.draw.ellipse(screen, BROWN, pygame.Rect(xPos-5, yPos-35, 40, 30))
    
    # Adding shading to the slingshot
    pygame.draw.line(screen, BROWN, (xPos+5, yPos+50), (xPos+5, yPos+300), 5)
    pygame.draw.line(screen, BROWN, (xPos+15, yPos+65), (xPos+15, yPos+300), 5)
    
    # Hollowing out the centre of the slingshot craddle to match the sky colour
    pygame.draw.rect(screen, (150-(frameNum*4), 217-(frameNum*7), 233-(frameNum*8)), pygame.Rect(xPos-35, yPos-100, 100, 65))

# Drawing a flower
def drawFlower(xPos, yPos, colour):
    # Drawing the stem and the centre of the flower
    pygame.draw.line(screen, LIGHT_GREEN, (xPos-1, yPos), (xPos-1, yPos+20), 2)
    pygame.draw.circle(screen, YELLOW, (xPos, yPos), 4)
    
    # Drawing the petals of the flower
    pygame.draw.ellipse(screen, colour, pygame.Rect(xPos+4, yPos-3, 10, 6))
    pygame.draw.ellipse(screen, colour, pygame.Rect(xPos-14, yPos-3, 10, 6))
    pygame.draw.ellipse(screen, colour, pygame.Rect(xPos-3, yPos-14, 6, 10))
    pygame.draw.ellipse(screen, colour, pygame.Rect(xPos-3, yPos+4, 6, 10))    
    
# Drawing a piece of grass
def drawGrass(xPos, yPos):
    pygame.draw.line(screen, LIGHT_GREEN, (xPos, yPos), (xPos, yPos+10), 2)
    
# Drawing 8 pieces of grass, and 4 different coloured flowers
def drawFlowerSet(yPos): 
    # Drawing grass
    drawGrass(random.randint(0, 800), random.randint(yPos, yPos+200))
    drawGrass(random.randint(0, 800), random.randint(yPos, yPos+200))
    drawGrass(random.randint(0, 800), random.randint(yPos, yPos+200))
    drawGrass(random.randint(0, 800), random.randint(yPos, yPos+200))
    drawGrass(random.randint(0, 800), random.randint(yPos, yPos+200))
    drawGrass(random.randint(0, 800), random.randint(yPos, yPos+200))
    drawGrass(random.randint(0, 800), random.randint(yPos, yPos+200))
    drawGrass(random.randint(0, 800), random.randint(yPos, yPos+200)) 
    
    # Drawing flowers
    drawFlower(random.randint(0, 800), random.randint(yPos, yPos+200), RED)
    drawFlower(random.randint(0, 800), random.randint(yPos, yPos+200), BLUE)
    drawFlower(random.randint(0, 800), random.randint(yPos, yPos+200), VIOLET)
    drawFlower(random.randint(0, 800), random.randint(yPos, yPos+200), WHITE)    
    
# Drawing an angry bird
def drawBird(xPos, yPos):
    # Drawing main body and head tuffs
    pygame.draw.ellipse(screen, BLACK, (xPos-60, yPos+20, 70, 25))
    pygame.draw.ellipse(screen, BLACK, (xPos-10, yPos+5, 50, 70))
    pygame.draw.ellipse(screen, BLACK, (xPos-45, yPos, 70, 25))
    pygame.draw.circle(screen, BLACK, (xPos, yPos+150), 120)
    pygame.draw.ellipse(screen, RED, (xPos-55, yPos+25, 60, 15))
    pygame.draw.ellipse(screen, RED, (xPos-5, yPos+10, 40, 60))
    pygame.draw.ellipse(screen, RED, (xPos-40, yPos+5, 60, 15))    
    pygame.draw.circle(screen, RED, (xPos, yPos+150), 115)
    
    # Drawing underbelly
    pygame.draw.ellipse(screen, BEIGE, (xPos-80, yPos+175, 160, 90))
    
    # Drawing spots
    pygame.draw.ellipse(screen, DARK_RED, (xPos-80, yPos+140, 20, 25))
    pygame.draw.ellipse(screen, DARK_RED, (xPos-50, yPos+130, 25, 35))
    pygame.draw.ellipse(screen, DARK_RED, (xPos-15, yPos+125, 40, 45))
    pygame.draw.ellipse(screen, DARK_RED, (xPos+50, yPos+125, 40, 45)) 
    
    # Drawing eyes
    pygame.draw.circle(screen, BLACK, (xPos+20, yPos+140), 22)
    pygame.draw.circle(screen, BLACK, (xPos+60, yPos+140), 22)
    pygame.draw.circle(screen, WHITE, (xPos+20, yPos+140), 17)
    pygame.draw.circle(screen, WHITE, (xPos+60, yPos+140), 17)
    pygame.draw.circle(screen, BLACK, (xPos+25, yPos+140), 5)
    pygame.draw.circle(screen, BLACK, (xPos+55, yPos+140), 5)    
    
    # Drawing eyebrows
    pygame.draw.polygon(screen, BLACK, ((xPos+40, yPos+135), (xPos-15, yPos+120), (xPos-10, yPos+105), (xPos+40, yPos+125), (xPos+85, yPos+100), (xPos+90, yPos+115)))
    
    # Drawing forehead wrinkles
    pygame.draw.ellipse(screen, DARK_RED, (xPos, yPos+95, 70, 10))
    pygame.draw.ellipse(screen, RED, (xPos, yPos+92, 70, 10))
    pygame.draw.ellipse(screen, DARK_RED, (xPos+15, yPos+83, 55, 10))
    pygame.draw.ellipse(screen, RED, (xPos-5, yPos+80, 70, 10))
    
    # Drawing beak
    pygame.draw.polygon(screen, BLACK, ((xPos-10, yPos+170), (xPos+40, yPos+210), (xPos+80, yPos+180)))
    pygame.draw.polygon(screen, BLACK, ((xPos-10, yPos+170), (xPos+45, yPos+140), (xPos+90, yPos+190)))
    pygame.draw.polygon(screen, YELLOW, ((xPos, yPos+175), (xPos+40, yPos+205), (xPos+65, yPos+185)))
    pygame.draw.polygon(screen, YELLOW, ((xPos-5, yPos+170), (xPos+45, yPos+145), (xPos+80, yPos+185)))
    
    # Drawing tail
    pygame.draw.polygon(screen, BLACK, ((xPos-120, yPos+145), (xPos-120, yPos+135), (xPos-150, yPos+125), (xPos-155, yPos+145)))
    pygame.draw.polygon(screen, BLACK, ((xPos-120, yPos+145), (xPos-120, yPos+155), (xPos-135, yPos+175), (xPos-145, yPos+160)))
    pygame.draw.polygon(screen, BLACK, ((xPos-120, yPos+135), (xPos-115, yPos+130), (xPos-130, yPos+105), (xPos-140, yPos+115)))

# Drawing everything in one frame in the correct order for the scenery to layer correctly
def drawEverything(frameNum):    
    
    # Drawing the sky, and changing incrementing the colour depending on the frame number
    screen.fill((150-(frameNum*4), 217-(frameNum*7), 233-(frameNum*8)))
    
    # Drawing the seagulls, and the frame number is used to blend in the undersides of their wings
    drawSeagull(random.randint(95, 355), random.randint(75, 100), frameNum)
    drawSeagull(random.randint(445, 695), random.randint(75, 125), frameNum)     
    drawSeagull(random.randint(330, 470), random.randint(150, 200), frameNum)
    
    # Detecting if it's day or night based on the frame number, and drawing a sun or moon respectively
    if frameNum <= 10:
        drawSun((frameNum*80), 25+(frameNum*10)) # Using frame number to determine the position of the sun in the sky
    else:
        drawMoon(((frameNum-11)*80), 25+((frameNum-11)*10), frameNum) # Using frame number to determine the position of the moon in the sky
    
    # Drawing all the clouds
    drawBigCloud(random.randint(0, 400), random.randint(25, 85))
    drawBigCloud(random.randint(400, 800), random.randint(25, 85))   
    drawMediumCloud(random.randint(0, 800), random.randint(25, 85))
    drawMediumCloud(random.randint(0, 800), random.randint(25, 85))
    drawMediumCloud(random.randint(0, 400), random.randint(25, 85))
    drawMediumCloud(random.randint(400, 800), random.randint(25, 85))
    drawSmallCloud(random.randint(0, 800), random.randint(25, 85))
    drawSmallCloud(random.randint(0, 800), random.randint(25, 85))  
    
    # Drawing the slingshot in the far background
    drawSlingshot(random.randint(125, 175), random.randint(225, 275))
    
    # Drawing hills infront of the slingshot, the parameters are the x position, the length of the hill, the height of the hill, and the colour
    drawHill(random.randint(-700, -100), random.randint(1000, 1100), random.randint(900, 1000), (25, 158, 73))
    drawHill(random.randint(-100, 500), random.randint(1000, 1100), random.randint(900, 1000), (20, 153, 68))
    
    # Drawing a tree inbetween the hills
    drawTree(random.randint(575, 625), random.randint(240, 260))
    
    # Drawing more hills to complete the background
    drawHill(random.randint(-700, -100), random.randint(1000, 1100), random.randint(700, 800), (15, 148, 63))
    drawHill(random.randint(-100, 500), random.randint(1000, 1100), random.randint(700, 800), (10, 143, 58))
    drawHill(random.randint(-700, -100), random.randint(1000, 1100), random.randint(500, 600), (5, 138, 53))
    drawHill(random.randint(-100, 500), random.randint(1000, 1100), random.randint(500, 600), (0, 133, 48))  

    # Drawing 10 sets of flowers/grass, and passing in max y value where the flowers/grass should appear
    drawFlowerSet(400)
    drawFlowerSet(400)  
    drawFlowerSet(400)
    drawFlowerSet(400)
    drawFlowerSet(400)
    drawFlowerSet(400)  
    drawFlowerSet(400)
    drawFlowerSet(400)    
    drawFlowerSet(400)
    drawFlowerSet(400)     
    
    # Drawing the angry bird
    drawBird(random.randint(350, 450), random.randint(280, 320))
    
    # Displaying the graphic to the audience, and waiting for 0.1 seconds
    pygame.display.flip()
    pygame.time.wait(100)
    
    # Increamenting the frame number by one, and returning the new frame number
    return frameNum+1



# <---------------Body of program--------------->

# Initializing pygame and setting the screen size to the SIZE constant
pygame.init()
screen = pygame.display.set_mode(SIZE)

# Setting variables to 0
frameNum = 5
i = 0

# Looping through as long as 'i < 600'. Also, 'i' is increamented by 1 everytime the loop is ran once. Since each frame takes 0.1 seconds, the whole animation will take 1 minute total
while i < 600:
    frameNum = drawEverything(frameNum) # Calling the 'drawEverything' function to draw the graphic. Then setting 'frameNum' to the returned value of the function
    
    # Checks if the frame number is divisible by the animation length, if it is, then 'frameNum' is set to zero so the animated sequence can restart again
    if frameNum % ANIMATION_LENGTH == 0: 
        frameNum = 0
    i += 1 # This is where 'i' is increamented by 1, as mentioned above

pygame.quit() # Closing the pygame window