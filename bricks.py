import turtle
import math

WIDTH = 60
HEIGHT = 20

ROWS = 4
COLS = 10
START_X = -270
START_Y = 100

bricks = []
def make_bricks(screen):
  '''
    Makes all of the bricks for Breakout
    4 rows of 10 bricks, starting at (-270, 100)
  '''
  T = turtle.Turtle()
  screen.addshape("brick.gif")
  T.shape("brick.gif")

def check_hit(ball):
  '''
    Checks whether any active brick is hit by ball (based on ball.hits)
    If so:
    * Bounce ball (horizontally if abs(deltaY/deltaX) < width/height;
                   vertically if abs(deltaY/deltaX) >= width/height)
    * Destroy and remove hit brick
    * Return True
  '''
  return False

def has_won():
  '''
    Return whether the player has won (no bricks remain)
  '''
  return False

class Brick:
  def __init__(self, T):
    '''
      Initializes this brick as a stamp of the given Turtle
    '''
    self.T = T
    self.x = T.xcor()
    self.y = T.ycor()
    self.id = T.stamp()
  def xcor(self):
    '''Returns x coordinate of center'''
    return self.x
  def ycor(self):
    '''Returns y coordinate of center'''
    return self.y
  def width(self):
    '''Returns width'''
    return WIDTH
  def height(self):
    '''Returns height'''
    return HEIGHT
  def destroy(self):
    '''Makes this stamp disappear (Turtle.clearstamp(id))'''
    pass
