import pygame
from network import Network
import time


pygame.font.init()
WIDTH = 600
HEIGHT = 700
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("RockPaperSciessors")


class Button:
    def __init__(self,x,y,text,color):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.height = 150
        self.width = 100
        self.rect = (x,y,self.width,self.height)

    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)
        font =  pygame.font.SysFont('comicsans',30)
        textsurface = font.render(self.text,1, (0, 0, 0))
        win.blit(textsurface,(self.x + round(self.width /2)-round(textsurface.get_width()/2) ,self.y + round(self.height/2)- round(textsurface.get_height()/2)))
    def click(self,pos):
        p1 = pos[0]
        p2 = pos[1]
        if (p1 > self.x and p1 < self.x + self.width) and (p2 > self.y and p2 < self.y + self.height):
            print('clicked')
            return True
        else:
            return False

def redrawgameWindow(win,game,picked):
    win.fill((255,255,255))
    font = pygame.font.SysFont("comicsans",30)
    if not game.connected():
        textsurface = font.render('Waiting for Players',1,(0,0,0),True)
    else:
        textsurface = font.render("Connected",1,(0,0,0),True)
        showtext =  font.render(picked,1,(0,0,0),True)
        if (game.p1Went and player == 1) or (game.p2Went and player == 0) :
            showtext1 = font.render("Locked",1,(0,0,0),True) 
        else:
            showtext1 = font.render("Not Moved",1,(0,0,0),True)

        win.blit(showtext,(100,400))
        win.blit(showtext1,(400,400))  
        
    win.blit(textsurface,(WIDTH//2 - textsurface.get_width()//2,HEIGHT//2 - textsurface.get_height()//2))
    showScoreBoard(win)

    for button in buttons:
        button.draw(win)


  
    pygame.display.update()

def showScoreBoard(win):
    font = pygame.font.SysFont("comisans",40)
    textsurface1 = font.render(f"Your Score : {yourScore}",1,(0,255,0),True)
    textsurface2 = font.render(f"opponent Score : {opponentScore}",1,(0,255,0),True)
    win.blit(textsurface2,(WIDTH - textsurface2.get_width()-10,50+textsurface2.get_height()))
    win.blit(textsurface1, (10,50+textsurface1.get_height()))


buttons = [Button(50,500,'Rock',(255,0,0)),Button(250,500,'Sciessors',(0,0,255)),Button(450,500,'Paper',(0,255,0))]


n = Network()
run = True
player = n.get_P()
picked = 'Your Move'
yourScore,opponentScore = 0,0
print("You are player",player)
while run:
    clock.tick(60)
    try:
        game = n.send('get')
    except Exception as e:
        print(str(e))
        run = False
    if game.quit:
        print("Exisiting From game")
        run = False
    if game.p1Went and game.p2Went:
        pygame.time.delay(500)
        font =  pygame.font.SysFont('comicsans',50)
        if (game.winner() == 0 and player == 0) or (game.winner() == 1 and player ==1):
            yourScore += 1
            textsurface = font.render("You Won",1, (255, 0, 0))
        elif game.winner() == -1:
            textsurface = font.render("Tie",1,(255,0,0))
        else:
            opponentScore += 1
            textsurface = font.render("You Lost",1,(255,0,0))
        win.blit(textsurface,(WIDTH//2 - textsurface.get_width()//2,100))
        pygame.display.update()
        pygame.time.delay(2000)
        try:
            n.send('reset')
            picked = 'Your Move'
        except:
            run = False
            print("Could'nt get game")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
           
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for btn in buttons:
                if btn.click(pos) and game.connected():
                    if player == 0:
                        if not game.p1Went:
                            picked = f"You Selected {btn.text}"
                            game = n.send(btn.text)
                    else:
                        if not game.p2Went:
                            picked = f"You Selected {btn.text}"
                            game = n.send(btn.text)

  
    
    redrawgameWindow(win,game,picked)
   
pygame.quit()
    

