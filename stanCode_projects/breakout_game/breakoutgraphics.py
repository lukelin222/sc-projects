"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Basic implementation of Breakout graphics.
Collision check does not account for multiple objects and
checks four corners instead of ball outline.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius, ball_radius, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.ball.filled = True
        self.place_ball()

        # Initialize our mouse listeners.
        onmouseclicked(self.launch_ball)
        onmousemoved(self.move_paddle)

        # Draw bricks.
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height,
                              x=j*(brick_width+brick_spacing), y=brick_offset+i*(brick_height+brick_spacing))
                brick.filled = True
                brick.fill_color = color[i//2]
                self.window.add(brick)

        # Create winning label.
        self.label_win = GLabel('YOU WIN!')
        self.label_win.font = '-40'
        self.label_win.x = (window_width-self.label_win.width)/2
        self.label_win.y = (window_height-self.label_win.height)/2

        # Create losing label.
        self.label_lose = GLabel('GAME OVER!')
        self.label_lose.font = '-40'
        self.label_lose.x = (window_width-self.label_lose.width)/2
        self.label_lose.y = (window_height-self.label_lose.height)/2

    # Returns count of bricks to remove for win condition.
    @staticmethod
    def get_brick_count():
        return BRICK_COLS*BRICK_ROWS

    # Getters and setters.
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx_bounce(self):
        self.__dx *= -1
        return self.__dx

    def set_dy_bounce(self):
        self.__dy *= -1
        return self.__dy

    # Reset ball, used in constructor and when life lost.
    def place_ball(self):
        # Center ball and stop animation loop.
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.ball_in_motion = False
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # On mouse clicked, set variable that allows animation loop to run.
    def launch_ball(self, mouse):
        self.ball_in_motion = True
        return

    # Paddle y is fixed and x is center of mouse.x, without allowing paddle to exceed borders.
    def move_paddle(self, mouse):
        if mouse.x <= self.paddle.width/2:
            x = 0
        elif mouse.x+self.paddle.width/2 >= self.window.width:
            x = self.window.width - self.paddle.width
        else:
            x = mouse.x-(self.paddle.width/2)
        self.paddle.x = x
        return

    # Check four corners for collision and return object if collision detected.
    def check_collision(self):
        top_left = self.window.get_object_at(self.ball.x, self.ball.y)
        top_right = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        bottom_left = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        bottom_right = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        if top_left is not None:
            return top_left
        if top_right is not None:
            return top_right
        if bottom_left is not None:
            return bottom_left
        if bottom_right is not None:
            return bottom_right
        return None
