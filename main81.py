#Adva & Rainny
#Jewelry Room
#Pygame Summative
#Python 3.3

import pygame
from pygame.transform import scale
from pygame.locals import*
import time
pygame.init()

pygame.mixer.music.load('thief song.mp3')
pygame.mixer.music.play(-1)

x = 819#Size of background #546,414 used to be 1444, 842
y = 621
screen = pygame.display.set_mode((x,y),pygame.FULLSCREEN)
background = pygame.image.load("jroom1.bmp").convert()
back_rect = background.get_rect()

pygame.mouse.set_visible(1)



pygame.display.set_caption("Jewelry Room")

black = (0,0,0)
white = (255,255,255)
blue = (123,127,222)
green = (36,238,63)
clock = pygame.time.Clock()


keyx,keyy = 142,498
def text(text,location):# Displays score and lives on screen
    font=pygame.font.Font(None,20)
    t=font.render(text, 1,green)
    screen.blit(t, (location))
def drag(mouse,obj,obj_rect):
    obj_rect.center = mouse
    screen.blit(obj, obj_rect)


inventory = pygame.image.load('rectangle.bmp').convert_alpha()
inventory_rect = inventory.get_rect()
screen.blit(inventory, inventory_rect)

class back(pygame.sprite.Sprite):
    def __init__(self,click):
        button = pygame.image.load('back.bmp').convert_alpha()
        button_rect = button.get_rect()
        button_rect.bottomright = ([819,621])
        b = screen.blit(button, button_rect)
        screen.blit(button, button_rect)
        if click == True and b.collidepoint(pos) and pygame.mouse.get_pressed():
            print("back to Rainny")
            ins = False


def rscore(score):
    for sprite in evidence:
        num = sprite.score()
        if num == True:
            score = score +1
    font=pygame.font.Font(None,30)
    t=font.render("Evidence Found:"+str(score), 1,white)
    screen.blit(t, (580,10))
    

class clue(pygame.sprite.Sprite):      
    def __init__(self,position,info):
        image = pygame.image.load(info[3]).convert_alpha()  
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.position = position
        self.image = image
        self.image1 = image
        self.rect = self.image.get_rect()
        pos = pygame.mouse.get_pos()              
        self.rect.bottomleft = self.position
        self.height = info[0]
        self.width = info[1]
        self.words = info[2]
        self.state = info[4]
    def show(self,click,held,screen):
        b = screen.blit(self.image, self.rect)        
        if held == True and b.collidepoint(pos) and self.state == 'moveable':
            self.rect.center = pos
            point = self.rect.center
            if inventory_rect.collidepoint(point):
                self.image = pygame.transform.scale(self.image,(18,18))
                self.rect.height =18
                self.rect.width = 18
            else:
                self.image = self.image1
                self.rect.height =self.height
                self.rect.width = self.width
        elif click == True:
            if b.collidepoint(pos) and self.state == 'not_moveable':
                wordplacex = self.rect.bottomleft[0]
                wordplacey = self.rect.bottomleft[1]
                wordplace = (wordplacex,wordplacey)
                text("You can't move this",wordplace)
    def score(self):
        b = screen.blit(self.image, self.rect)
        if b.colliderect(inventory_rect):
            return True
        else:
            return False
    def what(self):
        b = screen.blit(self.image, self.rect)
        if b.collidepoint(pos):
            wordplacex = self.rect.bottomleft[0]-self.width - (0.3*self.width)
            wordplacey = self.rect.bottomleft[1]-self.height -(0.3*self.height)
            wordplace = (wordplacex,wordplacey)
            text(self.words,wordplace)

            
keyinfo =  (38,38, "A key? I wonder where this fits?",'key.bmp',"moveable") 
noteinfo = (77,77, "Note reading: I told you you would regret this!",'letter.bmp',"moveable")
glassinfo = (88,77, "A spyglass- I've always wanted one of those...",'spyglass.bmp',"moveable")
footprintinfo = (77,77,"A footprint? Size 10 women, size 8 men.",'footprint.bmp',"not_moveable")
boxinfo = (58,53,"The kings most priceless jewels...GONE!",'jcase.bmp',"moveable")
shoesinfo = (90,61,"Leatherbound, handstiched, iconic Andy Loafers! Don't get to shine those everyday!", 'shoes.bmp',"moveable")
bottleinfo = (60,57,"A broken wine bottle. There must have been some kind of fight.",'bottle.bmp',"not_moveable")
evidence = pygame.sprite.Group()
clue.groups = evidence


class menu(pygame.sprite.Sprite):
    def __init__(self,file,screen,loc):
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = loc     
    def instructions(self,screen):
        b = screen.blit(self.image, self.rect)
        pos = pygame.mouse.get_pos()
        if b.collidepoint(pos):
            return True
        else:
            return False
        
menubuttons = pygame.sprite.Group()
menu.groups = menubuttons
instruct = menu('instructions-button.bmp',screen,(x/2,y/2))
play =  menu('start-button.bmp',screen,(x/2,375))

MousePressed=False
MouseDown=False
held = False
click = False
MouseReleased=False # Released THIS FRAME
info = False
position = 142,498
key1 = clue((142,498),keyinfo)
note = clue((624,443),noteinfo)
spyglass = clue((700,250),glassinfo)
footprint = clue((600,590),footprintinfo)
jcase = clue((414,317),boxinfo)
shoes = clue((150,600),shoesinfo)
bottle= clue((200,350),bottleinfo)

score = 0
playing = True
cr = False
ins = False
while playing:
    screen.fill(blue)
    font=pygame.font.Font(None,150)
    t=font.render("Mystery Jewels", 1,green)
    screen.blit(t, (20,50))
    pos = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            ins = instruct.instructions(screen)
            cr = play.instructions(screen)
        else:
            instruct.instructions(screen)
            play.instructions(screen)        
        if ins == True:
            screen.fill(blue)
            font=pygame.font.Font(None,30)
            t=font.render("Mystery Jewels", 1,green)
            screen.blit(t, (20,50))
            one=font.render("You are the average shoe shiner come to visit your friend king ------ .", 1,green)
            two=font.render("Unfortunately the king is having some problems with a theif in his very mist.", 1,green)
            three=font.render("Luckily you think you can solve the case.", 1,green)
            four=font.render("Game Play", 1,green)
            five=font.render("Use your mouse to click around the crimeroom to discover clues.", 1,green)
            six = font.render("Right click on items to learn more about them.", 1,green)
            seven=font.render("Rainny write instructions here", 1,green)
            screen.blit(one, (20,80))
            screen.blit(two, (20,110))
            screen.blit(three, (20,140))
            screen.blit(four, (20,200))
            screen.blit(five, (20,230))
            screen.blit(six, (20,260))
            screen.blit(seven, (20,290))
            back(click)
        pygame.display.flip()
        while cr == True:
            click = False
            held = False
            pos = pygame.mouse.get_pos()
            screen.blit(background, back_rect)
            screen.blit(inventory, inventory_rect)
            rscore(score)
            for sprite in evidence:
                sprite.show(click,held,screen)
            back(click)
            pygame.display.flip()    
            clock.tick(50)
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    MousePressed=True 
                    MouseDown=True
                if ev.type == pygame.MOUSEBUTTONUP:
                    MouseReleased=True
                    MouseDown=False
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 3:
                    info = True
            if MousePressed==True:   
                click = True
                screen.blit(inventory, inventory_rect)
                for sprite in evidence:
                    sprite.show(click,held,screen)
                back(click)
            if MouseDown == True:
                held = True
                for sprite in evidence:
                    sprite.show(click,held,screen)
            if info == True:
                for sprite in evidence:
                    sprite.what()
                pygame.display.flip()
                time.sleep(0.8)
            MousePressed=False
            MouseReleased=False
            info = False
            
            pygame.display.flip()
                #time.sleep(0.8)

pygame.quit()
