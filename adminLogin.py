from tkinter import *
from PIL import ImageTk, Image
import toAsk ,mySQLConnection as dataBase
from tkinter import messagebox as popup
import adminMainPage


class AdminLogin:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="purple")

        def toCheck(adminName, adminPassword):
            try:
                toTest = int(adminName)
                try:
                    dataBase.myQuery.execute(f"select * from myAdmin where admin_id={adminName}")
                    if dataBase.myQuery:
                        myResults = dataBase.myQuery.fetchone()
                        if myResults[2] in adminPassword:
                            frame.destroy()
                            newPage = adminMainPage.AdminMainPage()
                        else:
                            popup.showwarning("Property Management System", "Valid Password is REQUIRED")
                except:
                    popup.showwarning("Property Management System", "Enter Valid ID And Password!!")
            except:
                popup.showwarning("Property Management System", "Valid ID is REQUIRED")

        def loginMe():
            psuedoAdmin = usernameEntry.get()
            psuedoPass = passwordEntry.get()
            adminName = psuedoAdmin.strip()
            adminPassword = psuedoPass.strip()

            if adminName in "" and adminPassword in "":
                popup.showwarning("Property Management System", "Kindly Enter ID And Password")
            elif adminPassword in "":
                popup.showwarning("Property Management System", "Password Field is REQUIRED")
            elif adminName in "":
                popup.showwarning("Property Management System", "ID Field is REQUIRED")
            else:
                toCheck(adminName,adminPassword)

        myWallpaper = ImageTk.PhotoImage(Image.open("areyouaa.jpeg"))
        areYouA = Label(frame, image=myWallpaper)
        areYouA.place(x=0, y=0)

        newWindow = Frame(frame)
        newWindow.place(x=233, y=84, width=800, height=500)
        newWindow.config(bg="white")

        clientPic = ImageTk.PhotoImage(Image.open("adminLogin.jpg"))
        clientImageLabel = Label(newWindow, image=clientPic, borderwidth=0)
        clientImageLabel.place(x=40, y=40)

        usernameLabel = Label(newWindow, text="Admin ID : ", font=("Times New Roman", 16))
        usernameLabel.place(x=470, y=140)
        usernameLabel.config(bg="white")
        usernameEntry = Entry(newWindow, font=("Times New Roman", 16))
        usernameEntry.config(bg="sky blue", fg="black")
        usernameEntry.place(x=470, y=170)

        passwordLabel = Label(newWindow, text="Password : ", font=("Times New Roman", 16))
        passwordLabel.place(x=470, y=200)
        passwordLabel.config(bg="white")
        passwordEntry = Entry(newWindow, font=("Times New Roman", 16), show="*")
        passwordEntry.config(bg="sky blue", fg="black")
        passwordEntry.place(x=470, y=230)

        loginButton = Button(newWindow, text="Login", font=("Times New Roman", 16), command=loginMe)
        loginButton.place(x=500, y=280, width=160, height=30)
        loginButton.config(bg="light green", fg="dark blue", activebackground="sky blue", activeforeground="black",
                           borderwidth=0)

        def toMoveBack():
            frame.destroy()
            newPage = toAsk.ToAsk()

        button = Button(frame, command=toMoveBack, text="↤", font=("Lato", 30, "bold"))
        button.place(x=20, y=30, width=100, height=40)
        button.config(bg="white", borderwidth=1)
        frame.mainloop()


if __name__ == "__main__":
    myWindow = AdminLogin()
