"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Basic implementation of Breakout game,
does not account for collision with side of brick or
calculate correct travel affected by bounce.

TODO:: Switch paddle collision bugfix to make ball only bounce upward when colliding with paddle,
    instead of resetting ignore paddle check when colliding with top edge or brick.
    In case other objects are introduced into game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()

    # Initialize variables.
    lives = NUM_LIVES
    bricks_removed = 0
    ignore_paddle = False

    # Animation loop.
    while True:
        if graphics.ball_in_motion is True:
            # Check window edge collision.
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                # Lose life when ball exits bottom edge and checks for lose condition.
                lives -= 1
                if lives == 0:
                    break
                graphics.place_ball()
                # Reset collision detection with paddle.
                ignore_paddle = False
            # Left and right edge detection and fill dx dy values.
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                dx = graphics.set_dx_bounce()
            else:
                dx = graphics.get_dx()
            if graphics.ball.y <= 0:
                dy = graphics.set_dy_bounce()
                ignore_paddle = False
            else:
                dy = graphics.get_dy()
            # Check for object collision
            collision_object = graphics.check_collision()
            if collision_object is not None:
                # Bounce off paddle and ignore further detections until variable reset by top edge or brick.
                if collision_object is graphics.paddle and ignore_paddle is False:
                    dy = graphics.set_dy_bounce()
                    ignore_paddle = True
                # If brick, bounce, remove brick, reset paddle check, and check for win condition.
                elif collision_object is not graphics.paddle:
                    dy = graphics.set_dy_bounce()
                    graphics.window.remove(collision_object)
                    ignore_paddle = False
                    bricks_removed += 1
                    if bricks_removed == graphics.get_brick_count():
                        break
            graphics.ball.move(dx, dy)
        pause(FRAME_RATE)
    graphics.window.clear()
    if bricks_removed == graphics.get_brick_count():
        graphics.window.add(graphics.label_win)
    elif lives == 0:
        graphics.window.add(graphics.label_lose)


if __name__ == '__main__':
    main()
