from tkinter import *
root = Tk()
root.geometry("1200x900")
root.resizable(width=FALSE, height=False)
root.title("PhotoNot CC 2018")


topFrame = Frame(root, width=1200, height=100, bg="green")
topFrame.place(x=0, y=0)

controlsFrame = Frame(root, width=200, height=800, bg="Blue")
controlsFrame.place(x=0, y=100)

rotateButton = Button(controlsFrame, text="Rotate", fg="white", bg="RED", width=10, height = 2)
rotateButton.place(x=66, y=5)

titleLabel = Label(topFrame, text="PhotoNot CC 2018", fg="white", bg="green", font=("Impact", 40))
titleLabel.place(x=5, y=15)
exitButton = Button(topFrame, text="CLOSE", bg="RED", fg="WHITE", font="Impact", height=1, width=5, command=quit)
exitButton.place(x=1125, y=15)
root.mainloop()
