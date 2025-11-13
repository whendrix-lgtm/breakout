import paddle
import turtle
import unittest

class DummyBall:
  def __init__(self, x=0, y=0, h=0):
    self.x = x
    self.y = y
    self.heading = h
  def xcor(self):
    return self.x
  def ycor(self):
    return self.y
  def setheading(self, head):
    self.heading = head

class PaddleTest (unittest.TestCase):
  def setUp(self):
    screen = turtle.Screen()
    screen.setup(640, 480)
    self.paddle = paddle.Paddle(screen, 0, 32)
  def test_movement(self):
    self.assertEqual(self.paddle.state, paddle.NEUTRAL)
    self.paddle.left()
    self.assertEqual(self.paddle.state, paddle.LEFT)
    for i in range(20):
      self.assertEqual(self.paddle.xcor(), -i*10)
      self.assertEqual(self.paddle.ycor(), 32)
      self.paddle.animate()
    self.paddle.goto(0, 64)
    self.paddle.right()
    self.assertEqual(self.paddle.state, paddle.RIGHT)
    for i in range(20):
      self.assertEqual(self.paddle.xcor(), i*10)
      self.assertEqual(self.paddle.ycor(), 64)
      self.paddle.animate()
    self.paddle.goto(0, 8)
    self.paddle.release()
    self.assertEqual(self.paddle.state, paddle.NEUTRAL)
    for i in range(5):
      self.assertEqual(self.paddle.xcor(), 0)
      self.assertEqual(self.paddle.ycor(), 8)
      self.paddle.animate()
  def test_movement_boundary(self):
    self.paddle.goto(paddle.MAXX-80, 100)
    self.paddle.right()
    for i in range(8):
      self.assertEqual(self.paddle.xcor(), paddle.MAXX - 80 + 10*i)
      self.paddle.animate()
    for i in range(8):
      self.assertEqual(self.paddle.xcor(), paddle.MAXX)
      self.paddle.animate()
    self.paddle.goto(paddle.MINX+80, 100)
    self.paddle.left()
    for i in range(8):
      self.assertEqual(self.paddle.xcor(), paddle.MINX + 80 - 10*i)
      self.paddle.animate()
    for i in range(8):
      self.assertEqual(self.paddle.xcor(), paddle.MINX)
      self.paddle.animate()
  def test_bounce(self):
    self.paddle.goto(90, 90)
    ball = DummyBall()
    ball.y = 90
    for i in range(50, 131):
      ball.x = i
      self.paddle.hit_ball(ball)
      self.assertEqual(ball.heading, 180 - i)
    
    
