from tkinter import *
from PIL import ImageTk, Image
import adminMainPage, mypurchaseTable, mySellTable, myRentTable, myUserDetails
import purchaseSearch, rentSearch, sellSearch, userSearch
import delPurchase, delRent, delSell, dellUser


class AdminCombination:
    def __init__(self, pageNumber):
        frame = Tk()
        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Property Management System")
        myicon = PhotoImage(file='myIcon.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="cornsilk")

        def toMoveBack():
            frame.destroy()
            adminMainPage.AdminMainPage()

        def toMoveOnPurchasePage():
            if pageNumber == 1:
                frame.destroy()
                mypurchaseTable.PurchaseTable()
            elif pageNumber == 2:
                frame.destroy()
                purchaseSearch.PurchaseSearch()
            else:
                frame.destroy()
                delPurchase.PurchaseDelete()

        def toMoveOnRentPage():
            if pageNumber == 1:
                frame.destroy()
                myRentTable.RentTable()
            elif pageNumber == 2:
                frame.destroy()
                rentSearch.RentSearch()
            else:
                frame.destroy()
                delRent.RentDelete()

        def toMoveOnSellPage():
            if pageNumber == 1:
                frame.destroy()
                mySellTable.SellTable()
            elif pageNumber == 2:
                frame.destroy()
                sellSearch.SellSearch()
            else:
                frame.destroy()
                delSell.SellDelete()

        def toMoveOnUserPage():
            if pageNumber == 1:
                frame.destroy()
                myUserDetails.UserTable()
            elif pageNumber == 2:
                frame.destroy()
                userSearch.UserSearch()
            else:
                frame.destroy()
                dellUser.UserDelete()

        pur = ImageTk.PhotoImage(Image.open("purchaseDis.jpg"))
        myFrame1 = Label(frame, image=pur)
        myFrame1.place(x=0, y=0, width=422, height=494)
        myFrame1.config(bg="cornsilk")
        myPur = Button(frame, text="PURCHASE", font=("Times New Roman", 24, "bold"), borderwidth=0,
                       command=toMoveOnPurchasePage)
        myPur.place(x=0, y=494, width=422, height=40)
        myPur.config(bg="mediumpurple", fg="white", activeforeground="mediumpurple", activebackground="white")

        ren = ImageTk.PhotoImage(Image.open("rentComb.jpg"))
        myFrame2 = Label(frame, image=ren)
        myFrame2.place(x=422, y=0, width=422, height=494)
        myFrame2.config(bg="aqua")
        myRen = Button(frame, text="RENT", font=("Times New Roman", 24, "bold"), borderwidth=0,
                       command=toMoveOnRentPage)
        myRen.place(x=422, y=494, width=422, height=40)
        myRen.config(bg="mediumpurple", fg="white", activeforeground="mediumpurple", activebackground="white")

        sell = ImageTk.PhotoImage(Image.open("sellDis.jpg"))
        myFrame3 = Label(frame, image=sell)
        myFrame3.place(x=844, y=0, width=422, height=494)
        mySol = Button(frame, text="SELL", font=("Times New Roman", 24, "bold"), borderwidth=0,
                       command=toMoveOnSellPage)
        mySol.place(x=844, y=494, width=422, height=40)
        mySol.config(bg="mediumpurple", fg="white", activeforeground="mediumpurple", activebackground="white")

        myInfo = Button(frame, text=f"USER", font=("Times New Roman", 22, "bold"))
        myInfo.place(x=0, y=534, width=1266, height=78.2)
        myInfo.config(bg="white", fg="mediumpurple", borderwidth=0, activeforeground="mediumpurple",
                      activebackground="white", command=toMoveOnUserPage)

        Back = Button(frame, text="↤", font=("Lato", 30, "bold"), command=toMoveBack)
        Back.place(x=0, y=612.2, width=1266, height=55)
        Back.config(bg="mediumpurple", fg="white", borderwidth=0
                    , activeforeground="white",
                    activebackground="mediumpurple")

        frame.mainloop()


if __name__ == "__main__":
    newPage = AdminCombination(1)