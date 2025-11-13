import ball
import unittest
import math
import turtle

class DummyBrick:
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
  def xcor(self):
    return self.x
  def ycor(self):
    return self.y
  def width(self):
    return self.w
  def height(self):
    return self.h

class BallTest (unittest.TestCase):
  def setUp(self):
    screen = turtle.Screen()
    screen.setup(640, 320)
    self.ball = ball.Ball(screen)
  def test_bouncing(self):
    theta1 = list(range(0, 360, 2))
    theta2 = list(range(180, -1, -2)) + list(range(358,180,-2))
    theta3 = [0] + list(range(358, 0, -2))
    for i in range(len(theta1)):
      self.ball.setheading(theta1[i])
      self.ball.hbounce()
      self.assertEqual(self.ball.heading(), theta2[i]) # horizontal bouncing
    for i in range(len(theta1)):
      self.ball.setheading(theta1[i])
      self.ball.vbounce()
      self.assertEqual(self.ball.heading(), theta3[i]) # vertical bouncing
    self.ball.spd = 1000000000
    self.ball.vbounce()
    self.assertEqual(round(self.ball.spd), 1005000000)
    self.ball.vbounce()
    self.assertEqual(round(self.ball.spd), 1010025000)
    self.ball.vbounce()
    self.assertEqual(round(self.ball.spd), 1015075125)
    self.ball.spd = 1000000000
    self.ball.hbounce()
    self.assertEqual(round(self.ball.spd), 1005000000)
    self.ball.hbounce()
    self.assertEqual(round(self.ball.spd), 1010025000)
    self.ball.hbounce()
    self.assertEqual(round(self.ball.spd), 1015075125)
  def test_movement(self):
    self.ball.spd = 1000
    for i in range(360, 2):
      self.ball.goto(0, 0)
      self.ball.setheading(i)
      self.ball.animate()
      self.assertEqual(round(self.ball.xcor()), round(1000*math.cos(math.radians(i))))
      self.assertEqual(round(self.ball.ycor()), round(1000*math.sin(math.radians(i))))
    self.ball.setheading(0)
    for y in range(50, 10):
      self.ball.goto(305, y)
      self.ball.spd = 10
      self.ball.animate()
      self.ball.animate()
      self.assertEqual(self.ball.xcor(), 304.95) # right wall bounce
      self.assertEqual(self.ball.heading(), 180)
      self.ball.goto(-305, y)
      self.ball.spd = 10
      self.ball.animate()
      self.ball.animate()
      self.assertEqual(self.ball.xcor(), -304.95) # left wall bounce
      self.assertEqual(self.ball.heading(), 0)
    for x in range(-50, 50, 10):
      self.ball.goto(x, 225)
      self.ball.setheading(90)
      self.ball.spd = 10
      self.ball.animate()
      self.ball.animate()
      self.assertEqual(self.ball.ycor(), 224.95) # top wall bounce
      self.assertEqual(self.ball.heading(), 270)
      self.ball.goto(x, -225)
      self.ball.spd = 10
      self.ball.animate()
      self.ball.animate()
      self.assertEqual(self.ball.ycor(), -245) # bottom - no bounce
      self.assertEqual(self.ball.heading(), 270)
  def test_intersection(self):
    brik = DummyBrick(128, 128, 32, 32)
    for x in range(98, 158, 4):
      for y in range(98, 158, 4):
        self.ball.goto(x+0.5, y+0.5)
        if abs(x-128) < 20 and abs(y-128) < 20:
          self.assertTrue(self.ball.hits(brik))
        else:
          self.assertFalse(self.ball.hits(brik))
