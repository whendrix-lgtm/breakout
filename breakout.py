'''
  Script that simulates the game Breakout

  Controls:  Left/Right to move, Escape to quit
'''

import turtle
import paddle
import ball
import bricks
import time

ANIM_DELAY = 20

if __name__ == '__main__':
  screen = turtle.Screen()
  screen.setup(640, 480)
  screen.title('Breakout')
  ball = ball.Ball(screen)
  paddle = paddle.Paddle(screen)
  bricks.make_bricks(screen)

  # Main animation loop
  def animate():
    start = time.time()
    ball.animate()
    paddle.animate()
    bricks.check_hit(ball)
    if ball.has_lost():
      print('Game over')
      screen.bye()
    elif bricks.has_won():
      print("You win!!!")
      screen.bye()
    else:
      delay = ANIM_DELAY - (time.time() - start) *1000
      if delay > 0:
        screen.ontimer(animate, int(delay))
      else:
        screen.ontimer(animate, 0)
    if ball.hits(paddle):
      paddle.hit_ball(ball)
  
  screen.listen()
  screen.onkey(screen.bye, 'Escape')
  screen.ontimer(animate, ANIM_DELAY)
  screen.mainloop()
