from values import constants

class Paddle:
    allConstants = constants.Constants()

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x1 = x
        self.y1 = y
        self.x2 = x + self.allConstants.PaddleConstants.PADDLE_WIDTH
        self.y2 = y + self.allConstants.PaddleConstants.PADDLE_HEIGHT
        self.paddle = self.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill='white')

    def up(self):
        self.canvas.delete(self.paddle)
        self.y1-=self.allConstants.PaddleConstants.PADDLE_SPEED
        self.y2-=self.allConstants.PaddleConstants.PADDLE_SPEED
        self.paddle = self.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill='white')

    def down(self):
        self.canvas.delete(self.paddle)
        self.y1 += self.allConstants.PaddleConstants.PADDLE_SPEED
        self.y2 += self.allConstants.PaddleConstants.PADDLE_SPEED
        self.paddle = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='white')

    def auto(self):
        pass