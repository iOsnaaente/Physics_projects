from kivy.properties import ReferenceListProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.app import App 

from random import randint


class PongBall(Widget):
    vel_x = NumericProperty(0)
    vel_y = NumericProperty(0)
    vel   = ReferenceListProperty( vel_x, vel_y ) 
    def move( self ):
        self.pos = Vector( *self.vel ) + self.pos


class PongPaddle( Widget ):
    score = NumericProperty(0)
    def bounceBall( self, ball ):
        if self.collide_widget(ball):
            vx, vy = ball.vel 
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector( -1 * vx, vy )
            vel = bounced * 1.1 
            ball.vel = vel.x, vel.y + offset 


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel = [4,0] ):
        self.ball.center = self.center
        self.ball.vel = vel

    def update(self, dt ):
        self.ball.move()
        self.player1.bounceBall( self.ball )            
        self.player2.bounceBall( self.ball )        

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.vel_y *= -1
        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.vel_x *= -1
        

        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))
    
    def on_touch_move(self, touch):
        if touch.x < self.width /3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width /3:
            self.player2.center_y = touch.y 



class PongApp(App):

    def build( self ):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval( game.update, 1.0/60.0 )
        Clock.schedule_interval( lambda dt : print(game.ball.vel, dt), 1 )
        return game

if __name__ == '__main__':
    PongApp().run()
