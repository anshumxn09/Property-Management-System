from tkinter import *
from PIL import ImageTk, Image
import clientLogin, myDetails
import mySQLConnection as dataBase
from tkinter import messagebox as popup


class UpdateMyDetails:
    def __init__(self, myResults):
        passFrame = Tk()
        passFrame.geometry("900x550+233+79")
        passFrame.title("Property Management System")
        passFrame.config(bg="white")

        def toMoveBack():
            passFrame.destroy()
            myDetails.MyDetails(myResults)

        def toVerify():
            global myGender
            psuedoName = userName.get()
            psuedoPass = userPass.get()
            psuedoMobile = userPhno.get()
            psuedoAdd = userAddress.get(1.0, END)
            psuedoDob = userdob.get()

            Name = psuedoName.strip()
            Pass = psuedoPass.strip()
            Mobile = psuedoMobile.strip()
            Add = psuedoAdd.strip()
            Dob = psuedoDob.strip()

            if Name in "" or Pass in "" or Mobile in "" or Add in "" or Dob in "":
                popup.showwarning("Property Management System", "Oops! Some Field Are Left To Fill.")
                return

            if x.get() == 1:
                myGender = "Male"
            elif x.get() == 2:
                myGender = "Female"
            else:
                popup.showwarning("Property Management System", "Kindly select gender field.")
                return

            if len(Mobile) > 10:
                popup.showwarning("Property Management System", "Contact Number is Greater Than 10 Digits.")
                return
            if len(Add) > 300:
                popup.showwarning("Property Management System", "Address Field is Greater Than 300 Digits.")
            else:
                try:
                    show = int(Mobile)
                    query1 = f"delete from myuser where user_id={myResults[0]}"
                    dataBase.myQuery.execute(query1)
                    dataBase.myDatabase.commit()
                    myQuery = "insert into myUser values(%s, %s, %s, %s, %s, %s, %s)"
                    val = (myResults[0], Name, Pass, myGender, Add, Dob, Mobile)
                    dataBase.myQuery.execute(myQuery, val)
                    dataBase.myDatabase.commit()
                    popup.showinfo("Property Management System", "Updated Successfully!!")
                    passFrame.destroy()
                    clientLogin.ClientLogin()
                except:
                    popup.showwarning("Property Management System", "Kindly Enter Valid Details!!")

        userNameLabel = Label(passFrame, text="USER NAME : ", font=("Times New Roman", 14))
        userNameLabel.place(x=50, y=40)
        userNameLabel.config(bg="white", fg="midnightblue")
        userName = Entry(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                         )
        userName.place(x=180, y=40, height=25, width=200)
        userName.insert(0, myResults[1])

        userPassLabel = Label(passFrame, text="PASSWORD : ", font=("Times New Roman", 14))
        userPassLabel.place(x=50, y=95)
        userPassLabel.config(bg="white", fg="midnightblue")

        userPass = Entry(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                         )
        userPass.place(x=180, y=95, height=25, width=200)
        userPass.insert(0, myResults[2])

        userGender = Label(passFrame, text="GENDER : ", font=("Times New Roman", 14))
        userGender.place(x=50, y=150)
        userGender.config(bg="white", fg="midnightblue")
        x = IntVar()
        # PY_VAR0
        GenderM = Radiobutton(passFrame, text="Male", variable=x, value=1, font=("Times New Roman", 14),
                              fg="midnightblue",
                              bg="white")
        GenderM.place(x=153, y=150)
        GenderF = Radiobutton(passFrame, text="Female", variable=x, value=2, font=("Times New Roman", 14),
                              fg="midnightblue",
                              bg="white")
        GenderF.place(x=233, y=150)
        if myResults[3] == "Male":
            GenderM.select()
            x.set(1)
        else:
            GenderF.select()
            x.set(2)

        userPhnoLabel = Label(passFrame, text="PHONE NO. : ", font=("Times New Roman", 14))
        userPhnoLabel.place(x=50, y=205)
        userPhnoLabel.config(bg="white", fg="midnightblue")
        userPhno = Entry(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                         highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue")
        userPhno.place(x=180, y=205, height=25, width=200)
        userPhno.insert(0, myResults[6])

        userAddressLabel = Label(passFrame, text="ADDRESS : ", font=("Times New Roman", 14))
        userAddressLabel.place(x=50, y=260)
        userAddressLabel.config(bg="white", fg="midnightblue")
        userAddress = Text(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                           highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                           )
        userAddress.place(x=180, y=260, height=100, width=200)
        userAddress.insert(1.0, myResults[4])

        warn = Label(passFrame, text="Maximum : 300 Words.")
        warn.place(x=180, y=365)
        warn.config(fg="red", bg="white")

        userDobLabel = Label(passFrame, text="Date Of Birth : ", font=("Times New Roman", 14))
        userDobLabel.place(x=50, y=420)
        userDobLabel.config(bg="white", fg="midnightblue")
        userdob = Entry(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                        highlightthickness=0.5, highlightbackground="midnightblue", highlightcolor="midnightblue",
                        )
        userdob.place(x=180, y=420, height=25, width=200)
        userdob.insert(0, myResults[5])

        updateMyDetails = Button(passFrame, text="UPDATE", font=("Times New Roman", 14))
        updateMyDetails.place(x=220, y=475, height=40)
        updateMyDetails.config(bg="midnightblue", fg="white", activebackground="midnightblue",
                               activeforeground="white", command=toVerify,
                               borderwidth=0)
        button = Button(passFrame, text="↤", font=("Lato", 30, "bold"), borderwidth=0, command=toMoveBack)
        button.place(x=105, y=475, width=100, height=40)
        button.config(bg="midnightblue", fg="white", activeforeground="white", activebackground="midnightblue")

        mywall = ImageTk.PhotoImage(Image.open("updateDetails.jpg"))
        myWallPaper = Label(passFrame,image=mywall)
        myWallPaper.place(x=400, y=0, width=500, height=550)
        passFrame.mainloop()


if __name__ == '__main__':
    newPage = UpdateMyDetails((909, "Anshuman", "Anshu@123", "Male", "Mumbai", "09-02-2003", "9892609458"))
