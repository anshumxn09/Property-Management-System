from tkinter import *
import clientMain, updateMyDetails
import mySQLConnection as database
from PIL import ImageTk, Image
from tkinter import messagebox as popup


class MyDetails:
    def __init__(self, myResults):

        frame = Tk()
        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)

        frame.config(bg="lavender")

        def toMoveBack():
            frame.destroy()
            newPage = clientMain.ClientMain(myResults)

        # try:
        #     database.myQuery.execute(f"select * from myUser where user_id={LoginID}")
        #     myResults = database.myQuery.fetchone()
        #     print(myResults)
        # except:
        #     print("hey bro")

        def getPass():
            frame.destroy()
            updateMyDetails.UpdateMyDetails(myResults)

        def toUpdatePage():
            # popup.askyesno("Property Management System", "Want to update your info : ")
            if popup.askyesno("Property Management System", "Want to update your info?"):
                getPass()
            else:
                pass

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="white")

        myWall = ImageTk.PhotoImage(Image.open("myDetails.jpg"))
        myWallpaper = Label(newWindow, image=myWall)
        myWallpaper.place(x=40, y=0, width=500, height=628)
        myWallpaper.config(bg="black")

        userIDLabel = Label(newWindow, text="USER ID : ", font=("Times New Roman", 14))
        userIDLabel.place(x=640, y=70)
        userIDLabel.config(bg="white", fg="royal blue")
        showID = Label(newWindow, text=myResults[0], font=("Times New Roman", 14, "bold"))
        showID.place(x=790, y=70)
        showID.config(bg="white", fg="royal blue")

        userNameLabel = Label(newWindow, text="USER NAME : ", font=("Times New Roman", 14))
        userNameLabel.place(x=607, y=140)
        userNameLabel.config(bg="white", fg="royal blue")
        showName = Label(newWindow, text=myResults[1], font=("Times New Roman", 14, "bold"))
        showName.place(x=790, y=140)
        showName.config(bg="white", fg="royal blue")

        userPassLabel = Label(newWindow, text="PASSWORD : ", font=("Times New Roman", 14))
        userPassLabel.place(x=607, y=210)
        userPassLabel.config(bg="white", fg="royal blue")
        showPass = Label(newWindow, text=myResults[2], font=("Times New Roman", 14, "bold"))
        showPass.place(x=790, y=210)
        showPass.config(bg="white", fg="royal blue")

        userGender = Label(newWindow, text="GENDER : ", font=("Times New Roman", 14))
        userGender.place(x=607, y=280)
        userGender.config(bg="white", fg="royal blue")
        showGen = Label(newWindow, text=myResults[3], font=("Times New Roman", 14, "bold"))
        showGen.place(x=790, y=280)
        showGen.config(bg="white", fg="royal blue")

        userPhnoLabel = Label(newWindow, text="PHONE NO. : ", font=("Times New Roman", 14))
        userPhnoLabel.place(x=607, y=350)
        userPhnoLabel.config(bg="white", fg="royal blue")
        showPhno = Label(newWindow, text=myResults[6], font=("Times New Roman", 14, "bold"))
        showPhno.place(x=790, y=350)
        showPhno.config(bg="white", fg="royal blue")

        userAddressLabel = Label(newWindow, text="ADDRESS : ", font=("Times New Roman", 14))
        userAddressLabel.place(x=607, y=420)
        userAddressLabel.config(bg="white", fg="royal blue")
        showAdd = Label(newWindow, text=myResults[4], font=("Times New Roman", 14, "bold"))
        showAdd.place(x=790, y=420)
        showAdd.config(bg="white", fg="royal blue")

        userDobLabel = Label(newWindow, text="Date Of Birth : ", font=("Times New Roman", 14))
        userDobLabel.place(x=607, y=490)
        userDobLabel.config(bg="white", fg="royal blue")
        showdob = Label(newWindow, text=myResults[5], font=("Times New Roman", 14, "bold"))
        showdob.place(x=790, y=490)
        showdob.config(bg="white", fg="royal blue")

        button = Button(newWindow, text="↤", font=("Lato", 30, "bold"), borderwidth=0, command=toMoveBack)
        button.place(x=790, y=565, width=100, height=30)
        button.config(bg="lavender", fg="royal blue", activeforeground="royal blue", activebackground="white")

        mybtn = ImageTk.PhotoImage(Image.open("infoo.jpg"))
        UpdateButton = Button(newWindow, text="i", font=("Times New Roman", 14),
                              command=toUpdatePage,
                              image=mybtn)
        UpdateButton.place(x=1136, y=20, height=50, width=50)
        UpdateButton.config(borderwidth=0)

        frame.title(f"Property Management System - Hello {myResults[1]}")
        frame.mainloop()


if __name__ == "__main__":
    myPage = MyDetails(("hey", 0, 0, "Male", 0, 0, 0))
