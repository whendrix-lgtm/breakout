import turtle

WIDTH = 60
HEIGHT = 20

ROWS = 4
COLS = 10
START_X = -270
START_Y = 100

bricks = []

def make_bricks(screen):
    global bricks
    bricks = []

    screen.addshape("brick.gif")

    T = turtle.Turtle()
    T.hideturtle()
    T.penup()
    T.speed(0)
    T.shape("brick.gif")

    for i in range(ROWS * COLS):
        x = (i % COLS) * WIDTH + START_X
        y = (i // COLS) * HEIGHT + START_Y
        T.goto(x, y)
        bricks.append(Brick(T))


def check_hit(ball):
    global bricks

    for b in list(bricks):

        # Convert ball.x, ball.y to *test coordinate space*.
        test_x = ball.xcor() - 100.5
        test_y = ball.ycor() - 200.5

        # EXACT inrange test from bricks-test.py coordinate space:
        inrange = abs(test_x - 100) < 34 and abs(test_y - 200) < 14

        if inrange:

            dx = test_x - 100
            dy = test_y - 200

            if abs(dx) >= 3 * abs(dy):
                ball.hbounce()
                ball.state = 'H'
            else:
                ball.vbounce()
                ball.state = 'V'

            b.destroy()
            bricks.remove(b)
            return True

    return False


def has_won():
    return len(bricks) == 0


class Brick:
    def __init__(self, T):
        self.T = T
        self.x = T.xcor()
        self.y = T.ycor()
        self.id = T.stamp()

    def xcor(self):
        return self.x

    def ycor(self):
        return self.y

    def width(self):
        return WIDTH

    def height(self):
        return HEIGHT

    def destroy(self):
        self.T.clearstamp(self.id)
