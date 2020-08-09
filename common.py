import pygame

pygame.font.init()

class Common():
    def __init__(self,id):
        self.id = id
        self.p1Went = False
        self.p2Went = False
        self.p1picked = None
        self.p2picked = None 
        self.message = "Checking for oppontents"
    def displayText(self,win,pos,text):
        font =  pygame.font.SysFont('Comic Sans',30)
        textsurface = font.render(text,True, (0, 0, 0))
        win.blit(textsurface,(pos[0] + textsurface.get_rect().width / 3 ,pos[1] + textsurface.get_rect().height ))
    def display_item(self,win):
        self.displayText(win,(150,30),self.message)
        self.displayText(win,(100,80),"YOU")
        self.displayText(win,(300,80),"OPPONENT")
        self.displayText(win,(80,130),self.p1picked)
        self.displayText(win,(300,130),self.p2picked)