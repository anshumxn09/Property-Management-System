from tkinter import *
from PIL import ImageTk, Image
import toAsk, clientLogin, myDetails, purchasePage, rentPage, sellPage, newAddPage0
import mySQLConnection as database


class ClientMain:

    def __init__(self, LoginID):
        frame = Tk()
        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="cornsilk")

        def showMyDetails():
            global myResults
            try:
                database.myQuery.execute(f"select * from myUser where user_id={LoginID}")
                myResults = database.myQuery.fetchone()
                # print(myResults)
            except:
                print("hey bro")
            frame.destroy()
            newPage = myDetails.MyDetails(myResults)

        def toMoveBack():
            frame.destroy()
            newPage = clientLogin.ClientLogin()

        def toMoveOnPurchasePage():
            frame.destroy()
            newPage = newAddPage0.NewAddPage0(LoginID)

        def toMoveOnRentPage():
            frame.destroy()
            newPage = rentPage.Rent(LoginID)

        def toMoveOnSellPage():
            frame.destroy()
            newPage = sellPage.Sell(LoginID)

        pur = ImageTk.PhotoImage(Image.open("purchasePic.jpg"))
        myFrame1 = Label(frame, image=pur)
        myFrame1.place(x=0, y=0, width=422, height=494)
        myFrame1.config(bg="cornsilk")
        myPur = Button(frame, text="PURCHASE", font=("Times New Roman", 24, "bold"), borderwidth=0,
                       command=toMoveOnPurchasePage)
        myPur.place(x=0, y=494, width=422, height=40)
        myPur.config(bg="royal blue", fg="white", activeforeground="royal blue", activebackground="white")

        ren = ImageTk.PhotoImage(Image.open("rentPic.jpg"))
        myFrame2 = Label(frame, image=ren)
        myFrame2.place(x=422, y=0, width=422, height=494)
        myFrame2.config(bg="aqua")
        myRen = Button(frame, text="RENT", font=("Times New Roman", 24, "bold"), borderwidth=0,
                       command=toMoveOnRentPage)
        myRen.place(x=422, y=494, width=422, height=40)
        myRen.config(bg="royal blue", fg="white", activeforeground="royal blue", activebackground="white")

        sell = ImageTk.PhotoImage(Image.open("sellPic.jpg"))
        myFrame3 = Label(frame, image=sell)
        myFrame3.place(x=844, y=0, width=422, height=494)
        mySol = Button(frame, text="SELL", font=("Times New Roman", 24, "bold"), borderwidth=0,
                       command=toMoveOnSellPage)
        mySol.place(x=844, y=494, width=422, height=40)
        mySol.config(bg="royal blue", fg="white", activeforeground="royal blue", activebackground="white")

        myInfo = Button(frame, text="Show My Details", font=("Times New Roman", 18, "bold"), command=showMyDetails)
        myInfo.place(x=0, y=534, width=1266, height=78.2)
        myInfo.config(bg="white", fg="Royal Blue", borderwidth=0, activeforeground="royal blue",
                      activebackground="white")

        Back = Button(frame, text="↤", font=("Lato", 30, "bold"), command=toMoveBack)
        Back.place(x=0, y=612.2, width=1266, height=55)
        Back.config(bg="royal blue", fg="white", borderwidth=0
                    , activeforeground="white",
                    activebackground="Royal Blue")

        frame.mainloop()


if __name__ == "__main__":
    myWindow = ClientMain(9)
