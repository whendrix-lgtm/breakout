# Breakout lab

This lab represents the game Breakout, in which the player uses a paddle to bounce a ball around the screen and eliminate all bricks.  The ball bounces off the paddle based on how far to the left or right it hits the paddle.

**Main script:**  breakout.py

## Controls

Left/Right:  move paddle
Escape:  quit program


## Testing

The script is incomplete and requires 3 files to function:

* `ball.py`:  script for the ball
* `paddle.py`:  script for the player's paddle
* `bricks.py`:  script for the bricks to break

Each file has a `unittest` test script (`ball-test.py`, `paddle-test.py`, and `bricks-test.py`).  When implementing, use

`python -m unittest testfile`

to test each of these files in turn.  The game should be complete when all tests pass.
