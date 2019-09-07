import pygame
import time
import math 


population = 75
positions = []

So  = [0,0]
Pos = [0,0]

velAng = 2
teta = 0


def initCircles():
	for i in range(population):
		positions.append([-100,0])

def dist (pos = [0,0], origin=[0,0]) : 
	dx = pos[0] - origin[0]
	dy = pos[1] - origin[1]
	return math.sqrt(dx**2 + dy**2)

def degToRad(grau):
	return grau*math.pi/180



if __name__ == "__main__":
	
	pygame.init()
	mainScreen = pygame.display.set_mode([800,800])
	clock = pygame.time.Clock()

	So = [400,400]
	Pos = [600,400]

	initCircles()

	raio = dist(Pos, So)
	
	while True:

		mainScreen.fill([255,255,255])
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		teta = teta + velAng

		Pos[0] = raio* math.cos(degToRad(teta)) + So[0]
		Pos[1] = raio* math.sin(degToRad(teta)) + So[1]
		
		for i in range(len(positions)-1):
			pygame.draw.circle(mainScreen, [100,10,150], [int(positions[i][0]),int(positions[i][1])], 20, 0)
			print(positions[i])
		pygame.draw.circle(mainScreen, [0,10,50], [int(positions[len(positions)-1][0]),int(positions[len(positions)-1][1])], 20, 0)	
		
		del(positions[0])
		aux = [Pos[0], Pos[1]]
		positions.append(aux)
			
		pygame.display.update()
		time.sleep(0.01)