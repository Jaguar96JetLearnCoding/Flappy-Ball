import pgzrun
import random
WIDTH=600
HEIGHT=600
a=1000
#Class for the ball
class Ball():
    def __init__(self,radius,x,y,colour):
        self.radius=radius
        self.x=x
        self.y=y
        self.vx=60
        self.vy=0
        self.colour=colour
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.colour)
red_ball=Ball(20,300,50,"Red")
        
def draw():
    screen.fill("black")
    red_ball.draw()
def update(dt):
    uy=red_ball.vy
    red_ball.vy+=a*dt
    s=(uy+red_ball.vy)/2*dt
    red_ball.y+=s

    ux=red_ball.vx
    red_ball.vx+=2000*dt
    s=(ux+red_ball.vx)/2*dt
    red_ball.x+=s
    if red_ball.x > WIDTH - red_ball.radius:
        red_ball.vx *= -0.85
        red_ball.x = WIDTH - red_ball.radius

   
    if red_ball.x < red_ball.radius:
        red_ball.vx *= -0.85
        red_ball.x = red_ball.radius
    if red_ball.y>600-red_ball.radius:
        red_ball.vy*=-0.85
        red_ball.y=600-red_ball.radius
        
pgzrun.go()

