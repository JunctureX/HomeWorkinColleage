import random
import sys
import pygame

WHITE=(255,255,255)
BLACK=(0,0,0)
LIGHT_GRAY=(240,240,240)

curSpeed=6

BLOCKCOLOR=BLACK
BGCOLOR=LIGHT_GRAY

class Block : 
    width = 24
    height = 24

    @staticmethod
    def draw(s,left,top,color,bg_color) :
        pygame.draw.rect(s,bg_color,pygame.Rect(left,top,Block.width,Block.height))
        pygame.draw.rect(s,color,pygame.Rect(left,top,Block.width-1,Block.height-1))


class Building :
    def __init__(self):
        self.form=random.choice(
            [
                [
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,1,1,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]
                ],
                [
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]
                ],
                [
                    [0,0,0,0,0],
                    [0,1,1,0,0],
                    [0,0,1,1,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]
                ],
                [
                    [0,0,0,0,0],
                    [0,0,1,1,0],
                    [0,1,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]
                ],
                [
                    [0,0,0,0,0],
                    [0,1,1,0,0],
                    [0,0,1,0,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0]
                ],
                [
                    [0,0,0,0,0],
                    [0,1,1,0,0],
                    [0,1,1,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]
                ]
            ]
        )

    def __getitem__(self,pos) : 
        return self.form[pos]
    
    def __setitem__(self,key,value):
        self.form[key]=value

class Layout : 

    def __init__(self) :
    #    print("init Layout")
        self.blockX=16
        self.blockY=22
        self.layout=[[0 if 1<i<self.blockX-2 and j<self.blockY-2 else 1
            for i in range(self.blockX)] for j in range(self.blockY)]
    
    @property
    def size(self) :
        return (self.blockX*Block.width,self.blockY*Block.height)
    
    def createNewBulding(self) :
        self.building=Building()
        self.buildL,self.buildT=5,0
        self.drop_speed=curSpeed
    #    print(self.testBuildingTouchWall())
        return self.testBuildingTouchWall()
    
    @property
    def speed(self) :
        return self.drop_speed
    
    def testBuildingTouchWall(self,X=0,Y=0) :
        for i in range(4,-1,-1) :
            for j in range(5) : 
                if self.building[i][j] :
                    if self.layout[i+self.buildT+Y][j+self.buildL+X]:
                        return True
        return False

    def moveLeftRight(self,x) :
        if not self.testBuildingTouchWall(X=x) : 
            self.buildL+=x
    
    def downBuild(self):
        self.buildT+=1
    
    def directDown(self):
        self.drop_speed=50
    
    def convertBuilding(self) :
        newBox=[[0 for i in range(5)] for j in range(5)]
        for i in range(5) : 
            for j in range(4,-1,-1):
                newBox[i][j]=self.building[4-j][i]
        self.building=newBox

    def clearFullLine(self):
        newLayout = [[0 if 1<i<self.blockX-2 and j<self.blockY-2 else 1
            for i in range(self.blockX)]for j in range(self.blockY)]
        rowLen=self.blockX-4
        newRow=self.blockY-3
        for curRow in range(self.blockY-3,0,-1):
            if sum(self.layout[curRow][2:self.blockX-2])<rowLen : 
                newLayout[newRow]=self.layout[curRow]
                newRow-=1
        self.layout=newLayout

    def putBuildingToLayout(self) :
        for i in range(4,-1,-1):
            for j in range(5):
                if self.building[i][j]:
                    self.layout[i+self.buildT][j+self.buildL]=1
        self.clearFullLine()
    
    def drawBuilding(self,s):
        curL,curT=self.buildL*Block.width,self.buildT*Block.height
        for i in range(5):
            for j in range(5) :
                if self.building[j][i] :
                    Block.draw(s,curL+i*Block.width,curT+j*Block.height,BLOCKCOLOR,BGCOLOR)
    
    def draw(self,s) :
        for i in range(self.blockX) :
            for j in range(self.blockY) :
                if self.layout[j][i]==0 : 
                    Block.draw(s,i*Block.width,j*Block.height,BGCOLOR,BLOCKCOLOR)
                else :
                    Block.draw(s,i*Block.width,j*Block.height,BLOCKCOLOR,BGCOLOR)

def main() : 
    global curSpeed
    #print("do main")
    while True :
    #    print("do loop")
        layout=Layout()
    #    print("init?")
        layout.createNewBulding()
        pygame.init()
        pygame.display.set_caption('俄罗斯方块-仲星焱')
        screen=pygame.display.set_mode((layout.size),0,32)
        is_over=False
        down_flag=False
        while not is_over:
            for e in pygame.event.get():
                if e.type==pygame.QUIT :
                    sys.exit()
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_UP:
                        layout.convertBuilding()
                    if e.key==pygame.K_DOWN:
                        down_flag=True
                    if e.key==pygame.K_LEFT:
                        layout.moveLeftRight(-1)
                    if e.key==pygame.K_RIGHT:
                        layout.moveLeftRight(1)
                    if e.key==pygame.K_MINUS:
                        curSpeed = max(curSpeed - 1, 1)
                    if e.key==pygame.K_EQUALS or e.key==pygame.K_PLUS:
                        curSpeed = min(curSpeed + 1, 10)
            if layout.testBuildingTouchWall(Y=1):
                layout.putBuildingToLayout()
                is_over=layout.createNewBulding()
                down_flag=False
            else :
                layout.downBuild()
            layout.draw(screen)
            layout.drawBuilding(screen)
            pygame.display.update()
            if down_flag : 
                layout.directDown()
            pygame.time.Clock().tick(layout.speed)
            layout.drop_speed=curSpeed
        down_flag=False

if __name__=='__main__':
 #   print("in main")
    main()