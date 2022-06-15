from tkinter import *
from PIL import ImageTk, Image
import adminLogin, adminCombination


class AdminMainPage:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="aliceblue")

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="cornflowerblue")

        myWall = ImageTk.PhotoImage(Image.open("adminMainPage.jpg"))
        myWallpaper = Label(newWindow, image=myWall)
        myWallpaper.place(x=506, y=0, width=700, height=628)
        myWallpaper.config(bg="black")

        def toMoveBack():
            frame.destroy()
            newPage = adminLogin.AdminLogin()

        def toMoveComb1():
            frame.destroy()
            adminCombination.AdminCombination(1)

        def toMoveComb2():
            frame.destroy()
            adminCombination.AdminCombination(2)

        def toMoveComb3():
            frame.destroy()
            adminCombination.AdminCombination(3)

        displayButton = Button(newWindow, text="Display", font=("Times New Roman", 24))
        displayButton.place(x=0, y=0, width=506, height=192)
        displayButton.config(borderwidth=0, bg="cornflowerblue", fg="aliceblue",
                             activebackground="navy",
                             activeforeground="cornflowerblue", command=toMoveComb1)

        searchButton = Button(newWindow, text="Search", font=("Times New Roman", 24))
        searchButton.place(x=0, y=192, width=506, height=192)
        searchButton.config(borderwidth=0, bg="coral", fg="navy",
                            activebackground="navy",
                            activeforeground="coral", command=toMoveComb2)

        deleteButton = Button(newWindow, text="Delete", font=("Times New Roman", 24))
        deleteButton.place(x=0, y=384, width=506, height=192)
        deleteButton.config(borderwidth=0, bg="cornflowerblue", fg="aliceblue",
                            activebackground="navy",
                            activeforeground="cornflowerblue", command=toMoveComb3)

        Back = Button(newWindow, text="↤", font=("Lato", 30, "bold"), command=toMoveBack)
        Back.place(x=0, y=576, width=506, height=52)
        Back.config(bg="lightsalmon", fg="navy", borderwidth=0,
                    activebackground="lightsalmon",
                    activeforeground="navy")

        frame.mainloop()


if __name__ == "__main__":
    newPage = AdminMainPage()
