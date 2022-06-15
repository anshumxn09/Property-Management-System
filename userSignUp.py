from tkinter import *
from PIL import ImageTk, Image
import mySQLConnection as dataBase, clientLogin
from tkinter import messagebox as popup


class UserSignUp:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        frame.config(bg="midnightblue")
        myGender = "Love"

        dataBase.myQuery.execute("select * from myUser order by user_id")
        myResult = dataBase.myQuery.fetchall()
        lastID = ()
        for x in myResult:
            lastID = x
        myNewID = lastID[0] + 1

        def toSubmit():
            global myGender
            psuedoName = userName.get()
            psuedoPass = userPass.get()
            psuedoPassC = userPassC.get()
            psuedoMobile = userPhno.get()
            psuedoAdd = userAddress.get(1.0, END)
            psuedoDob = userdob.get()

            Name = psuedoName.strip()
            Pass = psuedoPass.strip()
            PassC = psuedoPassC.strip()
            Mobile = psuedoMobile.strip()
            Add = psuedoAdd.strip()
            Dob = psuedoDob.strip()

            if Name in "" or Pass in "" or PassC in "" or Mobile in "" or Add in "" or Dob in "":
                popup.showwarning("Property Management System", "Oops! Some Field Are Left To Fill.")
                return
            if PassC not in Pass or Pass not in PassC:
                popup.showwarning("Property Management System", "Confirm Password Doesn't Matched With Original "
                                                                "Password.")
                return

            if x.get() == 1:
                myGender = "Male"
            elif x.get() == 2:
                myGender = "Female"
            else:
                popup.showwarning("Property Management System", "Kindly select gender field.")
                return

            if len(Mobile) > 10 :
                popup.showwarning("Property Management System", "Contact Number is Greater Than 10 Digits.")
                return

            if len(Mobile) < 10:
                popup.showwarning("Property Management System", "Contact Number is Lesser Than 10 Digits.")
                return

            if len(Add) > 300:
                popup.showwarning("Property Management System", "Address Field is Greater Than 300 Digits.")
            else:
                try:
                    check = int(Mobile)
                    myQuery = "insert into myUser values(%s, %s, %s, %s, %s, %s, %s)"
                    val = (myNewID, Name, Pass, myGender, Add, Dob, Mobile)
                    dataBase.myQuery.execute(myQuery, val)
                    dataBase.myDatabase.commit()
                    frame.destroy()
                    newPage = clientLogin.ClientLogin()
                except:
                    popup.showwarning("Property Management System", "Kindly Enter Valid Phone Number!!")

        def toMoveBack():
            frame.destroy()
            newPage = clientLogin.ClientLogin()

        newWindow = Frame(frame)
        newWindow.place(x=30, y=20, width=1206, height=628)
        newWindow.config(bg="white")

        myWall = ImageTk.PhotoImage(Image.open("userSignUp.jpg"))
        myWallpaper = Label(newWindow, image=myWall)
        myWallpaper.place(x=0, y=0, width=500, height=628)
        myWallpaper.config(bg="black")

        userIDLabel = Label(newWindow, text="USER ID : ", font=("Times New Roman", 14))
        userIDLabel.place(x=590, y=45)
        userIDLabel.config(bg="white", fg="midnightblue")
        userID = Label(newWindow, text=myNewID, font=("Times New Roman", 14, "bold"))
        userID.place(x=690, y=45, height=25, width=200)
        userID.config(bg="white", fg="midnightblue")

        userNameLabel = Label(newWindow, text="USER NAME : ", font=("Times New Roman", 14))
        userNameLabel.place(x=557, y=100)
        userNameLabel.config(bg="white", fg="midnightblue")
        userName = Entry(newWindow, font=("Times New Roman", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                         )
        userName.place(x=690, y=100, height=25, width=200)

        userPassLabel = Label(newWindow, text="PASSWORD : ", font=("Times New Roman", 14))
        userPassLabel.place(x=557, y=155)
        userPassLabel.config(bg="white", fg="midnightblue")

        userPass = Entry(newWindow, font=("Times New Roman", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                         )
        userPass.place(x=690, y=155, height=25, width=200)

        userPassCLabel = Label(newWindow, text="CONFIRM PASSWORD : ", font=("Times New Roman", 14))
        userPassCLabel.place(x=557, y=210)
        userPassCLabel.config(bg="white", fg="midnightblue")
        userPassC = Entry(newWindow, font=("Times New Roman", 14), fg="midnightblue",
                          highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                          )
        userPassC.place(x=780, y=210, height=25, width=200)

        userGender = Label(newWindow, text="GENDER : ", font=("Times New Roman", 14))
        userGender.place(x=557, y=265)
        userGender.config(bg="white", fg="midnightblue")
        x = IntVar()
        # PY_VAR0
        GenderM = Radiobutton(newWindow, text="Male", variable=x, value=1, font=("Times New Roman", 14), fg="midnightblue",
                              bg="white")
        GenderM.place(x=660, y=265)
        GenderF = Radiobutton(newWindow, text="Female", variable=x, value=2, font=("Times New Roman", 14), fg="midnightblue",
                              bg="white")
        GenderF.place(x=740, y=265)

        userPhnoLabel = Label(newWindow, text="PHONE NO. : ", font=("Times New Roman", 14))
        userPhnoLabel.place(x=557, y=320)
        userPhnoLabel.config(bg="white", fg="midnightblue")
        userPhno = Entry(newWindow, font=("Times New Roman", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue")
        userPhno.place(x=690, y=320, height=25, width=200)

        userAddressLabel = Label(newWindow, text="ADDRESS : ", font=("Times New Roman", 14))
        userAddressLabel.place(x=557, y=375)
        userAddressLabel.config(bg="white", fg="midnightblue")
        userAddress = Text(newWindow, font=("Times New Roman", 14), fg="midnightblue",
                           highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                           )
        userAddress.place(x=690, y=375, height=100, width=200)

        warn = Label(newWindow, text="Maximum : 300 Words.")
        warn.place(x=690, y=480)
        warn.config(fg="red", bg="white")

        userDobLabel = Label(newWindow, text="Date Of Birth : ", font=("Times New Roman", 14))
        userDobLabel.place(x=557, y=510)
        userDobLabel.config(bg="white", fg="midnightblue")
        userdob = Entry(newWindow, font=("Times New Roman", 14), fg="midnightblue",
                        highlightthickness=0.5, highlightbackground="midnightblue", highlightcolor="midnightblue",
                        )
        userdob.place(x=690, y=510, height=25, width=200)

        submit = Button(newWindow, text="SUBMIT", font=("Times New Roman", 14), command=toSubmit)
        submit.place(x=803, y=565, height=30, width=100)
        submit.config(bg="midnightblue", fg="white", activeforeground="midnightblue")

        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)

        button = Button(newWindow, command=toMoveBack, text="↤", font=("Lato", 30, "bold"))
        button.place(x=683, y=565, width=100, height=30)
        button.config(bg="midnightblue", fg="white", activeforeground="midnightblue")

        frame.mainloop()


if __name__ == "__main__":
    myWindow = UserSignUp()
