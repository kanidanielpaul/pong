from values import constants

class Ball:
    allConstants = constants.Constants()

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.canvas.create_oval(x,y,x+self.allConstants.BallConstants.BALL_WIDTH,y+self.allConstants.BallConstants.BALL_HEIGHT,fill=self.allConstants.BallConstants.BALL_COLOR)