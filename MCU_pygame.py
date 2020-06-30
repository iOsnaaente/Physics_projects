import pygame
import time
import math 

width  = 800
height = 800

# TO USE MULTIPLES CIRCLES
population = 1
positions = []


#FUNCTIONS
def dist (pos = [0,0], origin=[0,0]) : 
	dx = pos[0] - origin[0]
	dy = pos[1] - origin[1]
	return math.sqrt(dx**2 + dy**2)

def mod(vector):
	return math.sqrt(vector[0]**2 + vector[1]**2)

def degToRad(degree):
	return degree*math.pi/180

def initCircles():
	for i in range(population):
		positions.append([-100,0])


#POS SET DEFINITIONS TO TEST THE CODE
Pos = [300,200]
Hz = 10 #HZ


#PRE SET DEFINITIONS
So  = [width/2,height/2]

angular = 2*math.pi*Hz

teta = 0

velAng = [	(-1)*angular*dist(Pos,So)*math.sin(teta),
		  	(+1)*angular*dist(Pos,So)*math.cos(teta)
		 ]

aclAng = [	(+1)*(angular**2)*dist(Pos,So)*math.cos(teta),
			(-1)*(angular**2)*dist(Pos,So)*math.sin(teta)
		 ] 

To = time.time()
T1 = To


if __name__ == "__main__":
	
	pygame.init()
	mainScreen = pygame.display.set_mode([width, height])
	clock = pygame.time.Clock()

	initCircles()

	radius = dist(Pos, So)
	
	To = time.time()

	while True:

		mainScreen.fill([200,200,200])
		#pygame.draw.circle(mainScreen, [220,200,20], [int(So[0]),int(So[1])], 20, 0)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		
		T1 = time.time()
		
		teta = teta + angular*(T1 - To)

		Pos[0] = radius* math.cos(degToRad(teta)) + So[0]
		Pos[1] = radius* math.sin(degToRad(teta)) + So[1]

		
		"""
		for i in range(len(positions)-1):
			pygame.draw.circle(mainScreen, [100,10,150], [int(positions[i][0]),int(positions[i][1])], 20, 0)
			print(positions[i])
		pygame.draw.circle(mainScreen, [0,10,50], [int(positions[len(positions)-1][0]),int(positions[len(positions)-1][1])], 20, 0)	
		
		del(positions[0])
		aux = [Pos[0], Pos[1]]
		positions.append(aux)
		"""
		
		velAng[0] = (-1)* radius* math.sin(degToRad(teta)) + Pos[0]
		velAng[1] = (+1)* radius* math.cos(degToRad(teta)) + Pos[1]
		#DRAW THE LINEAR SPEED OF THE CIRCLE - RUNNING AWAY TO THE TANGENT
		pygame.draw.circle(mainScreen, [255,79,113], [int(velAng[0]),int(velAng[1])], 5, 0)
		pygame.draw.line(mainScreen, [255,75,113], [int(velAng[0]),int(velAng[1])], [int(Pos[0]),int(Pos[1])], 2)
		
		aclAng[0] = (-1)*radius*math.cos(degToRad(teta)) + Pos[0]
		aclAng[1] = (-1)*radius*math.sin(degToRad(teta)) + Pos[1]
		#DRAW THE ANGULAR ACELERATION OF THE CIRCLE - TURNED TO INTO THE ORIGIN 		
		pygame.draw.line(mainScreen, [255,175,13], [int(aclAng[0]),int(aclAng[1])], [int(Pos[0]),int(Pos[1])], 2)
		pygame.draw.circle(mainScreen, [218,165,32], [int(aclAng[0]),int(aclAng[1])], 10, 0)
		
		#DRAW THE MAIN CIRCLE 		
		pygame.draw.circle(mainScreen, [139,10,139], [int(Pos[0]),int(Pos[1])], 40, 0)
		
		To = T1
		if teta > 360: teta = 0 
		
		pygame.display.update()
		time.sleep(0.01)