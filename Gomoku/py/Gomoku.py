import pygame


BLACK=(0,0,0)
WHITE=(255, 255, 255)
GRAY=(240,240,240)

LEN=40
LINES=15
RADIUS=15
LEFTWIDTH=100
RIGHTWIDTH=100
UPPERWIDTH=80
DOWNWIDTH=150
WIDTH=LEFTWIDTH+RIGHTWIDTH+LEN*(LINES-1)
HEIGHT=UPPERWIDTH+DOWNWIDTH+LEN*(LINES-1)
CONSNUM=5
WHITEPLAYER=1
BLACKPLAYER=2

pygame.init()
pygame.display.set_caption('五子棋')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() 
pygame.display.update()
myfont  = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',50)
WHITEWINTEXT = myfont.render("White player wins!",True,BLACK,GRAY)
BLACKWINTEXT = myfont.render("Black player wins!",True,BLACK,GRAY)
board=[]
for i in range(LINES):
	board.append([0]*LINES)
Win=False
running=True
CurPlayer=WHITEPLAYER
NxtPlayer=BLACKPLAYER
WinPlayer=0
def draw(board):
	screen.fill(GRAY) 
	for i in range(0,LINES):
		pygame.draw.line(screen,BLACK,(LEFTWIDTH+i*LEN,UPPERWIDTH),(LEFTWIDTH+i*LEN,HEIGHT-DOWNWIDTH),3)
		pygame.draw.line(screen,BLACK,(LEFTWIDTH,UPPERWIDTH+i*LEN),(WIDTH-RIGHTWIDTH,UPPERWIDTH+i*LEN),3)
	for i in range(0,LINES):
		for j in range(0,LINES):
			if (board[i][j]==WHITEPLAYER):
				pygame.draw.circle(screen,WHITE,(LEFTWIDTH+i*LEN,UPPERWIDTH+j*LEN),RADIUS,RADIUS)
			if (board[i][j]==BLACKPLAYER):
				pygame.draw.circle(screen,BLACK,(LEFTWIDTH+i*LEN,UPPERWIDTH+j*LEN),RADIUS,RADIUS)
	if (WinPlayer):
		if (WinPlayer==WHITEPLAYER):
			screen.blit(WHITEWINTEXT,(WIDTH//2-100,HEIGHT-DOWNWIDTH//2))
		else:
			screen.blit(BLACKWINTEXT,(WIDTH//2-100,HEIGHT-DOWNWIDTH//2))

	pygame.display.update()

while (running):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			MouseX,MouseY=pygame.mouse.get_pos()
			if ((MouseX-LEFTWIDTH)%LEN<=RADIUS or (MouseX-LEFTWIDTH)%LEN>=LEN-RADIUS):
				if ((MouseY-UPPERWIDTH)%LEN<=RADIUS or (MouseY-UPPERWIDTH)%LEN>=LEN-RADIUS):
					PosX,PosY=(MouseX-LEFTWIDTH+RADIUS)//LEN,(MouseY-UPPERWIDTH+RADIUS)//LEN
					if (PosX>=0 and PosX<LINES and PosY>=0 and PosY<LINES and board[PosX][PosY]==0):
						board[PosX][PosY]=CurPlayer
						CurPlayer,NxtPlayer=NxtPlayer,CurPlayer
	Win=False
	for i in range(0,LINES):
		for j in range(0,LINES):
			if (i>=CONSNUM-1):
				Win=True
				for k in range(0,CONSNUM):
					if (board[i-k][j]!=NxtPlayer):
						Win=False
						break
				if Win:
					break
			if (j>=CONSNUM-1):
				Win=True
				for k in range(0,CONSNUM):
					if (board[i][j-k]!=NxtPlayer):
						Win=False
						break
				if Win:
					break

			if (i>=CONSNUM-1 and j>=CONSNUM-1):
				Win=True
				for k in range(0,CONSNUM):
					if (board[i-k][j-k]!=NxtPlayer):
						Win=False
						break
				if Win:
					break


			if Win:
				break
		if Win and WinPlayer==0:
			print(1)
			WinPlayer=NxtPlayer

	draw(board)