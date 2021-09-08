from values import constants

class Paddle:
    allConstants = constants.Constants()

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.paddle = self.canvas.create_rectangle(x,y,x+self.allConstants.PaddleConstants.PADDLE_WIDTH,y+self.allConstants.PaddleConstants.PADDLE_HEIGHT,fill='white')