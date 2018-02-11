import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Color
import itertools


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
           
             
            lis=[0,1]
            q=[(x,y,z) for x in lis for y in lis for z in lis]
            print(q)
            for n in q:
              
                ball.color=[*n,abs(vel.x/50)]
            
            print ('vx,vy is', vx,vy)
            print ('offset is', offset)
            print ('vel is' ,vel)
            print ('ball velocity is' ,ball.velocity)
            print ('col',ball.color)


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    color_r = NumericProperty(0)
    color_g = NumericProperty(0)
    color_b = NumericProperty(0)
    color_a = NumericProperty(0)
    color = ReferenceListProperty(color_r,color_g,color_b,color_a)
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        #print ("pos is", self.pos)


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel
        

    def update(self, dt):
        self.ball.move()

        # bounce ball off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1
            print (self.ball.y,self.y,self.ball.top,self.top,self.ball.velocity_y)

        # went off a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            print(self.ball.x,self.x,'1st')
            self.serve_ball(vel=(4, 0))
            
        if self.ball.x > self.width:
            self.player1.score += 1
            print(self.ball.x,self.width,'2nd')
            self.serve_ball(vel=(4, 0))
            print(self.ball.x,self.width,'2nd')

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
