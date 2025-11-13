import bricks
import turtle
import unittest

class MakeTest(unittest.TestCase):
  def test_make(self):
    screen = turtle.Screen()
    screen.addshape('brick.gif')
    bricks.bricks = []
    bricks.make_bricks(screen)
    self.assertEqual(len(bricks.bricks), 40)
    for i in range(len(bricks.bricks)):
      b = bricks.bricks[i]
      self.assertEqual(b.xcor(), (i%10)*60-270)
      self.assertEqual(b.ycor(), (i//10)*20+100)
      self.assertEqual(b.width(), 60)
      self.assertEqual(b.height(), 20)

class TestBall:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.state = '-'
  def hits(self, b):
    return abs(b.xcor()) <= b.width() + 8 and abs(b.ycor()) <= b.height() + 8
  def xcor(self):
    return self.x
  def ycor(self):
    return self.y
  def width(self):
    return 8
  def height(self):
    return 8
  def hbounce(self):
    self.state = 'H'
  def vbounce(self):
    self.state = 'V'

class HitTest (unittest.TestCase):
  def setUp(self):
    screen = turtle.Screen()
    screen.addshape('brick.gif')
    self.T = turtle.Turtle()
    self.T.hideturtle()
    self.T.penup()
    self.T.speed(0)
    self.ball = TestBall()
  def test_ball_hits_brick(self):
    self.T.goto(100, 200)
    for y in range(-20, 20):
      self.ball.y = y + 200.5
      for x in range(-40, 40):
        self.ball.x = x + 100.5
        self.ball.state = '-'
        bricks.bricks = [bricks.Brick(self.T)]
        inrange = abs(x-100) < 34 and abs(y-200) < 14
        self.assertEqual(bricks.check_hit(self.ball), inrange)
        self.assertEqual(len(bricks.bricks), not inrange)
  def test_bounce(self):
    self.T.goto(-100, -200)
    for y in range(-14, 14):
      self.ball.y = y - 199.5
      for x in range(-34, 34):
        self.ball.x = x - 99.5
        self.ball.state = '-'
        bricks.bricks = [bricks.Brick(self.T)]
        bricks.check_hit(self.ball)
        inrange = abs(x+100) < 34 and abs(y+200) < 14
        if not inrange:
          self.assertEqual(self.ball.state, '-')
        elif abs(x+100) >= 3*abs(y+200):
          self.assertEqual(self.ball.state, 'H')
        else:
          self.assertEqual(self.ball.state, 'V')
