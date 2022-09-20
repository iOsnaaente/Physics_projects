import random 

class Particle:
    def __init__( self, x : int, y : int, img : list, w : int, h : int, vector : list = [4 + random.randint( 7, 10 ) / 10,4 + random.randint( 7, 10 ) / 10] ) -> None:
        self.x          = x 
        self.y          = y 
        self.scale      = 0.01
        self.img        = img 
        self.w          = w
        self.h          = h
        self.alpha      = 255 
        self.alpha_rate = 1
        self.alive      = True 
        self.vx         = vector[0] 
        self.vy         = vector[1] 
        self.k =  0.01*random.random() * random.choice([-1, 1])
        self.id         = -1

    def update( self ):
        self.x  += self.vx 
        self.vx += self.k 
        self.y  += self.vy
        self.vy += self.k
        self.scale += 0.0001 
        self.alpha -= self.alpha_rate
        if self.alpha < 0:
            self.alpha = 0 
            self.alive = False 
        self.alpha_rate -= 0.1 
        if self.alpha_rate < 1.5:
            self.alpha_rate = 1.5 
        
        self.w += self.w*self.scale
        self.h += self.h*self.scale

    def get_alpha( self ): 
        return self.alpha

    def kill_particle( self ):
        if not self.alive: 
            return True
        else: 
            return False 

    def set_id( self, id ):
        self.id = id 


class Smoke:
    def __init__( self, x : int, y : int, img : str, w : int, h : int ):
        self.x = x 
        self.y = y 
        self.img = img 
        self.w = w 
        self.h = h 
        self.particles = [ ] 
        self.frames  = 0 
        self.new_att = 1
        self.vector  = [4 + random.randint( 7, 10 ) / 10, 4 + random.randint( 7, 10 ) / 10]

    def update( self ): 
        self.particles = [ i for i in self.particles if i.alive ]
        self.frames += 1 
        if self.frames % self.new_att == 0: 
            self.frames = 0 
            self.particles.append( Particle( self.x, self.y, self.img, self.w, self.h, self.vector ) )
            self.new_att = random.randint( 2, 5)
        for i in self.particles:
            i.update()

    def get_particles( self ):
        return self.particles

    def set_particles( self, particles ):
        self.particles = particles 