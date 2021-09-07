import tkinter
from values import constants


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

    def startGame(self):
        self.deleteAllExistingComponents()
        self.player1 = self.canvas.create_rectangle()

    def deleteAllExistingComponents(self):
        for item in self.canvasGarbageCollector:
            self.canvas.delete(item)

    def startMainLoop(self):
        self.root.mainloop()