from tkinter import *
from PIL import ImageTk, Image
import toAsk, aboutUs


class LoginAsA:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)

        def loginClick():
            frame.destroy()
            toAsk.ToAsk()

        def moveToAboutUs():
            frame.destroy()
            aboutUs.AboutUs()

        header = Label(frame, text="PROPERTY MANAGEMENT SYSTEM", font=("lato", 30, "bold"))
        header.place(x=0, y=0, width=1266, height=65)
        header.config(bg="black", fg="white")

        loginPic = ImageTk.PhotoImage(Image.open("login.jpg"))
        loginLabel = Label(header, image=loginPic)
        loginLabel.place(x=20, y=5, width=50, height=50)

        login = Button(header, text="LOGIN", font=("lato", 20), borderwidth=0,
                       activeforeground="white",
                       activebackground="black",
                       command=loginClick)
        login.place(x=77, y=5, width=80, height=50)
        login.config(bg="black", fg="white")

        aboutPic = ImageTk.PhotoImage(Image.open("info.jpg"))
        aboutLabel = Label(header, image=aboutPic)
        aboutLabel.place(x=1065, y=2, width=50, height=50)

        aboutUss = Button(header, text="ABOUT US", font=("lato", 20), borderwidth=0,
                         activeforeground="white",
                         activebackground="black", command=moveToAboutUs)
        aboutUss.place(x=1111, y=5, width=140, height=50)
        aboutUss.config(bg="black", fg="white")
        mainPic = ImageTk.PhotoImage(Image.open("froPage.jpg"))

        tosetImage = Label(frame, image=mainPic)
        tosetImage.place(x=0, y=60, width=1266, height=608)


        frame.mainloop()


if __name__=="__main__":
    myPage = LoginAsA()