import pygame

pygame.display.init()
pygame.display.set_caption("Assignment 1")
drawing_window = pygame.display.set_mode((500,500))
drawing_window.fill((249,150,107))#Light Salmon (RGB value - 249,150,107)
pygame.draw.rect(drawing_window,(76,196,23),((0,240,500,260)))#Green Apple (RGB value - 76,196,23)  The grass is drawn
pygame.draw.ellipse(drawing_window,(130,202,255),(76,308,186,140))#Day Sky Blue (RGB value - 130,202,255)   The pond is drawn
pygame.draw.polygon(drawing_window,(194,70,65),((192,183),(242,144),(390,144),(340,183)))#Cherry Red (RGB value - 194,70,65)    The tilted roof is drawn
pygame.draw.polygon(drawing_window,(194,70,65),((373,149),(390,144),(424,183),(403,183)))#Cherry Red (RGB value - 194,70,65) The tilted roof is drawn
pygame.draw.rect(drawing_window,(234,193,23),((200,184,139,88)))#Golden Brown (RGB value -234,193,23) One of the walls of the house is drawn
pygame.draw.rect(drawing_window,(253,208,23),((339,184,66,88)))#Bright Gold (RGB value - 253,208,23) The other wall of the house is drawn
pygame.draw.rect(drawing_window,(98,93,93),((200,184,139,3)))#Carbon Gray (RGB value - 98,93,93) The shadow of the roof on the wall is drawn
pygame.draw.polygon(drawing_window,(253,208,23),((339,184),(405,183),(373,149)))#Bright Gold (RGB value - 253,208,23) The other wall of the house is completed
pygame.draw.circle(drawing_window,(248,114,23),(465,170),32)#Pumpkin Orange (RGB value - 248,114,23) The sun is drawn
pygame.draw.circle(drawing_window,(255,243,128),(304,213),21)#Corn Yellow (RGB value - 255,243,128) The border of the circular window on the wall is drawn
pygame.draw.circle(drawing_window,(194,223,255),(304,213),18)#Sea Blue (RGB value - 194,223,255) The glass of the window on the wall is drawn
pygame.draw.rect(drawing_window,(234,193,23),((283,213,42,59)))#Golden Brown (RGB value - 234,193,23) One of the walls is completed
pygame.draw.rect(drawing_window,(255,243,128),((283,213,42,2)))#Corn Yellow (RGB value - 255,243,128) The border of the circular window is drawn
pygame.draw.rect(drawing_window,(255,243,128),((225,194,42,42)))#Corn Yellow (RGB value - 255,243,128) The border of the square window is drawn
pygame.draw.rect(drawing_window,(194,223,255),((227,196,38,38)))#Sea Blue (RGB value - 194,223,255) The square window is drawn
pygame.draw.rect(drawing_window,(255,243,128),((225,215,42,2)))#Corn Yellow (RGB value - 255,243,128) The border of the window on the wall is drawn
pygame.draw.rect(drawing_window,(255,243,128),((246,194,2,42)))#Corn Yellow (RGB value - 255,243,128) The grill of the window on the wall is drawn
pygame.draw.rect(drawing_window,(184,115,51),((360,197,28,75)))#Copper (RGB value - 184,115,51) The door is drawn
pygame.draw.rect(drawing_window,(255,243,128),((365,203,18,18)))#Corn Yellow (RGB value - 255,243,128) The border of the window on the door is drawn 
pygame.draw.rect(drawing_window,(194,223,255),((367,205,14,14)))#Sea Blue (RGB value - 194,223,255) The window on the door is drawn
pygame.draw.circle(drawing_window,(255,243,128),(384,240),2)#Corn Yellow (RGB value - 255,243,128) The grill of the window on the door is drawn
pygame.draw.rect(drawing_window,(194,70,65),((354,115,21,36)))#Cherry Red (RGB value - 194,70,65) The chimney is drawn
pygame.draw.rect(drawing_window,(194,70,65),((350,114,29,8)))#Cherry Red (RGB value - 194,70,65) The top of the chimney is drawn
pygame.draw.polygon(drawing_window,(73,61,38),((260,144),(262,130),(283,130),(288,144)))#Mocha (RGB value - 73,61,38) The bark of the tree is being drawn
pygame.draw.polygon(drawing_window,(73,61,38),((262,130),(273,108),(266,101),(280,87),(286,114),(283,130)))#Mocha (RGB value - 73,61,38) The bark of the tree is being drawn
pygame.draw.polygon(drawing_window,(73,61,38),((266,101),(248,91),(241,128),(231,122),(217,125),(229,116),(236,118),(243,80),(260,84),(280,87)))#Mocha (RGB value - 73,61,38) The bark of the tree is being drawn 
pygame.draw.polygon(drawing_window,(73,61,38),((260,92),(270,80),(288,73),(301,84),(306,99),(290,83),(280,87)))#Mocha (RGB value - 73,61,38) The bark of the tree is being drawn
pygame.draw.polygon(drawing_window,(73,61,38),((257,92),(265,63),(269,55),(280,52),(295,46),(307,63),(293,54),(273,63),(274,92)))#Mocha (RGB value - 73,61,38) The tree is completed

pygame.display.update()
pygame.image.save(drawing_window,"house_101171605.bmp")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()