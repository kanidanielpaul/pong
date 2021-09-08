import tkinter
from values import constants
from components import paddle, ball

class Pong:
    allConstants = constants.Constants()
    canvasGarbageCollector = []

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(self.allConstants.WindowConstants.TITLE+" "+self.allConstants.WindowConstants.VERSION)
        self.root.geometry(str(self.allConstants.WindowConstants.WIDTH)+"x"+str(self.allConstants.WindowConstants.HEIGHT))
        self.root.configure(bg=self.allConstants.WindowConstants.BACKGROUND_COLOR)
        self.canvas = tkinter.Canvas(self.root,bg=self.allConstants.WindowConstants.BACKGROUND_COLOR,height=self.allConstants.WindowConstants.HEIGHT, width=self.allConstants.WindowConstants.WIDTH)
        self.canvas.grid(row=0,column=0,sticky="nesw")
        self.canvas.create_line(int(self.allConstants.WindowConstants.WIDTH/2),0,int(self.allConstants.WindowConstants.WIDTH/2),self.allConstants.WindowConstants.HEIGHT, fill=self.allConstants.PaddleConstants.PADDLE_COLOR)

    def startGame(self):
        self.deleteAllExistingComponents()
        p1 = paddle.Paddle(self.canvas,0,10)
        p2 = paddle.Paddle(self.canvas,990,10)
        b = ball.Ball(self.canvas,50,50)

    def deleteAllExistingComponents(self):
        for item in self.canvasGarbageCollector:
            self.canvas.delete(item)

    def startMainLoop(self):
        self.root.mainloop()