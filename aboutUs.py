from tkinter import *
from PIL import ImageTk, Image
import loginAsa


class AboutUs:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="purple")

        def toMoveBack():
            frame.destroy()
            loginAsa.LoginAsA()

        myWall = ImageTk.PhotoImage(Image.open("aboutUs.jpg"))
        wallLabel = Label(frame, image=myWall)
        wallLabel.place(x=0, y=0, width=663, height=668)

        Back = Button(wallLabel,text="🢘", font=("Times New Roman", 30))
        Back.place(x=10, y=10, height=50, width=60)
        Back.config(bg="#c5e4f9", fg="white", activeforeground="white", activebackground="#c5e4f9",
                    borderwidth=0, command=toMoveBack)

        myWall2 = ImageTk.PhotoImage(Image.open("aboutUs2.jpg"))
        wallLabel2 = Label(frame, image=myWall2)
        wallLabel2.place(x=663, y=0, width=663, height=668)

        frame.mainloop()


if __name__ == "__main__":
    myPage = AboutUs()