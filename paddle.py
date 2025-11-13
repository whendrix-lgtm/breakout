import turtle

SPEED = 10
HEIGHT = 10
WIDTH = 70

STARTX = 0
STARTY = -200
MINX = -280
MAXX = -MINX

LEFT = -1
RIGHT = 1
NEUTRAL = 0

class Paddle (turtle.Turtle):
  def __init__(self, screen, x = STARTX, y = STARTY):
    '''
      Creates the paddle at the given location
      Initially not moving (state = NEUTRAL)
      Sets up the screen so that pressing Left/Right calls .left()/.right()
        Releasing Left/Right calls .release()
    '''
    turtle.Turtle.__init__(self)
    screen.addshape("paddle.gif")
    self.shape("paddle.gif")
  def animate(self):
    '''
      Moves the paddle left or right 10 px based on state
      Will not move if past MINX or MAXX
    '''
    pass
  def left(self, amt=SPEED):
    '''Sets state to LEFT'''
    self.state = LEFT
  def right(self, amt=SPEED):
    '''Sets state to RIGHT'''
    self.state = RIGHT
  def release(self):
    '''Sets state to NEUTRAL'''
    self.state = NEUTRAL
  def width(self):
    '''Returns width'''
    return WIDTH
  def height(self):
    '''Returns height'''
    return HEIGHT
  def hit_ball(self, ball):
    '''
      Called when striking the ball
      Bounces the ball so that ball's heading is set to 90 if dead center (same x coords)
      Adjust angle by deltaX (leftward on left side, rightward on right side)
    '''
    pass

if __name__ == '__main__':
  # Short demo
  # Move paddle with Left and Right
  # End demo with Escape
  screen = turtle.Screen()
  screen.setup(640, 480)
  make_paddle(screen)
  def animate():
    paddle.animate()
    screen.ontimer(animate, 10)
  screen.listen()
  screen.ontimer(animate, 10)
  screen.onkey(screen.bye, 'Escape')
  screen.mainloop()
