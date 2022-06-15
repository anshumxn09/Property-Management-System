# from tkinter import *
# from PIL import ImageTk, Image
# import mySQLConnection as database
#
# frame = Tk()
#
# frame.geometry("1266x668+50+20")
# frame.minsize(1266, 668)
# frame.maxsize(1266, 668)
# frame.title("Property Management System")
# myicon = PhotoImage(file='myIcon.png')
# frame.iconphoto(False, myicon)
#
#  = Frame(frame)
# .place(x=30, y=20, width=1206, height=628)
# passFrame.config(bg="white")
#
# search = Label(passFrame, text="Enter Purchaser's ID : ", font=("Times New Roman", 16))
# search.place(x=383, y=20)
# search.config(bg="white", fg="darkmagenta")
#
# searchEntry = Entry(passFrame, font=("Times New Roman", 16))
# searchEntry.place(x=580, y=20)
# searchEntry.config(fg="darkmagenta", highlightcolor="darkmagenta",
#                    highlightbackground="darkmagenta",
#                    highlightthickness=1)
# dottedBorder = Label(passFrame, font=("Lato", 12))
# dottedBorder.place(x=0, y=60)
# for i in range(500):
#     dottedBorder.config(text="-"*i, fg="darkmagenta", bg="white")
#
# searchButton = Button(passFrame)
# searchButton.place(x=810, y=20)
#
# # database.myQuery.execute(f"select * from mypurchase where p_id = {searchEntry.get()}")
#
# Name = Label(passFrame, text="Purchaser's Name : ", font=("Times New Roman", 14))
# Name.place(x=70, y=70+20)
# Name.config(fg="darkmagenta", bg="white")
# pname = Label(passFrame, font=("Times New Roman", 14))
# pname.place(x=260, y=70+20)
# pname.config(bg="purple")
#
# Address = Label(passFrame, text="Purchaser's Address : ", font=("Times New Roman", 14))
# Address.place(x=70, y=120+20)
# Address.config(fg="darkmagenta", bg="white")
# padd = Label(passFrame, font=("Times New Roman", 14))
# padd.place(x=260, y=120+20)
# padd.config(bg="purple")
#
# BType = Label(passFrame, text="Building Type : ", font=("Times New Roman", 14))
# BType.place(x=70, y=170+20)
# BType.config(fg="darkmagenta", bg="white")
# pb = Label(passFrame, font=("Times New Roman", 14))
# pb.place(x=260, y=170+20)
# pb.config(bg="purple")
#
# AType = Label(passFrame, text="Area Type: ", font=("Times New Roman", 14))
# AType.place(x=70, y=220+20)
# AType.config(fg="darkmagenta", bg="white")
# pa = Label(passFrame, font=("Times New Roman", 14))
# pa.place(x=260, y=220+20)
# pa.config(bg="purple")
#
# ASqft = Label(passFrame, text="Area (SqFT) : ", font=("Times New Roman", 14))
# ASqft.place(x=70, y=270+20)
# ASqft.config(fg="darkmagenta", bg="white")
# pas = Label(passFrame, font=("Times New Roman", 14))
# pas.place(x=260, y=270+20)
# pas.config(bg="purple")
#
# Location = Label(passFrame, text="Location: ", font=("Times New Roman", 14))
# Location.place(x=70, y=320+20)
# Location.config(fg="darkmagenta", bg="white")
# pl = Label(passFrame, font=("Times New Roman", 14))
# pl.place(x=260, y=320+20)
# pl.config(bg="purple")
#
# Landamrk = Label(passFrame, text="Landmark : ", font=("Times New Roman", 14))
# Landamrk.place(x=70, y=370+20)
# Landamrk.config(fg="darkmagenta", bg="white")
# plm = Label(passFrame, font=("Times New Roman", 14))
# plm.place(x=260, y=370+20)
# plm.config(bg="purple")
#
# Up = Label(passFrame, text="Upper Price : ", font=("Times New Roman", 14))
# Up.place(x=70, y=420+20)
# Up.config(fg="darkmagenta", bg="white")
# pu = Label(passFrame, font=("Times New Roman", 14))
# pu.place(x=260, y=420+20)
# pu.config(bg="purple")
#
# Lp = Label(passFrame, text="Lower Price : ", font=("Times New Roman", 14))
# Lp.place(x=70, y=470+20)
# Lp.config(fg="darkmagenta", bg="white")
# plp = Label(passFrame, font=("Times New Roman", 14))
# plp.place(x=260, y=470+20)
# plp.config(bg="purple")
#
# Cno = Label(passFrame, text="Contact No. : ", font=("Times New Roman", 14))
# Cno.place(x=70, y=520+20)
# Cno.config(fg="darkmagenta", bg="white")
# pcn = Label(passFrame, font=("Times New Roman", 14))
# pcn.place(x=260, y=520+20)
# pcn.config(bg="purple")
#
# # database.myQuery.execute(f"select * from mypurchase where p_id = {searchEntry.get()}")
# # database.myQuery.execute(f"select * from mypurchase where p_id=9000")
# # myRow = database.myQuery.fetchone()
#
# pname.config(text=myRow[1])
# padd.config(text=myRow[2])
# pb.config(text=myRow[3])
# pa.config(text=myRow[4])
# pas.config(text=myRow[5])
# pl.config(text=myRow[6])
# plm.config(text=myRow[7])
# pu.config(text=myRow[8])
# plp.config(text=myRow[9])
# pcn.config(text=myRow[10])
#
#
# frame.mainloop()
from tkinter import *
from PIL import ImageTk, Image
import mySQLConnection as database
from tkinter import messagebox as popup

passFrame = Tk()
passFrame.geometry("900x550+233+79")
passFrame.title("Property Management System")
passFrame.config(bg="white")


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
    # if PassC not in Pass or Pass not in PassC:
    #     popup.showwarning("Property Management System", "Confirm Password Doesn't Matched With Original "
    #                                                     "Password.")
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
        pass


userNameLabel = Label(passFrame, text="USER NAME : ", font=("Times New Roman", 14))
userNameLabel.place(x=50, y=40)
userNameLabel.config(bg="white", fg="midnightblue")
userName = Entry(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                 highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                 )
userName.place(x=180, y=40, height=25, width=200)

userPassLabel = Label(passFrame, text="PASSWORD : ", font=("Times New Roman", 14))
userPassLabel.place(x=50, y=95)
userPassLabel.config(bg="white", fg="midnightblue")

userPass = Entry(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                 highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                 )
userPass.place(x=180, y=95, height=25, width=200)

userGender = Label(passFrame, text="GENDER : ", font=("Times New Roman", 14))
userGender.place(x=50, y=150)
userGender.config(bg="white", fg="midnightblue")
x = IntVar()
# PY_VAR0
GenderM = Radiobutton(passFrame, text="Male", variable=x, value=1, font=("Times New Roman", 14), fg="midnightblue",
                      bg="white")
GenderM.place(x=153, y=150)
GenderF = Radiobutton(passFrame, text="Female", variable=x, value=2, font=("Times New Roman", 14), fg="midnightblue",
                      bg="white")
GenderF.place(x=233, y=150)

userPhnoLabel = Label(passFrame, text="PHONE NO. : ", font=("Times New Roman", 14))
userPhnoLabel.place(x=50, y=205)
userPhnoLabel.config(bg="white", fg="midnightblue")
userPhno = Entry(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                 highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue")
userPhno.place(x=180, y=205, height=25, width=200)

userAddressLabel = Label(passFrame, text="ADDRESS : ", font=("Times New Roman", 14))
userAddressLabel.place(x=50, y=260)
userAddressLabel.config(bg="white", fg="midnightblue")
userAddress = Text(passFrame, font=("Times New Roman", 14), fg="midnightblue",
                   highlightthickness=1, highlightbackground="midnightblue", highlightcolor="midnightblue"
                   )
userAddress.place(x=180, y=260, height=100, width=200)

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

updateMyDetails = Button(passFrame, text="UPDATE", font=("Times New Roman", 14))
updateMyDetails.place(x=165, y=475)
updateMyDetails.config(bg="midnightblue", fg="white", activebackground="midnightblue",
                       activeforeground="white", command=toVerify)

passFrame.mainloop()